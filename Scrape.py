
# coding: utf-8

# In[ ]:


#code for scrape datas from given url
import requests
from bs4 import BeautifulSoup
import csv
import lxml
import re


def open_csv(filename, d='\t'):
    data = []
    with open(filename, encoding='utf-8') as tsvin:
        f_reader = csv.reader(tsvin, delimiter=d)
        for line in f_reader:
            data.append(line)
    return data


def write_csv(filename, data_sample):
    example = csv.writer(open(filename, 'w', encoding='utf-8'), dialect='excel')
    for i in range(0, len(data_sample)):
        example.writerows(data_sample[i])


def des_scrap(url):
    itm_nm = []
    sku_d = []
    price_d = []
    desc_d = []
    item_imgs = []
    response = requests.get(url, timeout=20)
    data = response.text
    soup = BeautifulSoup(data, 'lxml')
    
    itm_data = soup.find_all('h1', {'class' : 'eyTitle'})
    for d in itm_data:
        itm_nm.append(d.text)
    
    sku_data = soup.find_all('div', {'class': 'item-code'})
    for s in sku_data:
        sku_d.append(s.text)
        
    price_data = soup.find_all('span',{'class':'item-sale-price-color'})
    for t in price_data:
        price_d.append(t.text)
    
    desc_data = soup.find_all('div',{'itemprop':'description'})
    for d in desc_data:
        desc_d.append(d.text)
        
    img_data = soup.find_all('img',{'id':'SwitchThisImage'})
    for img in img_data:
        item_imgs.append(img['src'])

    return url, itm_nm[0], sku_d[0], price_d[0], desc_d[0],item_imgs


def cr4(st, end, lst):
    nw_lst = []
    o_lst = lst[st:end]
    for i in range(0, len(o_lst)):
        url_vl = o_lst[i]
        des = des_scrap(url_vl)
        nw_lst.append(des)
    return nw_lst


list_url = [#your_url
            ]

des_list = []
inp_taken = int(len(list_url))
scrap_dict = {}
for cor in range(0, inp_taken + 1):
    key = cor
    value = int(cor * (len(list_url) / inp_taken))
    scrap_dict[key] = value
    print(scrap_dict)
cr = {}
for co in range(0, len(scrap_dict)):
    key = co
    if key >= len(scrap_dict) - 1:
        break
    val = cr4(scrap_dict[key], scrap_dict[key + 1], list_url)
    cr[key] = val

for key in cr:
    des_list.append(cr[key])

write_csv("C:/Users/pramod/Desktop/scan/GBD/GG/ggscrape2.csv", des_list)
print("done")

