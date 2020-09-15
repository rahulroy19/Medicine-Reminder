from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
import requests
import json
import schedule
import time
from threading import *
# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'USER'})

def add(request):
    val1=request.GET['n']
    val2=request.GET['x']
    val3=request.GET['y']
    val4=request.GET['t']
    val5=request.GET['h']
    val6=request.GET['m']
    

    fin=val1
    pin=val4
    hr=val5
    min=val6



   


    def send_sms(number, message):
        url = 'https://www.fast2sms.com/dev/bulk'
        params = {
            'authorization': '1taq5MlrLehCwz08AFsE63kGmZ49QBN7YcuIXoxvVTfSnKOgUD8i0132VlCQX5zHPsqhTZMaGkvBJe7t',
            'sender_id': 'FSTSMS',
            'message': message,
            'language': 'english',
            'route': 'p',
            'numbers': number
        }
        response = requests.get(url, params=params)
        dic = response.json()
        print(dic)
        return dic.get('return')

    num=val3
    mes="HELLO "+val1+"its time to take your medicine "+val2
    tot=hr+":"+min
    #new=send_sms(num,mes)
    schedule.every().day.at(tot).do(send_sms,num,mes)

    while True:
        schedule.run_pending()
        time.sleep(1)
        messages.success(request,'your alert has been created')
        #return render(request,'result.html',{'result':fin})
  
            

    #send_sms(num,mes)
   
    

    
    return render(request,'result.html',{'result':fin})