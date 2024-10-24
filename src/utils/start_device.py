import os
import sys
import time
import asyncio
import uiautomator2 as u2

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.utils.adb_utils import run_adb_devices
from src.utils.const import ldconsole_path

# Function để khởi động LDPlayer dựa vào index
async def start_ldplayer(device_name):
    command = f'{ldconsole_path} launch --name {device_name}'
    print(f"Running command: {command}")
    os.system(command)

    print(f"Đang khởi động LDPlayer với name {device_name}...")
    await  wait_for_device_online()
    await_time = 30
    # for _ in range(await_time):
    #     device_id = run_adb_devices()
    #     print(device_id)
    #     if device_id and device_id[device_name]:
    #         print("Thiết bị LDPlayer đã online.")
    #         return
    #     else:
    #         print("Đang đợi thiết bị LDPlayer online...")
    #         await asyncio.sleep(1)  # Chờ 1 giây trước khi kiểm tra lại

# Function để kiểm tra thiết bị LDPlayer đã online chưa
async def wait_for_device_online():
    while True:
        # Kiểm tra danh sách thiết bị qua adb
        result = os.popen('adb devices').read()
        print(result)

        if False:
            print("Đã khởi động thiết bị")
            break
        else:
            print("Đang khởi động thiết bị...")
            await asyncio.sleep(2)  # Đợi 2 giây rồi kiểm tra lại

# # Function kết nối uiautomator2 với LDPlayer qua adb
# def connect_uiautomator2(device_ip):
#     d = u2.connect(device_ip)
#     if d:
#         print(f"Kết nối thành công với thiết bị: {device_ip}")
#     else:
#         print(f"Không thể kết nối với thiết bị: {device_ip}")
#     return d
 

async def main():
    await start_ldplayer("seobaba12345@gmail.com")
    
if __name__ == "__main__":
    asyncio.run(main())
