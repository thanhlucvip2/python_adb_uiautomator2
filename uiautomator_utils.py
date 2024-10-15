import uiautomator2 as u2
import time

def interact_with_device(device):
    """
    Kết nối và tương tác với thiết bị qua uiautomator2.
    """
    try:
        print(f"Connecting to device: {device}")
        d = u2.connect(device)
        clear_all_page(d)

        print(f"Interacting with device: {device}")
        time.sleep(2)
        
        d(description="Thư mục: System Apps").click()
        time.sleep(1)
        d(text="Cửa hàng Play").click()
        time.sleep(2)

        print(f"Device {device} info: {d.info}")
    
    except Exception as e:
        print(f"Error interacting with device {device}: {e}")

def clear_all_page(d):
    d.press('recent')
    time.sleep(2)
    if d(resourceId="com.android.systemui:id/button").exists :
        d(resourceId="com.android.systemui:id/button").click()
    else:
        d.press('home')
