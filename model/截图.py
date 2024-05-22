import pyautogui
import paramiko
import keyboard
from io import BytesIO
import time
from PIL import Image

# 远程服务器信息
HOST = '62.234.58.121'
USERNAME = 'root'
PASSWORD = 'wsh520Lihui@'
PORT = 22
REMOTE_PATH = '/usr/local/data/'

# 捕捉屏幕截图并保存为文件
def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    print("Screenshot saved as screenshot.png")
    return screenshot

# 上传文件到远程服务器
def upload_to_server(image, filename):
    # 将图像转换为字节流
    img_byte_arr = BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # 连接到远程服务器并上传文件
    transport = paramiko.Transport((HOST, PORT))
    transport.connect(username=USERNAME, password=PASSWORD)
    sftp = paramiko.SFTPClient.from_transport(transport)
    
    try:
        with BytesIO(img_byte_arr) as fl:
            sftp.putfo(fl, REMOTE_PATH + filename)
        print(f'File {filename} uploaded successfully to {REMOTE_PATH}')
    except Exception as e:
        print(f'Failed to upload file: {e}')
    finally:
        sftp.close()
        transport.close()

# 定义快捷键处理函数
def on_hotkey_pressed():
    # 捕捉屏幕截图
    image = take_screenshot()
    
    # 获取当前时间戳
    timestamp = int(time.time())
    filename = f"screenshot_{timestamp}.png"

    # 上传截图到远程服务器
    upload_to_server(image, filename)

# 监听快捷键
keyboard.add_hotkey('ctrl+shift+s', on_hotkey_pressed)

print("Press Ctrl+Shift+S to take a screenshot and upload it to the server.")
keyboard.wait('esc')  # 按下 'esc' 键退出程序
