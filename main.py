import threading
import asyncio
from adb_utils import run_adb_devices
from app.uiautomator_utils import interact_with_device
from devices.start_device  import start_ldplayer
import json
import subprocess
import sys

# Danh sách các thư viện cần cài đặt
required_packages = [
    "adb-utils",  # Thay đổi tên gói nếu cần
    "uiautomator2",  # Thay đổi tên gói nếu cần
    "json",  # Thư viện json là tích hợp sẵn trong Python, không cần cài đặt
    "numpy",
    "opencv-python"
]

# Hàm để cài đặt gói
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Kiểm tra và cài đặt từng gói
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"{package} chưa được cài đặt. Đang cài đặt...")
        install(package)

print("Tất cả các thư viện cần thiết đã được cài đặt.")

def run_devices_multithreaded():
    """
    Chạy các thiết bị đồng thời (đa luồng) bằng cách sử dụng adb và uiautomator.
    """
    devices = run_adb_devices()


    # devices = [
    #     {
    #         'device_id': 'emulator-5554',
    #         'proxy_address': '192.168.1.82',
    #         'proxy_port': '10014'
    #     },
    #     {
    #         'device_id': 'emulator-5556',
    #         'proxy_address': '192.168.1.82',
    #         'proxy_port': '10015'
    #     }
    # ]
    if devices:
        threads = []
        for device in devices:
            t = threading.Thread(target=interact_with_device, args=(device,))
            threads.append(t)
            t.start()
        
        # Đợi tất cả các luồng kết thúc
        for t in threads:
            t.join()
    else:
        print("No devices found.")

async def main():
    await start_ldplayer(0)
    # run_devices_multithreaded()

# Chạy hàm chính
if __name__ == "__main__":
    asyncio.run(main())
