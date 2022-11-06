from django.http import HttpResponse
from rest_framework.decorators import api_view
import requests
import time


@api_view(['GET'])
def start(request): 
    r = requests.post('http://localhost:8081/api/game', json={"num": 1})
    time.sleep(2)
    return HttpResponse(r.content)

@api_view(['POST'])
def game(request):
    num = request.data.get("num")
    msg = ['get', str(num) , '>']
    for s in str(num):
        if s == '3' or s == '6' or s == '9':
            msg.append("JJAK")
    time.sleep(2)
    print(" ".join(msg))
    requests.post('http://kyl2:8082/api/game',json={'num': num+1}, verify=False)
    return HttpResponse(" ")
