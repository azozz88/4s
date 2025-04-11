import requests
import random
import threading
import time
from uuid import uuid4
from colorama import Fore, init
import os
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import urllib3


init(autoreset=True)


token = "7206423294:AAFvvpyL4oFovo-E8fOSA5AzHaeANeZGjtU"
chat_id = '5290179758'
# Add Discord webhook URL
discord_webhook_url = "https://discord.com/api/webhooks/1359929777162817819/-wBHa6QsJaQxQX8fjiHm6vol92FD4ZfjvCSlbRvb1BFM2FGQk0VA3fPd5_IZiSYm6ZEL"
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

# إعداد جلسة طلبات مع إعادة المحاولة
def create_session():
    session = requests.Session()
    retry = Retry(
        total=2,  # Reduced further to 2
        backoff_factor=2.0,  # Increased to 2.0
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["POST", "GET"]
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

# إنشاء جلسة واحدة للاستخدام في جميع الطلبات
session = create_session()

# Add proxy rotation functionality
proxies = []
try:
    with open(os.path.join(os.path.dirname(__file__), 'proxies.txt'), 'r') as f:
        proxies = [line.strip() for line in f if line.strip()]
    print(f"{Fore.CYAN}Loaded {len(proxies)} proxies")
except Exception as e:
    print(f"{Fore.YELLOW}No proxies loaded: {e}")

def get_proxy():
    if not proxies:
        return None
    return {"http": f"http://{random.choice(proxies)}", 
            "https": f"http://{random.choice(proxies)}"}

# Add rate limiting
request_times = []
MAX_REQUESTS_PER_MINUTE = 10  # Reduced from 20 to 10
COOLDOWN_PERIOD = 300  # 5 minutes cooldown after too many errors

# Track errors
error_count = 0
last_error_time = 0
in_cooldown = False

def rate_limited_request(method, url, **kwargs):
    global request_times, error_count, last_error_time, in_cooldown
    
    # Check if we're in cooldown period
    if in_cooldown:
        current_time = time.time()
        if current_time - last_error_time < COOLDOWN_PERIOD:
            remaining = COOLDOWN_PERIOD - (current_time - last_error_time)
            print(f"{Fore.RED}In cooldown period. Waiting {remaining:.0f} seconds...")
            time.sleep(min(remaining, 10))  # Sleep at most 10 seconds at a time
            return None
        else:
            in_cooldown = False
            error_count = 0
    
    # Clean up old request times
    current_time = time.time()
    request_times = [t for t in request_times if current_time - t < 60]
    
    # Check if we've made too many requests in the last minute
    if len(request_times) >= MAX_REQUESTS_PER_MINUTE:
        sleep_time = 60 - (current_time - request_times[0]) + random.uniform(1, 3)
        print(f"{Fore.YELLOW}Rate limiting: sleeping for {sleep_time:.2f} seconds")
        time.sleep(sleep_time)
    
    # Add current request time
    request_times.append(time.time())
    
    # Use a proxy if available
    if 'proxies' not in kwargs:
        proxy = get_proxy()
        if proxy:
            kwargs['proxies'] = proxy
    
    # Disable SSL verification for all requests
    if 'verify' not in kwargs:
        kwargs['verify'] = False
    
    # Add random delay
    time.sleep(random.uniform(0.5, 2.0))
    
    # Make the request
    try:
        return getattr(session, method)(url, **kwargs)
    except Exception as e:
        error_count += 1
        last_error_time = time.time()
        
        # If too many errors, enter cooldown period
        if error_count >= 5:
            print(f"{Fore.RED}Too many errors ({error_count}). Entering cooldown period for {COOLDOWN_PERIOD} seconds.")
            in_cooldown = True
        
        raise e

def oopp():
    v1 = random.choice(om)
    v2 = random.choice(ooo)
    v3 = random.choice(ooo)
    v4 = random.choice(ooo)
    v5 = random.choice(op)

    user1 = v1 + v1 + v5 + v2 + v3
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

def a1():
    global a, s
    while True:
        try:
            user = oopp()
            data = {
                "email": "abdo1@gmail.com",
                "username": user,
                "password": "Aa123456" + user,
                "device_id": "android-" + str(uuid4()),
                "guid": str(uuid4()),
            }

            # Use rate limited request instead of direct session
            response = rate_limited_request("post", url, headers=headers, data=data, timeout=30)
            
            # If in cooldown, skip this iteration
            if response is None:
                continue
                
            response_text = response.text

            if '"email_is_taken"' in response_text:
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
                # إرسال إلى تيليجرام مع إعادة المحاولة
                try:
                    rate_limited_request("post", f'https://api.telegram.org/bot{token}/sendMessage', 
                                data={'chat_id': chat_id, 'text': message},
                                timeout=10)
                except Exception as e:
                    print(f"{Fore.YELLOW}Telegram notification failed: {e}")
                
                # إرسال إلى ديسكورد
                send_to_discord(user)
            else:
                s += 1

            print(f"\r{Fore.GREEN}Good ✅ {a} | {Fore.RED}Ban ❌ {s}", end='', flush=True)
            
        except Exception as e:
            print(f"\r{Fore.RED}Error: {str(e)[:100]}...", end='', flush=True)
            time.sleep(10)  # Increased to 10 seconds

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
        rate_limited_request("post", discord_webhook_url, json=discord_data, timeout=10)
    except Exception as e:
        print(f"{Fore.RED}Error sending to Discord: {e}")

print(f"{Fore.GREEN}Good ✅ 0 | {Fore.RED}Ban ❌ 0\n")
print(f"{Fore.CYAN}Starting with rate limit of {MAX_REQUESTS_PER_MINUTE} requests per minute")

# Create proxies.txt file if it doesn't exist
if not os.path.exists(os.path.join(os.path.dirname(__file__), 'proxies.txt')):
    with open(os.path.join(os.path.dirname(__file__), 'proxies.txt'), 'w') as f:
        f.write("# Add your proxies here, one per line in format: ip:port or user:pass@ip:port\n")
    print(f"{Fore.YELLOW}Created proxies.txt file. Add your proxies there for better performance.")

# Reduce number of threads to avoid rate limiting
thread_count = 3  # Reduced from 5 to 3
threads = []
for _ in range(thread_count):  
    t = threading.Thread(target=a1)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
