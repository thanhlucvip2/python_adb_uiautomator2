import threading
from adb_utils import run_adb_devices
from uiautomator_utils import interact_with_device

def run_devices_multithreaded():
    """
    Chạy các thiết bị đồng thời (đa luồng) bằng cách sử dụng adb và uiautomator.
    """
    # devices = run_adb_devices()
    devices = ['emulator-5554', 'emulator-5556']

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

if __name__ == "__main__":
    run_devices_multithreaded()
