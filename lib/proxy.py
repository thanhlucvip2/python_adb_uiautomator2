import subprocess

def change_proxy(device_id, proxy_address, proxy_port):
    """
    Thay đổi cấu hình proxy cho thiết bị Android thông qua ADB.
    
    :param device_id: ID của thiết bị Android (VD: 'emulator-5554' hoặc '192.168.1.100:5555')
    :param proxy_address: Địa chỉ proxy (VD: '192.168.1.1')
    :param proxy_port: Cổng proxy (VD: '8080')
    """
    try:
        # Kết nối với thiết bị thông qua ADB
        print(f"Kết nối với thiết bị {device_id}")
        subprocess.run(["adb", "-s", device_id, "root"], check=True)
        
        # Bật chế độ proxy
        print(f"Đang thiết lập proxy: {proxy_address}:{proxy_port}")
        subprocess.run([
            "adb", "-s", device_id, "shell", "settings", "put", "global", "http_proxy", f"{proxy_address}:{proxy_port}"
        ], check=True)
        
        # Bật lại proxy
        subprocess.run([
            "adb", "-s", device_id, "shell", "settings", "put", "global", "global_http_proxy_host", proxy_address
        ], check=True)
        
        subprocess.run([
            "adb", "-s", device_id, "shell", "settings", "put", "global", "global_http_proxy_port", proxy_port
        ], check=True)
        
        print(f"Proxy đã được thay đổi thành {proxy_address}:{proxy_port} cho thiết bị {device_id}")
        
        # Xác minh xem proxy đã thay đổi chưa
        result = subprocess.run(
            ["adb", "-s", device_id, "shell", "settings", "get", "global", "http_proxy"],
            capture_output=True, text=True
        )
        print(f"Proxy hiện tại: {result.stdout.strip()}")
    
    except subprocess.CalledProcessError as e:
        print(f"Đã xảy ra lỗi khi thay đổi proxy: {e}")
