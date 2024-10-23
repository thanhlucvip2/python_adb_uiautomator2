import os
import time
import asyncio
import uiautomator2 as u2
from adb_utils import run_adb_devices

# Function để khởi động LDPlayer dựa vào index
async def start_ldplayer(index):
    command = f'D:\LDPlayer\LDPlayer9\LDConsole.exe launch --index {index}'
    os.system(command)
    print(f"Đang khởi động LDPlayer với index {index}...")
    await  wait_for_device_online()
    await_time = 30
    for _ in range(await_time):
        device_id = run_adb_devices()
        print(device_id)
        if device_id and device_id[index]:
            print("Thiết bị LDPlayer đã online.")
            return
        else:
            print("Đang đợi thiết bị LDPlayer online...")
            await asyncio.sleep(1)  # Chờ 1 giây trước khi kiểm tra lại

# Function để kiểm tra thiết bị LDPlayer đã online chưa
async def wait_for_device_online():
    while True:
        # Kiểm tra danh sách thiết bị qua adb
        result = os.popen('adb devices').read()
        if 'device' in result:
            print("Đã khởi động thiết bị")
            break
        else:
            print("Đang khởi động thiết bị...")
            await asyncio.sleep(2)  # Đợi 2 giây rồi kiểm tra lại

# Function kết nối uiautomator2 với LDPlayer qua adb
def connect_uiautomator2(device_ip):
    d = u2.connect(device_ip)
    if d:
        print(f"Kết nối thành công với thiết bị: {device_ip}")
    else:
        print(f"Không thể kết nối với thiết bị: {device_ip}")
    return d
 

async def main():
    await start_ldplayer(0)