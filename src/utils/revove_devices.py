import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.utils.const import ldconsole_path

def remove_nonexistent_devices(ld_devices, json_array):
    """
    Xóa thiết bị không tồn tại trong json_array từ ld_devices.
    Giữ lại chỉ thiết bị mặc định.
    """
    # Tạo tập hợp email từ json_array để dễ kiểm tra
    existing_emails = {entry['email'] for entry in json_array}

    for device in ld_devices:
        # Nếu thiết bị không tồn tại trong json_array, xóa nó
        if device not in existing_emails:
            if device not in "default":
                # print(f"Removing device: {device}")
                remove_device(device)  # Giả định hàm xóa thiết bị

def remove_device(device_name):
    command = f'{ldconsole_path} remove --name {device_name}'
    print(f"Running command: {command}")
    os.system(command)