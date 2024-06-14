import sys
import pandas as pd
import requests
import os


def getDataHtml():
    for year in range(2011, 2017):
        for month in range(1, 13):
            if month < 10:
                url = 'https://en.tutiempo.net/climate/0{}-{}/ws-432950.html'.format(month, year)
            else:
                url = 'https://en.tutiempo.net/climate/{}-{}/ws-432950.html'.format(month, year)
            # texts = requests.get(url)
            html = requests.get(url).content
            df_list = pd.read_html(html)
            df = df_list[-1]
            # text_utf = texts.text.encode("utf=8")

            if not os.path.exists("../DataCollection/CsvData/{}".format(year)):
                os.makedirs("../DataCollection/CsvData/{}".format(year))
            # with open("../DataCollection/HtmlData/{}/{}.csv".format(year, month), "wb") as output:
            #     output.write(text_utf)
            df.to_csv("../DataCollection/CsvData/{}/{}.csv".format(year, month))
        sys.stdout.flush()
