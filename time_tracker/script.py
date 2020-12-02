import psutil
from datetime import datetime
from time import sleep

from cool_scripts.common.util import show_warning

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
                    show_warning("Соня, прошло 2 часа, выключай компухтер!", "Привет")
                    sleep(5)
                    process.kill()
                # print(time.total_seconds()) print('im brave') process.kill() print( f"name: {name} time: {
                # datetime.now() - datetime.fromtimestamp(process.create_time())} status: {process.status()}")




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
