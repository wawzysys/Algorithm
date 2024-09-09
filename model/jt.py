import pyautogui
import paramiko
import keyboard
from io import BytesIO
import time
from PIL import Image
from datetime import datetime
HOST = '47.121.221.247'
USERNAME = 'newuser'
PASSWORD = '1'
PORT = 22
REMOTE_PATH = '/home/newuser/jie/'
def take_screenshot():
    screenshot = pyautogui.screenshot()
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
        print(f'true')
    except Exception as e:
        print(f'false: {e}')
    finally:
        sftp.close()
        transport.close()
def on_hotkey_pressed():
    image = take_screenshot()
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"screenshot_{timestamp}.png"
    upload_to_server(image, filename)
keyboard.add_hotkey('f9', on_hotkey_pressed)

# print("Press F9")
keyboard.wait('esc')  
