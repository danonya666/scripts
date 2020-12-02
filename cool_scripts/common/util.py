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
