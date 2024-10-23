import random

# Định nghĩa các đầu số của các nhà mạng
viettel_prefixes = ['086', '096', '097', '098', '032', '033', '034', '035', '036', '037', '038', '039']
mobifone_prefixes = ['089', '090', '093', '070', '079', '077', '076', '078']
vinaphone_prefixes = ['088', '091', '094', '083', '084', '085', '081', '082']

def generate_phone_number(prefix):
    """Hàm tạo số điện thoại ngẫu nhiên với tiền tố cho trước"""
    return f"{prefix}{random.randint(1000000, 9999999)}"

# Tạo danh sách 1000 số điện thoại ngẫu nhiên
phone_numbers = []
for _ in range(1000):  # Mỗi nhà mạng lấy khoảng 333 số để tổng cộng là 1000 số
    phone_numbers.append(generate_phone_number(random.choice(viettel_prefixes)))
    phone_numbers.append(generate_phone_number(random.choice(mobifone_prefixes)))
    phone_numbers.append(generate_phone_number(random.choice(vinaphone_prefixes)))

# Ghi danh sách số điện thoại vào file
with open('phone_number.txt', 'w') as f:
    for number in phone_numbers:
        f.write(number + '\n')
