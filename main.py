from colorama import Fore, init
import requests
import datetime
from tzlocal import get_localzone
import json
import webbrowser
import time
import subprocess
import base64
import faker
import uuid
import os
import qrcode
import subprocess
import random
import schedule
from googletrans import Translator
import ctypes
import re
import random
import string
import pyperclip
init(autoreset=True)

local_timezone = datetime.timezone(datetime.timedelta(hours=0))
timed = datetime.datetime.now(local_timezone).strftime('%Y-%m-%d %H:%M:%S %Z')
opened1 = timed + " Running Xelestia \n"

with open('logs.txt', 'a') as f:
    f.write(opened1)
    f.write("\n")

creator = r"""____  ___     .__                   __  .__        
\   \/  /____ |  |   ____   _______/  |_|__|____   
 \     // __ \|  | _/ __ \ /  ___/\   __\  \__  \  
 /     \  ___/|  |_\  ___/ \___ \  |  | |  |/ __ \_
/___/\  \___  >____/\___  >____  > |__| |__(____  /
      \_/   \/          \/     \/               \/

                    Things I Made For No Reason.
"""

def clear_console():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_random_username():
    random_uuid = str(uuid.uuid4()).replace("-", "")
    username = random_uuid[:8]
    return username

def delete_webhook(url):
    try:
        timed = datetime.datetime.now(local_timezone).strftime('%Y-%m-%d %H:%M:%S %Z')
        timeoption = timed + " Option [2] Selected - Deletes a certain webhook \n."
        with open('logs.txt', 'a') as f:
            f.write(timeoption)
        print(" ")
        delete = requests.delete(url)
        if delete.status_code == 204:
            print(Fore.LIGHTMAGENTA_EX + "Successfully deleted webhook.")
        else:
            print(f"Couldn't delete webhook. Status code: {delete.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

def send_scheduled_message(webhook_url, message_to_send):
    try:
        payload = {'content': message_to_send}
        requests.post(webhook_url, json=payload)
        print(Fore.LIGHTGREEN_EX + "Message sent successfully!")
    except Exception as e:
        print(Fore.RED + f"Error sending message: {e}")

def generate_qr_code_text(text, output_directory, filename):
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(5))
    data = f"{text} {random_numbers}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    os.makedirs(output_directory, exist_ok=True)
    file_path = os.path.join(output_directory, filename)
    img.save(file_path)
    return file_path

def generate_qr_code_url(link_base, output_directory, filename):
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(5))
    link = f"{link_base}/{random_numbers}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    os.makedirs(output_directory, exist_ok=True)
    file_path = os.path.join(output_directory, filename)
    img.save(file_path)
    return file_path

