from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest):
    return HttpResponse('<p>this app is owned by hisakawa1251@gmail.com</p>')
