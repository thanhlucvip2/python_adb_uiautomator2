import subprocess
import sys
import os
import random
import json
import subprocess

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.utils.const import model_phone, phone_file_path, ldconsole_path, proxy_file_path

def run_adb_devices():
    """
    Chạy lệnh adb devices và trả về danh sách thiết bị kết nối.
    """
    result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Devices connected:")
        devices_str = result.stdout
        devices_list = [line.split()[0] for line in devices_str.strip().split('\n')[1:] if line.strip()]
        return devices_list
    else:
        print("Error running adb devices:")
        print(result.stderr)
        return []

def load_json_file(file_path):
    with open(file_path, 'r') as json_file:
        return json.load(json_file)

def save_json_file(file_path, data):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def get_ld_devices():
    command = f'{ldconsole_path} list'
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout.splitlines()  # Trả về danh sách các thiết bị

def copy_adb_devices(email):
    command = f'{ldconsole_path} copy --name {email} --from 0'
    print(f"Running command: {command}")
    os.system(command)

def set_phone_number(email, phone):
    command = f'{ldconsole_path} modify --name {email} --pnumber {phone}'
    print(f"Running command: {command}")
    os.system(command)

def get_random_phone_number():
    with open(phone_file_path, 'r') as f:
        phone_numbers = f.readlines()
    phone_numbers = [phone.strip() for phone in phone_numbers]
    phone = random.choice(phone_numbers)
    phone_numbers.remove(phone)
    with open(phone_file_path, 'w') as f:
        for number in phone_numbers:
            f.write(number + '\n')
    return phone

def get_random_proxy():
    with open(proxy_file_path, 'r') as f:
        proxy_data = f.readlines()
    proxy_data = [proxy.strip() for proxy in proxy_data]
    proxy = random.choice(proxy_data)
    proxy_data.remove(proxy)
    with open(proxy_file_path, 'w') as f:
        for number in proxy_data:
            f.write(number + '\n')
    return proxy

def get_random_manufacturer_and_model():
    manufacturer_data = random.choice(model_phone)
    return {
       "manufacturer": manufacturer_data['maker'], "model": manufacturer_data['model']
    }
    
def set_phone_model(email, phone_model):
    command = f'{ldconsole_path} modify --name {email} --manufacturer {phone_model["manufacturer"]} --model {phone_model["model"]}'
    print(f"Running command: {command}")
    os.system(command)

async def start_ldplayer(email):
    command = f'{ldconsole_path} launch --name {email}'
    print(f"Running command: {command}")
    os.system(command)

def close_ldplayer(email):
    command = f'{ldconsole_path} quit  --name {email}'
    print(f"Running command: {command}")
    os.system(command)
