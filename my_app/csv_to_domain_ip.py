import pandas as pd
import requests
import datetime
import json
from urllib.parse import urlparse as parse
import socket

def csv_to_domain_ip(url_data):

    response_str = ''
    df_urls = pd.read_csv(url_data, header=None, names=['url'])
    df_data = pd.DataFrame(columns=['domain_name', 'domain_ip', 'url', 'json_object', 'date', 'time'])

    for url in df_urls['url']:
        if (url.find('//www.', 0, 15) >= 0):

            url1 = parse(url)
            domain_ip = socket.gethostbyname(url1.netloc)
            domain_name_temp = url1.netloc
            domain_name_list = domain_name_temp.split('.', 1)
            domain_name = domain_name_list[1]
            html_page = requests.get(url)
            current_date = (str(datetime.datetime.now())).split(' ')[0]
            current_time = (str(datetime.datetime.now())).split(' ')[1].split('.', 1)[0]
            json_object = json.dumps({'url': str(url), 'uid': str(1024), 'page_content': html_page.text,
                                      'date_time': str(datetime.datetime.now())})

        elif (url.find('//', 0, 15) >= 0):

            url1 = parse(url)
            domain_ip = socket.gethostbyname(url1.netloc)
            domain_name = url1.netloc
            html_page = requests.get(url)
            current_date = (str(datetime.datetime.now())).split(' ')[0]
            current_time = (str(datetime.datetime.now())).split(' ')[1].split('.', 1)[0]

            json_object = json.dumps({'url': str(url), 'uid': str(1024), 'page_content': html_page.text,
                                      'date_time': str(datetime.datetime.now())})

        elif (url.find('www.', 0, 4) >= 0):

            url_temp = url.split('.', 1)
            url = 'http://' + url
            url1 = parse(url)
            domain_ip = socket.gethostbyname(url1.netloc)
            domain_name_temp = url1.netloc
            domain_name_list = domain_name_temp.split('.', 1)
            domain_name = domain_name_list[1]
            html_page = requests.get(url)
            current_date = (str(datetime.datetime.now())).split(' ')[0]
            current_time = (str(datetime.datetime.now())).split(' ')[1].split('.', 1)[0]

            json_object = json.dumps({'url': str(url), 'uid': str(1024), 'page_content': html_page.text,
                                      'date_time': str(datetime.datetime.now())})

        else:

            url = 'http://' + url
            url1 = parse(url)
            domain_ip = socket.gethostbyname(url1.netloc)
            domain_name = url1.netloc
            html_page = requests.get(url)
            current_date = (str(datetime.datetime.now())).split(' ')[0]
            current_time = (str(datetime.datetime.now())).split(' ')[1].split('.', 1)[0]

            json_object = json.dumps({'url': str(url), 'uid': str(1024), 'page_content': html_page.text,
                                      'date_time': str(datetime.datetime.now())})

        #print(url)
        #print(domain_ip)
        #print(domain_name)
        #print(current_date)
        #print(current_time)

        response_str = response_str + '\n' + domain_name + '\t' + domain_ip +'\n'

        df_data = df_data.append(
            {'domain_name': domain_name, 'domain_ip': domain_ip, 'url': url, 'json_object': json_object,
             'date': current_date, 'time': current_time}, ignore_index=True)



    return response_str