import threading
import requests
from datetime import datetime


def get_html(link):

    request = requests.get(link)
    print(link, len(request.text))


def main_task(parallel):

    links = ['https://yandex.ru', 'https://rambler.ru', 'https://rbc.ru', 'https://gazeta.ru', 'https://finanz.ru']

    threads = [threading.Thread(target=get_html, args=(link,)) for link in links]

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
