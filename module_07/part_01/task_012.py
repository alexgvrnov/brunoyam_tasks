import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def lists_update(rates_list):

    rates = [float(str(rates_list[i-1])[4: -5]) for i in range(len(rates_list)-1, 3, -3)]
    dates = [str(rates_list[i-2])[6: -5] for i in range(len(rates_list)-1, 3, -3)]

    return dates, rates


def main_task():

    request = requests.get('http://mfd.ru/currency/?currency=USD')

    soup = BeautifulSoup(request.text, 'html.parser')

    rates = soup.find('table', {'class': 'mfd-table mfd-currency-table'})

    rates_list = rates.find_all('td')

    dates, rates = lists_update(rates_list)

    fig, ax = plt.subplots()

    ax.xaxis.set_major_locator(MaxNLocator(4))
    ax.grid(True)

    ax.set_title('RUB / USD rate', fontsize=15)
    ax.set_xlabel('Date', fontsize=12, color='blue')
    ax.set_ylabel('Rate', fontsize=12, color='blue')
    ax.plot(dates, rates)

    plt.show()


main_task()
