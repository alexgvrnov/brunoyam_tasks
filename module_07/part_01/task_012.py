import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def lists_update(rates_list, dates, rates):

    for i in range(3, len(rates_list), 3):

        dates.append(str(rates_list[i])[6: -5])
        rates.append(float(str(rates_list[i+1])[4: -5]))

    dates.reverse()
    rates.reverse()


def main_task():

    request = requests.get('http://mfd.ru/currency/?currency=USD')

    soup = BeautifulSoup(request.text, 'html.parser')

    rates = soup.find('table', {'class': 'mfd-table mfd-currency-table'})

    rates_list = rates.find_all('td')

    dates = []
    rates = []

    lists_update(rates_list, dates, rates)

    figure = plt.figure()
    axis = figure.add_subplot()

    axis.xaxis.set_major_locator(MaxNLocator(4))
    axis.grid(True)

    plt.title('RUB / USD rate', fontsize=15)
    plt.xlabel('Date', fontsize=12, color='blue')
    plt.ylabel('Rate', fontsize=12, color='blue')
    plt.plot(dates, rates)
    plt.show()


main_task()
