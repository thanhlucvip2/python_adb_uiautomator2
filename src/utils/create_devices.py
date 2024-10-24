import json
import sys
import os
import asyncio
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.utils.adb_utils import close_ldplayer, get_ld_devices, get_random_manufacturer_and_model, get_random_phone_number, get_random_proxy, set_phone_model, copy_adb_devices, set_phone_number, start_ldplayer
from src.utils.revove_devices import remove_nonexistent_devices
from src.utils.const import output_file_path, email_file_path, ldconsole_path

with open(output_file_path, 'r', encoding='utf-8') as json_data:
    jsonData = json.load(json_data)

def find_email_index(email):
    for index, item in enumerate(jsonData):
        if item.get('email') == email:
            return index
    return -1

def create_json_object(parts):
    index = find_email_index(parts[0])
    return {
        "email": parts[0] if len(parts[0]) > 0 else None,
        "password": parts[1] if len(parts[1]) > 0 else None,
        "recovery_mail": parts[2] if len(parts[2]) > 0 else None,
        "proxy":  jsonData[index]['proxy'] if index != -1 and jsonData[index]['proxy'] else get_random_proxy(),
        "device": jsonData[index]['device'] if index != -1 and jsonData[index]['device'] else get_random_manufacturer_and_model(),
        "phone": jsonData[index]['phone'] if index != -1 and jsonData[index]['phone'] else get_random_phone_number(),
        "serial_number":  jsonData[index]['serial_number'] if index != -1 and jsonData[index]['serial_number'] else None,
        "is_device": False,
        "is_active": False,
    }
    
async def process_email_file(file_path=email_file_path):
    try:
        # Đọc file email
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        json_array = []
        ld_devices = get_ld_devices()
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
                await asyncio.sleep(15)  # Đợi 14 giây 
                await asyncio.sleep(2)  # Đợi 2 giây rồi kiểm tra lại
                await start_ldplayer(entry["email"])
                serial_number = await wait_for_device_online()
                set_phone_model(entry["email"], entry["device"])
                set_phone_number(entry["email"], entry["phone"] )
                entry['is_device'] = True
                entry['serial_number'] = serial_number
                # close_ldplayer(entry["email"])
                await asyncio.sleep(2)  # Đợi 2 giây rồi kiểm tra lại
            else:
                if not entry.get('serial_number'):
                    await start_ldplayer(entry["email"])
                    serial_number = await wait_for_device_online()
                    entry['serial_number'] = serial_number
                    # close_ldplayer(entry["email"])
                    # await asyncio.sleep(2)  # Đợi 2 giây rồi kiểm tra lại
                    print("==============")
                    print(not entry.get('serial_number'))
                    print(entry.get('email'))
                    print(entry.get('serial_number'))
                    print("==============")

            close_ldplayer(entry["email"])
            await asyncio.sleep(2)  # Đợi 2 giây 
                

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


# Function để kiểm tra thiết bị LDPlayer đã online chưa
async def wait_for_device_online():
    while True:
        # Kiểm tra danh sách thiết bị qua adb
        result = os.popen('adb devices').read()
        lines = result.splitlines()
    
        # Tạo mảng chứa tên các thiết bị
        devices = [line.split()[0] for line in lines if 'device' in line and not line.startswith('List')]
    
        if devices:
            print("Đã khởi động thiết bị")
            return devices[0]
        else:
            print("Đang khởi động thiết bị...")
            await asyncio.sleep(2)  # Đợi 2 giây rồi kiểm tra lại
    
async def main():
    await process_email_file()
    # run_devices_multithreaded()

# Chạy hàm chính
if __name__ == "__main__":
    asyncio.run(main())
