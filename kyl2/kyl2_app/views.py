from django.http import HttpResponse
from rest_framework.decorators import api_view
import requests
import time

@api_view(['POST'])
def game(request):
    num = request.data.get("num")
    msg = ['kyl2', 'get', str(num) , '>']
    for s in str(num):
        if s == '3' or s == '6' or s == '9':
            msg.append("JJAK")
    print(" ".join(msg))
    data = {'num': num+1}        
    requests.post('http://kyl3:8083/api/game',json=data, verify=False)
    time.sleep(2)
    return HttpResponse(" ")