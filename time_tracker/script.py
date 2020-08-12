import platform

import psutil
from datetime import datetime
import pandas as pd
from time import sleep
import os
import subprocess

SECONDS_IN_HOUR = 3600


def main():
    # the list the contain all process dictionaries
    processes = []
    for process in psutil.process_iter():
        # get all process info in one shot
        with process.oneshot():
            # get the process id
            pid = process.pid
            if pid == 0:
                # System Idle Process for Windows NT, useless to see anyways
                continue

            # get the name of the file executed
            name = process.name()
            if "firefox" in process.name():
                time = datetime.now() - datetime.fromtimestamp(process.create_time())
                if time.total_seconds() > 2 * SECONDS_IN_HOUR:
                    log_end_of_day()
                if day_is_over():
                    show_warning()
                    sleep(5)
                    process.kill()
                # print(time.total_seconds())
                # print('im brave')
                # process.kill()
                # print(
                #     f"name: {name} time: {datetime.now() - datetime.fromtimestamp(process.create_time())} status: {process.status()}")


def show_warning():
    system = platform.system()
    cmd = ""
    notification_text = "Соня, прошло 2 часа, пора выключать компухтер!"
    title = "Zzzzzz"
    if system == "Darwin":
        cmd = f"""osascript -e 'display notification "{notification_text}" with title "{title}"'"""
    if system == "Linux":
        cmd = f'notify-send "{notification_text}"'
    results = subprocess.run(
        cmd, shell=True, universal_newlines=True, check=True)
    # print(results.stdout)


def log_end_of_day():
    with open("log_file.txt", 'a') as f:
        f.write(f'{str(datetime.now().date())}\n')


def day_is_over():
    with open("log_file.txt", 'r') as f:
        lines = f.readlines()
        print(lines)
        for line in lines:
            line = line.strip('\n')
            if line == str(datetime.now().date()):
                return True
        return False


if __name__ == "__main__":
    while True:
        main()
        sleep(30)
