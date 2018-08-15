from django import forms


class HomeForm ( forms.Form ) :
    post = forms.CharField ( label = 'Please Enter Domain Name Below:' )
    # csv = forms.FileField()


class HomeForm1 ( forms.Form ) :
    # post = forms.CharField()
    csv = forms.FileField (label = 'Please Upload a CSV File:')
