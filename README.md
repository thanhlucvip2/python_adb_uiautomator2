# Hướng dẫn Khởi động và Quản lý LDPlayer

## Khởi động LDPlayer

Sử dụng lệnh dưới đây để khởi động các phiên bản của LDPlayer:

- Khởi động LDPlayer đầu tiên:
  ```bash
  LDConsole.exe launch --index 0
  ```

- Khởi động LDPlayer thứ hai:
  ```bash
  LDConsole.exe launch --index 1
  ```

- Khởi động LDPlayer theo tên:
  ```bash
  LDConsole.exe launch --name doanthanhluc91bvh@gmail.com
  ```

## Danh sách thiết bị

Để xem danh sách các thiết bị đang hoạt động, sử dụng lệnh:

```bash
LDConsole.exe list
```

## Sao chép thiết bị

Bạn có thể sao chép thiết bị bằng các lệnh sau:

- Sao chép thiết bị mới từ thiết bị đầu tiên:
  ```bash
  LDConsole.exe copy --from 0
  ```

- Sao chép thiết bị và đặt tên cho nó:
  ```bash
  LDConsole.exe copy --name test_12 --from 0
  ```

- Sao chép thiết bị với tên cụ thể:
  ```bash
  LDConsole.exe copy --name doanthanhluc91bvh@gmail.com --from 0
  ```
  
- Update số điện thoại
  ```bash
  LDConsole.exe modify --name doanthanhluc91bvh@gmail.com --pnumber 11111111
  ```

## Đổi tên thiết bị

Để đổi tên thiết bị, sử dụng lệnh sau:

```bash
LDConsole.exe rename --index 1 --title "new-name"
```

---

**Lưu ý:** Thay thế `0`, `1`, và tên thiết bị theo nhu cầu của bạn.



## Cài đặt weditor:
```bash
  pip install setuptools==67.5.1
  ```
```bash
  pip install weditor
  ```

## cấp quyền cho vs code:
```bash 
Set-ExecutionPolicy Unrestricted
 ```