import csv

import requests
from lxml import html
import math
base_url = 'https://www.op.gg/ranking/ladder/'


r = requests.get(base_url)
tree = html.fromstring(r.text)
xpath_total_users = '''//div[@class="ranking-pagination__desc"]/span[2]/text()'''
total_users = tree.xpath(xpath_total_users)[0]
total_users = int(total_users.replace(',', ''))
print(total_users)

users_per_page = 100 # displays 100 user per page
total_page = math.ceil(total_users / users_per_page)
print(total_page)


total_names = []
for i in range(total_page, 1, -1):
    url = base_url + "page=%d" % i

    r = requests.get(url)
    tree = html.fromstring(r.text)
    names = tree.xpath('''//tr[@class="ranking-table__row "]/td[2]//span/text()''')
    total_names.extend(names)

    if len(total_names) > 5000:
        break

print(total_names)

with open('usernames.csv', 'w', newline='') as file_usernames:
    wr = csv.writer(file_usernames, quoting=csv.QUOTE_ALL)
    wr.writerow(total_names)