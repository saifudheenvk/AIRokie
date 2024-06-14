# saifu


import time

from Functions.DataFromHtml import extractDataFromHtml
from Functions.get_html import getDataHtml
from Functions.scrapping_with_soup import usingBeautifulSoup


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # with pandas html download
    # start_time = time.time()
    # getDataHtml()
    # end_time = time.time()
    # print('total time taken={}'.format(start_time - end_time))
    # extractDataFromHtml()

    # with soup
    usingBeautifulSoup()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
