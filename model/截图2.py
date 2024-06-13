import pyautogui
import paramiko
import keyboard
from io import BytesIO
import time
from PIL import Image
from datetime import datetime

# HOST = '62.234.58.121'
# USERNAME = 'root'
# PASSWORD = 'wsh520Lihui@'
# PORT = 22
# REMOTE_PATH = '/usr/local/wzzz/'
HOST = '8.147.235.221'
USERNAME = 'root'
PASSWORD = '123qwe!QWE'
PORT = 22
REMOTE_PATH = '/usr/local/jietu/'
# Host = 8.147.235.221
#   HostName = 8.147.235.221
#   User = root
#   Port = 22
#   # password:123qwe!QWE
def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save(f"screenshot{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png")
    # print("Screenshot saved as screenshot.png")
    return screenshot

def upload_to_server(image, filename):

    img_byte_arr = BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    transport = paramiko.Transport((HOST, PORT))
    transport.connect(username=USERNAME, password=PASSWORD)
    sftp = paramiko.SFTPClient.from_transport(transport)
    
    try:
        with BytesIO(img_byte_arr) as fl:
            sftp.putfo(fl, REMOTE_PATH + filename)
        print(f'success')
    except Exception as e:
        print(f'Failed to upload file: {e}')
    finally:
        sftp.close()
        transport.close()
def on_hotkey_pressed():
    image = take_screenshot()
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"screenshot_{timestamp}.png"
    upload_to_server(image, filename)
keyboard.add_hotkey('f9', on_hotkey_pressed)

print("Press F9")
keyboard.wait('esc')  
