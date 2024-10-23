import json
import os

# Bước 1: Đọc nội dung file
with open('./email.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Bước 2: Tạo danh sách chứa các object JSON
json_array = []

for line in lines:
    # Xóa ký tự xuống dòng và khoảng trắng
    line = line.strip()

    # Tách dòng thành các phần tử bằng dấu '|'
    parts = line.split('|')

    # Tạo đối tượng JSON từ các phần tử, gán recovery_mail là None nếu không có phần tử thứ 3
    json_obj = {
        "email": parts[0] if len(parts) > 0 else None,
        "password": parts[1] if len(parts) > 1 else None,
        "recovery_mail": parts[2] if len(parts) > 2 else None,
    }

    # Thêm object vào danh sách
    json_array.append(json_obj)

# Bước 3: Chuyển danh sách thành chuỗi JSON
json_output = json.dumps(json_array, indent=4)

# In chuỗi JSON ra màn hình hoặc ghi vào file
# print(json_output)

# Ghi vào file JSON nếu cần
with open('output.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_output)

with open('output.json', 'r', encoding='utf-8') as json_data:
    jsonData = json.load(json_data)

unique_emails = set()

# Lặp qua từng email và thêm vào tập hợp nếu chưa tồn tại
for entry in jsonData:
    email = entry["email"]
    unique_emails.add(email)

# Thực hiện lệnh cho từng email duy nhất
for email in unique_emails:
    command = f'D:\LDPlayer\LDPlayer9\LDConsole.exe copy --name {email} --from 0'
    print(f"Running command: {command}")
    os.system(command)


# đọc file JSON nếu cần


print("=================")
print(jsonData)
print("=================")

