import requests
import random
import threading
import time
from uuid import uuid4
from colorama import Fore, init
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

init(autoreset=True)

# Use environment variables with fallbacks
token = os.getenv("TELEGRAM_TOKEN", "7206423294:AAFvvpyL4oFovo-E8fOSA5AzHaeANeZGjtU")
chat_id = os.getenv("TELEGRAM_CHAT_ID", '5290179758')
discord_webhook_url = os.getenv("DISCORD_WEBHOOK", "https://discord.com/api/webhooks/1359929777162817819/-wBHa6QsJaQxQX8fjiHm6vol92FD4ZfjvCSlbRvb1BFM2FGQk0VA3fPd5_IZiSYm6ZEL")
a = 0
s = 0


om = 'qwertyuioplkjhgfdsazxcvbnmc'
ooo = 'qwertyuiopalkjhgfdsazxcvbnm0987654321'
op = '_.'
url = 'https://i.instagram.com/api/v1/accounts/create/'
headers = {
    'Content-Length': '437',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'i.instagram.com',
    'Connection': 'Keep-Alive',
    'User-Agent': 'Instagram 6.12.1 Android (30/11; 480dpi; 1080x2298; HONOR; ANY-LX2; HNANY-Q1; qcom; en_IQ)',
    'Accept-Language': 'en-IQ, en-US',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': 'AQ==',
    'Accept-Encoding': 'gzip',
}

def oopp():
    v1 = random.choice(om)
    v2 = random.choice(ooo)
    v3 = random.choice(ooo)
    v4 = random.choice(ooo)
    v5 = random.choice(op)

    user1 = v1 + v1 + v5 + v2 + v3
    user2 = v1 + v1 + v2 + v5 + v3
    user3 = v2 + v2 + v5 + v3 + v4
    user4 = v2 + v2 + v3 + v5 + v4
    user5 = v4 + v3 + v5 + v2 + v2
    user6 = v4 + v5 + v3 + v2 + v2
    user7 = v4 + v5 + v3 + v1 + v1
    user8 = v4 + v3 + v5 + v1 + v1
    user9 = v5 + v1 + v1 + v3 + v2
    user10 = v5 + v3 + v1 + v1 + v2
    user11 = v4 + v2 + v1 + v1 + v5
    user12 = v4 + v1 + v1 + v2 + v5
    user13 = v2 + v2 + v3 + v3 + v5
    user14 = v3 + v2 + v2 + v4 + v5
    user15 = v3 + v4 + v2 + v2 + v5
    user16 = v5 + v3 + v4 + v2 + v2
    user17 = v5 + v4 + v2 + v2 + v3
    user18 = v5 + v2 + v2 + v4 + v3
    user17 = v5 + v4 + v2 + v2 + v3
    user18 = v5 + v2 + v2 + v4 + v3
    user19 = v1 + v1 + v5 + v1 + v3
    user20 = v1 + v1 + v2 + v5 + v1
    user21 = v2 + v2 + v5 + v1 + v4
    user22 = v2 + v2 + v1 + v5 + v4
    user23 = v4 + v1 + v5 + v2 + v2
    user24 = v4 + v5 + v1 + v2 + v2
    user25 = v4 + v5 + v1 + v1 + v1
    user26 = v4 + v1 + v5 + v1 + v1
    user27 = v5 + v1 + v1 + v1 + v2
    user28 = v5 + v1 + v1 + v1 + v2
    user29 = v4 + v2 + v1 + v1 + v5
    user30 = v4 + v1 + v1 + v2 + v5
    user31 = v2 + v2 + v1 + v4 + v5
    user32 = v1 + v2 + v2 + v4 + v5
    user33 = v1 + v4 + v2 + v2 + v5
    user34 = v5 + v1 + v4 + v2 + v2
    user35 = v5 + v4 + v2 + v2 + v1
    user36 = v5 + v2 + v2 + v4 + v1
    user37 = v5 + v4 + v2 + v2 + v1
    user38 = v5 + v2 + v2 + v4 + v1


    return random.choice([user1, user2, user3, user4, user5, user6, user7, user8, user9, user10, user11, user12, user13, user14, user15, user16, user17, user18, user19, user20, user21, user22, user23, user24, user25, user26, user27, user28, user29, user30, user31, user32, user33, user34, user35, user36, user37, user38]) 


def send_to_discord(username):
    """Send username to Discord webhook"""
    discord_data = {
        "content": "",
        "embeds": [{
            "title": "Good User Instagram",
            "description": f"Username: **{username}**",
            "color": 5814783,  # Green color
            "footer": {
                "text": "dev: RL"
            }
        }]
    }
    try:
        requests.post(discord_webhook_url, json=discord_data)
    except Exception as e:
        print(f"{Fore.RED}Error sending to Discord: {e}")

def a1():
    global a, s
    while True:
        user = oopp()
        data = {
            "email": "abdo1@gmail.com",
            "username": user,
            "password": "Aa123456" + user,
            "device_id": "android-" + str(uuid4()),
            "guid": str(uuid4()),
        }

        try:
            response = requests.post(url, headers=headers, data=data).text

            if '"email_is_taken"' in response:
                print(Fore.GREEN + f'Good User: {user}')  
                a += 1

                message = f'''
-> Good User Instagram
------------------------------------------
-> User : {user}
------------------------------------------
-> dev : LEGEND
------------------------------------------
'''
                # Send to Telegram
                requests.post(f'https://api.telegram.org/bot{token}/sendMessage', data={'chat_id': chat_id, 'text': message})
                
                # Send to Discord webhook
                send_to_discord(user)
            else:
                s += 1

            print(f"\r{Fore.GREEN}Good ✅ {a} | {Fore.RED}Ban ❌ {s}", end='', flush=True)
            
        except requests.exceptions.RequestException:
            time.sleep(0.5)

print(f"{Fore.GREEN}Good ✅ 0 | {Fore.RED}Ban ❌ 0\n")
threads = []
for _ in range(20):  
    t = threading.Thread(target=a1)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
