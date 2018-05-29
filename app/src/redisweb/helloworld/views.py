from django.shortcuts import render
from django.http import HttpResponse

import redis


def hello(request):
    response = redis.__file__
    response = response + "<br>"
    r = redis.Redis(host='redis-master', port=6379, db=0)
    info = r.info()
    response = response + 'Set Hi <br>'
    r.set('Hi', 'HelloWorld-APP')
    response = response + ('Get Hi: %s <br>' % r.get('Hi'))
    response = response + 'Redis Info: <br>'
    response = response + 'Key: Info Value'

    for key in info:
        response = response + ("%s: %s <br>" % (key, info[key]))
    return HttpResponse(response)
