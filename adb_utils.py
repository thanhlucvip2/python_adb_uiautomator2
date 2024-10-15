import subprocess

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
