import pyautogui
import os
import keyboard
from io import BytesIO
from PIL import Image
from datetime import datetime
import subprocess

# Hexo博客的路径
HEXO_PATH = r'E:\0Code\blog\blog-demo'  # 替换为你Hexo博客的路径
MARKDOWN_PATH = os.path.join(HEXO_PATH, 'source', '_posts')
cnt = 0
def take_screenshot():
    global cnt
    cnt += 1
    screenshot = pyautogui.screenshot()
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # timestamp = cnt
    screenshot_path = os.path.join(MARKDOWN_PATH, 'screenshot',f"{timestamp}.png")
    screenshot.save(screenshot_path)
    return screenshot_path

def save_to_markdown(screenshot_path):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    screenshot_path = screenshot_path.replace('\\', '/')
    # screenshot_path = cnt
    markdown_filename = f'picture.md'
    markdown_filepath = os.path.join(MARKDOWN_PATH, markdown_filename)
    with open(markdown_filepath, 'a') as f:#'a'是追加，'w'是覆盖
        f.write(f"### Screenshot taken on {timestamp}\n\n")
        f.write(f"![Screenshot]({screenshot_path})\n")
    return markdown_filepath

def run_hexo_commands():
    commands = ['hexo clean', 'hexo generate', 'hexo deploy']
    for command in commands:
        process = subprocess.run(command, cwd=HEXO_PATH, shell=True)
        if process.returncode != 0:
            print(f"Command '{command}' failed with return code {process.returncode}")
            break
def on_hotkey_pressed():
    screenshot_path = take_screenshot()
    markdown_filepath = save_to_markdown(screenshot_path)
    run_hexo_commands()
    print(f"Screenshot saved and markdown created at {markdown_filepath}")
keyboard.add_hotkey('f9', on_hotkey_pressed)
print("Press F9 to take a screenshot and update your Hexo blog")
keyboard.wait('esc')
