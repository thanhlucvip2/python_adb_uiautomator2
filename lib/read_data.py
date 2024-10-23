import json

# Bước 1: Đọc nội dung file
with open('duong_dan_toi_file.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Bước 2: Tạo danh sách chứa các object JSON
json_array = []

for line in lines:
    # Xóa ký tự xuống dòng và khoảng trắng
    line = line.strip()
    
    # Tách dòng thành các phần tử bằng dấu '|'
    parts = line.split('|')
    
    # Kiểm tra xem có đúng 3 phần tử không
    if len(parts) == 3:
        # Tạo đối tượng JSON từ các phần tử
        json_obj = {
            "devices": parts[0],
            "email": parts[1],
            "proxy": parts[2]
        }
        # Thêm object vào danh sách
        json_array.append(json_obj)

# Bước 3: Chuyển danh sách thành chuỗi JSON
json_output = json.dumps(json_array, indent=4)

# In chuỗi JSON ra màn hình hoặc ghi vào file
print(json_output)

# Ghi vào file JSON nếu cần
with open('output.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_output)
