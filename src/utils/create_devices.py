import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.utils.adb_utils import get_ld_devices, get_random_manufacturer_and_model, get_random_phone_number, set_phone_model, copy_adb_devices, set_phone_number
from src.utils.revove_devices import remove_nonexistent_devices

output_file_path = 'output.json'

with open(output_file_path, 'r', encoding='utf-8') as json_data:
    jsonData = json.load(json_data)

def find_email_index(email):
    for index, item in enumerate(jsonData):
        if item.get('email') == email:
            return index
    return -1

def process_email_file(file_path='./email.txt'):
    try:
        # Đọc file email
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        json_array = []
        ld_devices = get_ld_devices()

        def create_json_object(parts):
            index = find_email_index(parts[0])
            return {
                "email": parts[0] if len(parts[0]) > 0 else None,
                "password": parts[1] if len(parts[1]) > 0 else None,
                "recovery_mail": parts[2] if len(parts[2]) > 0 else None,
                "proxy":  parts[3] if len(parts[3]) > 0 else None,
                "device": jsonData[index]['device'] if index != -1 and jsonData[index]['device'] else get_random_manufacturer_and_model(),
                "phone":jsonData[index]['phone'] if index != -1 and jsonData[index]['phone'] else get_random_phone_number(),
                "is_device": False,
                "is_active": False,
            }

        # Tạo json_array từ file
        for line in lines:
            parts = line.strip().split('|')
            json_array.append(create_json_object(parts))

        # Cập nhật is_device dựa trên danh sách ld_devices
        ld_device_set = set(ld_devices)
        for entry in json_array:
            if entry['email'] in ld_device_set:
                entry['is_device'] = True

        # Sao chép thiết bị ADB nếu is_device là False
        for entry in json_array:
            if not entry.get("is_device"):  # Kiểm tra if is_device là False
                copy_adb_devices(entry["email"])
                set_phone_model(entry["email"], entry["device"])
                set_phone_number(entry["email"], entry["phone"] )
                entry['is_device'] = True

        # Ghi dữ liệu JSON vào file output.json
        json_output = json.dumps(json_array, indent=4)
        with open(output_file_path, 'w', encoding='utf-8') as json_file:
            json_file.write(json_output)

         # Gọi hàm xóa thiết bị không tồn tại
        remove_nonexistent_devices(ld_devices, json_array)
    
        return True  # Trả về True nếu chạy thành công

    except Exception as e:
        print(f"An error occurred: {e}")
        return False  # Trả về False nếu có lỗi

# Gọi hàm và kiểm tra kết quả
if __name__ == "__main__":
    success = process_email_file()
    print(f"Process completed successfully: {success}")