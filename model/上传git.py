import pyautogui
import keyboard
from datetime import datetime
import subprocess

LOCAL_GIT_REPO_PATH = r'E:\0Code\Algorithm'

def take_screenshot():
    screenshot = pyautogui.screenshot()
    filename = f"screenshot{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
    screenshot.save(filename)
    return filename

def commit_and_push_to_git(filename):
    try:
        subprocess.run(['git', 'add', '.'], cwd=LOCAL_GIT_REPO_PATH, check=True)
        subprocess.run(['git', 'commit', '-m', f'Added {filename}'], cwd=LOCAL_GIT_REPO_PATH, check=True)
        subprocess.run(['git', 'push'], cwd=LOCAL_GIT_REPO_PATH, check=True)
        print(f'Successfully committed and pushed to Git repository')
    except subprocess.CalledProcessError as e:
        print(f'Failed to commit and push to Git repository: {e}')

def on_hotkey_pressed():
    filename = take_screenshot()
    commit_and_push_to_git(filename)

keyboard.add_hotkey('f9', on_hotkey_pressed)

print("Press F9 to take screenshot and upload to Git repository")
keyboard.wait('esc')
