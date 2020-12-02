import shutil
from time import sleep
import platform
import subprocess


def show_warning(notification_text, title):
    system = platform.system()
    cmd = ""
    if system == "Darwin":
        cmd = f"""osascript -e 'display notification "{notification_text}" with title "{title}"'"""
    if system == "Linux":
        cmd = f'notify-send "{notification_text}"'
    results = subprocess.run(
        cmd, shell=True, universal_newlines=True, check=True)
    # print(results.stdout)


normal_free = 264207257600

low_free = normal_free / 6  # around 40 GB

sleepy = 60

def almost_full():
    # if there is less than low_free space on disk left
    if shutil.disk_usage("/").free < low_free:
        show_warning("Disk space is running low!", "Your python util")
        sleepy = 15


if __name__ == "__main__":
    show_warning('almost_full.py starteddddd', 'almost_full.py')
    while True:
        try:
            almost_full()
            sleep(sleepy)
        except Exception:
            show_warning(f'almost_full.py exception', 'almost_full.py')
