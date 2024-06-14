import pandas as pd
import requests


def extractDataFromHtml():
    html = requests.get("https://en.tutiempo.net/climate/03-2013/ws-432950.html").content
    df_list = pd.read_html(html)
    df = df_list[-1]
    print(df)
    df.to_csv('my data.csv')
