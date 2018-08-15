import socket
import bs4
import requests
import pandas as pd
import datetime
import json
#from .import views
from urllib.parse import urlparse as parse

def domain_to_ip(url):

   # url = 'www.stackoverflow.com/questions/43469412/convert-html-source-code-to-json-object'

    if (url.find ( '//www.' , 0 , 15 ) >= 0) :

        url1 = parse ( url )
        domain_ip = socket.gethostbyname ( url1.netloc )
        domain_name_temp = url1.netloc
        domain_name_list = domain_name_temp.split ( '.' , 1 )
        domain_name = domain_name_list [ 1 ]
        html_page = requests.get ( url )

    elif (url.find ( '//' , 0 , 15 ) >= 0) :

        url1 = parse ( url )
        domain_ip = socket.gethostbyname ( url1.netloc )
        domain_name = url1.netloc
        html_page = requests.get ( url )

    elif (url.find ( 'www.' , 0 , 4 ) >= 0) :

        url_temp = url.split ( '.' , 1 )
        url = 'http://' + url
        url1 = parse ( url )
        domain_ip = socket.gethostbyname ( url1.netloc )
        domain_name_temp = url1.netloc
        domain_name_list = domain_name_temp.split ( '.' , 1 )
        domain_name = domain_name_list [ 1 ]
        html_page = requests.get ( url )

    else :

        url = 'http://' + url
        url1 = parse ( url )
        domain_ip = socket.gethostbyname ( url1.netloc )
        domain_name = url1.netloc
        html_page = requests.get ( url )

    return {"url":url, "domain_ip":domain_ip, "domain_name":domain_name}