def analyze_webhook(webhook_url):
    try:
        response = requests.get(webhook_url)
        data = response.json()
        user_data = data.get('user', {})
        username = user_data.get('username', 'N/A')
        avatar = user_data.get('avatar', 'N/A')
        avatar_url = f"https://cdn.discordapp.com/avatars/{user_data.get('id', 'N/A')}/{avatar}.png" if avatar != 'N/A' else 'N/A'
        last_message_timestamp = data.get('last_message_timestamp', 'N/A')
        created_at = data.get('created_at', 'N/A')
        recent_changes = data.get('recent_changes', [])
        last_message_time = datetime.utcfromtimestamp(last_message_timestamp).strftime('%Y-%m-%d %H:%M:%S UTC') if last_message_timestamp != 'N/A' else 'N/A'
        created_at_time = datetime.utcfromtimestamp(created_at).strftime('%Y-%m-%d %H:%M:%S UTC') if created_at != 'N/A' else 'N/A'
        print(" ")
        print(Fore.LIGHTRED_EX+f"Webhook Username: {username}")
        print(Fore.LIGHTBLUE_EX+f"Avatar: {avatar} Link: {avatar_url}")
        print(Fore.LIGHTCYAN_EX+f"Last Message Timestamp: {last_message_time}")
        print(Fore.LIGHTGREEN_EX+f"Webhook Created At: {created_at_time}")

        if recent_changes:
            print("Recent Changes:")
            for change in recent_changes:
                print(f"- {change.get('change', 'N/A')} at {datetime.utcfromtimestamp(change.get('timestamp', 0)).strftime('%Y-%m-%d %H:%M:%S UTC')}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def check_webhook(webhook_url):
    try:
        response = requests.head(webhook_url)
        if response.status_code == 200:
            print(Fore.LIGHTGREEN_EX+"Webhook is valid!")
            return True
        else:
            print(Fore.BLUE+f"Invalid webhook - Status code: {response.status_code}")
            return False
    except requests.ConnectionError:
        print(Fore.RED+"Couldn't to connect to the webhook.")
        return False

def send_to_webhook(url, amount, message):
    try:
        timed = datetime.datetime.now(local_timezone).strftime('%Y-%m-%d %H:%M:%S %Z')
        timeoption = timed + " Option [1] Selected - Sends a certain amount of messages to a certain webhook. \n"
        with open('logs.txt', 'a') as f:
            f.write(timeoption)
        print(" ")
        for i in range(amount):
            data = {'content': message}
            send = requests.post(url, json=data)
            time.sleep(0.7)
            if send.status_code == 204:
                print(Fore.LIGHTMAGENTA_EX + f"#{i + 1} Message sent.")
            else:
                print(f"Couldn't send message. Status code: {send.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

def is_valid_ip(ip_address):
    ipv4_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    ipv6_pattern = re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$')

    return ipv4_pattern.match(ip_address) or ipv6_pattern.match(ip_address)

def generate_random_password(length=12, include_numbers=True, include_special_chars=True):
    letters = string.ascii_letters
    numbers = string.digits if include_numbers else ''
    special_chars = string.punctuation if include_special_chars else ''
    if not (letters + numbers + special_chars):
        print(Fore.LIGHTCYAN_EX+"Error: Please include at least one character set.")
        return None
    password = ''.join(random.choice(letters + numbers + special_chars) for _ in range(length))
    return password

def ip_geolocation_lookup(ip_address):
    api_url = f"http://ipinfo.io/{ip_address}/json"

    try:
        response = requests.get(api_url)
        data = response.json()
        print("IP Address:", data.get("ip"))
        print("Location:", data.get("city"), data.get("region"), data.get("country"))
        print("Coordinates:", data.get("loc"))
        print("ISP:", data.get("org"))

    except requests.exceptions.RequestException as e:
        print("Error during API request:", e)
def main():
  while True:
    clear_console()
    options = """      [1] - Sends a certain amount of messages to a certain webhook.
      [2] - Deletes a certain webhook.
      [3] - Opens Github Project.
      [4] - Check's if a ip address is valid.
      [5] - Changes a certain Webhook's name.
      [6] - Changes a certain Webhook's avatar.
      [7] - Join Discord Server.
      [8] - Generate Random Password.
      [9] - IP Geolocation Lookup.
      [10] - Generates Fake Information.
      [11] - Checks If A Webhook Is Valid.
      [12] - QR Code Generator.
      [13] - Translates Text To English.
      [14] - Schedules A Messsage To Send To A Certain Webhook In A Set Amount Of Minutes.
      [15] - Analyzes Webhook Activity."""
    webhook_logs = []
    print(Fore.LIGHTRED_EX+creator)
    print(Fore.LIGHTRED_EX+options)
    option = input(f'\n{Fore.LIGHTCYAN_EX}#═╦═» {os.getlogin()}@Xelestia\n  ╚═» {Fore.GREEN}$ ')

    if option == "1":
        timed = datetime.datetime.now(local_timezone).strftime('%Y-%m-%d %H:%M:%S %Z')
        timeoption = timed + " Option [3] Selected - Opens Github Project.\n"
        with open('logs.txt', 'a') as f:
                f.write(timeoption)
        webhookurr = input(Fore.LIGHTBLUE_EX+"Enter Webhook's URL: ")
        everyone = input(Fore.LIGHTGREEN_EX+"Include @everyone in message? [y/n]: ")
        message = input(Fore.LIGHTCYAN_EX+"Enter the message content: ")
        if everyone == "y":
            afmessage = "@everyone " + message
        if everyone == "n":
            afmessage = message
        amount = int(input(Fore.LIGHTRED_EX+"Enter the amount of messages to send: "))

        send_to_webhook(webhookurr, amount, afmessage)
        time.sleep(3)
    elif option == "15":
        timed = datetime.datetime.now(local_timezone).strftime('%Y-%m-%d %H:%M:%S %Z')
        timeoption = timed + " Option [11] Selected - Checks If A Webhook Is Valid. \n"
        with open('logs.txt', 'a') as f:
                f.write(timeoption)
        webhook_url = input(Fore.LIGHTGREEN_EX+"Enter Webhook's URL you want to analyze: ")
        analyze_webhook(webhook_url)
        time.sleep(9)
    elif option == "11":
        timed = datetime.datetime.now(local_timezone).strftime('%Y-%m-%d %H:%M:%S %Z')
        timeoption = timed + " Option [11] Selected - Checks If A Webhook Is Valid. \n"
        with open('logs.txt', 'a') as f:
                f.write(timeoption)
        webhook = input(Fore.LIGHTGREEN_EX+"Enter Webhook's URL you want to check: ")
        check_webhook(webhook)
        time.sleep(4)
        
    elif option == "14":
        timed = datetime.datetime.now(local_timezone).strftime('%Y-%m-%d %H:%M:%S %Z')
        timeoption = timed + " Option [14] Selected - Schedules A Messsage To Send To A Certain Webhook In A Set Amount Of Minutes. \n"
        with open('logs.txt', 'a') as f:
                f.write(timeoption)
        web_url1 = input(Fore.LIGHTGREEN_EX+"Enter Webhook's URL: ")
        message_schedule = input(Fore.LIGHTGREEN_EX+"Enter Message To Schedule: ")
        delay_minutes = int(input(Fore.LIGHTGREEN_EX+"Enter Amount Of Minutes For Schedule: "))
        scheduled_time = datetime.datetime.now() + datetime.timedelta(minutes=delay_minutes)
        schedule.every().day.at(scheduled_time.strftime('%H:%M')).do(send_scheduled_message, web_url1, message_schedule)
        while True:
          schedule.run_pending()
          time.sleep(1) 
    elif option == "4":
        timed = datetime.datetime.now(local_timezone).strftime('%Y-%m-%d %H:%M:%S %Z')
        timeoption = timed + " Option [4] Selected - Check's if a ip address is valid. \n"
        with open('logs.txt', 'a') as f:
                f.write(timeoption)
        ip_input = input(Fore.LIGHTCYAN_EX+"Enter The IP Address You Want To Check: ")
        if is_valid_ip(ip_input):
          get_info = input("Enter if you want information for this IP (y/n): ")
          if get_info.lower() == "y":
              ip_geolocation_lookup(ip_input)
          if get_info.lower() == "n":
              time.sleep(3)
        time.sleep(3)
        
    elif option == "12":
        timed = datetime.datetime.now(local_timezone).strftime('%Y-%m-%d %H:%M:%S %Z')
        timeoption = timed + " Option [12] Selected - QR Code Generator. \n"
        with open('logs.txt', 'a') as f:
                f.write(timeoption)
        text_link = input("[text] For Text QR & [url] for URL QR: ")
        if text_link.lower() == "url":
           user_link = input(Fore.LIGHTGREEN_EX+"    Link For QR Code: ")
           random_number = random.randint(1, 1000000)
           output_directory = "qr_codes"
           random_file_name = f"urlQR{random_number}.png"
           generate_qr_code_url(user_link, output_directory, random_file_name)
           print(Fore.LIGHTMAGENTA_EX + f"QR code generated as: {random_file_name}. Inside Of qr_codes folder")
        elif text_link.lower() == "text":
          user_text = input(Fore.RED+"    Text For QR Code: ")
          output_directory = "qr_codes"
          random_number = random.randint(1, 1000000)
          random_file_name = f"textQR{random_number}.png"
          saved_file_path = generate_qr_code_text(user_text, output_directory, random_file_name)
          print(Fore.LIGHTMAGENTA_EX + f"QR code generated and saved as: {saved_file_path}. Inside Of qr_codes folder")
        else:
          print(Fore.RED + "Invalid option. Please choose [text] or [url].")
          saved_file_path = None
        time.sleep(8)
    elif option == "8":
      try:
        timed = datetime.datetime.now(local_timezone).strftime('%Y-%m-%d %H:%M:%S %Z')
        timeoption = timed + " Option [8] Selected - Generate Random Password. \n"
        with open('logs.txt', 'a') as f:
            f.write(timeoption)
        
        length = int(input(Fore.LIGHTMAGENTA_EX+"Enter the length of the password: "))
        include_numbers = input(Fore.LIGHTCYAN_EX+"Include numbers? (y/n): ").lower() == 'y'
        include_special_chars = input(Fore.LIGHTGREEN_EX+"Include special characters? (y/n): ").lower() == 'y'
        generated_password = generate_random_password(length, include_numbers, include_special_chars)
        if generated_password:
            print(f"Generated Password: {generated_password}")
            copy_to_clipboard = input(Fore.LIGHTRED_EX+"Do you want to copy the password to the clipboard? (y/n): ").lower()
            if copy_to_clipboard == 'y':
                pyperclip.copy(generated_password)
                print(" ")
                print(Fore.LIGHTRED_EX+"Password copied to clipboard.")
        else:
            print(" ")
            print(Fore.LIGHTRED_EX+"Password generation failed.")
      except Exception as e:
        print(f"An error occurred: {e}")
    elif option == "13":
        timed = datetime.datetime.now(local_timezone).strftime('%Y-%m-%d %H:%M:%S %Z')
        timeoption = timed + " Option [13] Selected - Translates Text To English. \n"
        with open('logs.txt', 'a') as f:
                f.write(timeoption)
        text_to_translate = input(Fore.LIGHTRED_EX+"Enter text to translate: ")
        translator = Translator()
        translated_text = translator.translate(text_to_translate, src='auto', dest='en').text
        print(Fore.LIGHTMAGENTA_EX + f"   Original Text: {text_to_translate}")
        print(Fore.LIGHTMAGENTA_EX + f"   Translated Text: {translated_text}")
        time.sleep(6)
    elif option == "9":
        timed = datetime.datetime.now(local_timezone).strftime('%Y-%m-%d %H:%M:%S %Z')
        timeoption = timed + " Option [9] Selected - IP Geolocation Lookup. \n"
        with open('logs.txt', 'a') as f:
                f.write(timeoption)
        wanted_ip = input(Fore.LIGHTCYAN_EX+"Enter The Ip You Want to look up: ")
        ip_geolocation_lookup(wanted_ip)
        time.sleep(10)
        
    elif option == "10":
        timed = datetime.datetime.now(local_timezone).strftime('%Y-%m-%d %H:%M:%S %Z')
        timeoption = timed + " Option [10] Selected - Generates Fake Information \n"
        with open('logs.txt', 'a') as f:
                f.write(timeoption)
        fake = faker.Faker()
        fake_name = fake.name()
        print(Fore.LIGHTGREEN_EX+f"Fake Name: {fake_name}")
        fake_ip = fake.ipv4()
        print(Fore.LIGHTGREEN_EX+f"Fake IP: {fake_ip}")
        fake_username = generate_random_username()
        print(Fore.LIGHTGREEN_EX+f"Fake Username: {fake_username}")
        time.sleep(10)

    elif option == "7":
      try:
            timed = datetime.datetime.now(local_timezone).strftime('%Y-%m-%d %H:%M:%S %Z')
            timeoption = timed + " Option [7] Selected - Join Discord Server. \n"
            with open('logs.txt', 'a') as f:
                f.write(timeoption)
            webbrowser.open('https://discord.gg/4PBMAPP6BA')
            print(Fore.BLUE + "Successfully Opened Discord Server.")
      except Exception as e:
            print(Fore.RED + f"Couldn't Open Discord Server: {e}")
      time.sleep(4)
    elif option == "3":
        try:
            timed = datetime.datetime.now(local_timezone).strftime('%Y-%m-%d %H:%M:%S %Z')
            timeoption = timed + " Option [3] Selected - Opens Github Project.\n"
            with open('logs.txt', 'a') as f:
                f.write(timeoption)
            webbrowser.open('https://github.com/tnaeso/Xelestia')
            print(Fore.BLUE + "Successfully Opened Github Project")
            time.sleep(4)
        except Exception as e:
            print(Fore.RED + f"Couldn't Open Github Project: {e}")
            time.sleep(4)
    elif option == "5":
     try:
        timed = datetime.datetime.now(local_timezone).strftime('%Y-%m-%d %H:%M:%S %Z')
        timeoption = timed + " Option [5] Selected - Changes Webhook's name. \n"
        with open('logs.txt', 'a') as f:
            f.write(timeoption)
        weburll = input(Fore.LIGHTMAGENTA_EX+"Enter Webhook URL: ")
        name = input(Fore.LIGHTMAGENTA_EX + "Enter Webhook's New Username: ")
        r = requests.patch(weburll, json={"name": f"{name}"})
        if r.status_code == 200:
            print(Fore.GREEN + "Webhook name updated successfully.")
        else:
            print(Fore.RED + f"Failed to update webhook name. Status code: {r.status_code}")
     except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
        time.sleep(4)
    elif option == "6":
     try:
        timed = datetime.datetime.now(local_timezone).strftime('%Y-%m-%d %H:%M:%S %Z')
        timeoption = timed + "    Option [6] Selected - Changes Webhook's avatar. \n"
        with open('logs.txt', 'a') as f:
            f.write(timeoption)
        weburl = input("    Enter Webhook URL: ")
        avatar_location = input("    Enter Image Location: ")
        with open(avatar_location, "rb") as avatar_file:
            avatar_data = avatar_file.read()
        headers = {
            "Content-Type": "application/json",
        }
        avatar_base64 = base64.b64encode(avatar_data).decode('utf-8')
        data = {
            "avatar": f"data:image/png;base64,{avatar_base64}"
        }
        response = requests.patch(weburl, headers=headers, json=data)
        if response.status_code == 200:
            print("    Webhook avatar updated successfully.")
        else:
            print(f"    Failed to update webhook avatar. Status code: {response.status_code}")

     except Exception as e:
        print(f"    An error occurred: {e}")
    time.sleep(4)

if __name__ == "__main__":
    main()
