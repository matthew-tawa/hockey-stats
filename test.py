# import urllib.request
# import certifi
# import ssl

# with urllib.request.urlopen('https://www.vlib.org/', context=ssl.create_default_context(cafile=certifi.where())) as f:
#     html = f.read().decode('utf-8')

# print('hello world')





# THIS WORKS WELL TO READ AN ENTIRE WEB PAGE
# from bs4 import BeautifulSoup
# import requests as req

# web = req.get('https://www.quanthockey.com/game-logs/en/game-log.php?player=41629&season=all&st=r')
# S = BeautifulSoup(web.text, 'lxml')
# print(S.prettify())


import requests
import pandas as pd

import matplotlib.pyplot as plt

url = 'https://www.quanthockey.com/game-logs/en/game-log.php?player=41629&season=2023-24&st=r'
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1]
print(df)
# df.to_csv('my data.csv')

my_shots = df.Shots.SHOTS.values
plt.hist(my_shots, bins=max(my_shots), rwidth=0.5, align='left')
plt.show()

