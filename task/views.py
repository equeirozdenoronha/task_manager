from django.shortcuts import render
from django.http import HttpResponse
class Tarefa(object):
    def __init__(self, titulo=None, data=None):
        self titulo=titulo
        self data=data
    def __str__(self):
        return self.descricao, self.data
# Create your views here.
def home(request):
    return HttpResponse("<h1>Olá</h1><br><h4>Você conseguiu</h4>")
def sobre(request):
    return HttpResponse("Ezequiel Queiroz")
def tarefa(request,ano,mes,dia):
    return HttpResponse("Tarefa:"+str(ano)+"/"+str(mes)+"/"+str(dia))
