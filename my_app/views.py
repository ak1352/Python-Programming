from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import HomeForm , HomeForm1

from .domain_to_ip import domain_to_ip
from .csv_to_domain_ip import csv_to_domain_ip
import pandas as pd
import requests
import datetime
import json
from urllib.parse import urlparse as parse
import socket
from .import scrapping_text
from .import content_cat_api


class HomeView ( TemplateView ) :
    template_name = 'my_app/index.html'

    def get ( self , request ) :
        form = HomeForm ()
        return render ( request , self.template_name , { 'form' : form } )

    def post ( self , request ) :
        form = HomeForm ( request.POST )
        if form.is_valid () :
            text = form.cleaned_data [ 'post' ]
            # myfile = request.FILES['csv']
            # csv_response = csv_to_domain_ip(myfile)
            answer = domain_to_ip ( text )
            form = HomeForm ()
            # khobsorti
            domain_Name = answer['domain_name']
            IP_Name =answer [ 'domain_ip' ]
            website_text = scrapping_text.scrapping_text(answer['url'])
            content_category = content_cat_api.content_cat_api(website_text)

        args = { 'form' : form , 'text' : IP_Name , "text1" : domain_Name , "content_cat":content_category}
        return render ( request , self.template_name , args )

    #########################


class FormView ( TemplateView ) :
    template_name = 'my_app/formm.html'

    def get ( self , request ) :
        form = HomeForm1 ()
        return render ( request , self.template_name , { 'form' : form } )

    def post ( self , request ) :
        form = HomeForm1 ( request.POST , request.FILES )
        if form.is_valid () :
            # text = form.cleaned_data['post']
            myfile = request.FILES [ 'csv' ]
            csv_response = csv_to_domain_ip ( myfile )
            # answer = domain_to_ip(text)
            form = HomeForm1 ()
            # khobsorti
            # domain_Name = 'Domain Name is ' + text
            # IP_Name = 'IP is ' + answer['domain_ip']

        args1 = { 'form' : form , 'csv_data' : myfile , 'csv_response' : csv_response }
        return render ( request , self.template_name , args1 )


class Main_page ( TemplateView ) :
    template_name = 'my_app/Home.html'


class Ip_to_Dom ( TemplateView ) :
    template_name = 'my_app/ip_to_dom.html'
