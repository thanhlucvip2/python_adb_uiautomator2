import requests

def check_proxy_ip(proxy):
    url = "https://api64.ipify.org/?format=json"  # Dịch vụ kiểm tra IP
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}",
    }

    try:
        response = requests.get(url, proxies=proxies, timeout=5)
        if response.status_code == 200:
            ip_info = response.json()
            return ip_info.get('ip')
        else:
            print( f"Lỗi HTTP {response.status_code}")
            return False
    except requests.exceptions.ProxyError:
        print("Lỗi proxy: Không thể kết nối tới proxy.")
        return False
    except requests.exceptions.ConnectTimeout:
        print("Lỗi: Kết nối tới proxy bị timeout.")
        return False
    except Exception as e:
        print(f"Lỗi khác: {str(e)}")
        return False
