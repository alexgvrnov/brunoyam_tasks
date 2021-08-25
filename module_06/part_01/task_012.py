import threading
from time import sleep
from datetime import datetime


def get_thread(thread_name):

    sleep(1)
    print(thread_name)


def main_task(parallel):

    threads = [threading.Thread(target=get_thread, args=('Thread: '+str(i),)) for i in range(5)]

    start_time = datetime.now()

    for t in threads:

        t.start()

        if not parallel:
            t.join()

    while threading.active_count() > 1 and parallel:

        pass

    print('Execution time: ', (datetime.now() - start_time))


main_task(False)
main_task(True)
