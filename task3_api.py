import json

from bottle import route, run, response, post, request 

from task3 import appearance


@post('/intervals')
def index():
    res = appearance(request.json)
    return str(res)


if __name__ == '__main__':
    run(host='localhost', port=8080)
