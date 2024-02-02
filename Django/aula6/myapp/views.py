from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from .models import Pessoa

"""
def cadastro(request):
    return render(request, 'cadastro.html')


def cadastro(request):
    if request.method =='POST':
        nome = request.POST.get('nome')
        pais = request.POST.get('pais')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        print(nome)
        print(pais)
        print(estado)
        print(cidade)
        return HttpResponseRedirect('/cadastro')
    else:
        return render(request, 'tabela.html')
"""
def index(request):
    return HttpResponseRedirect('/cadastro')

def tabela(request):
    '''
    for pessoa in Pessoa.objects.all():
        print(pessoa.nome)
        print(pessoa.pais)
        print(pessoa.estado)
        print(pessoa.cidade)
    '''
    return render(request, 'tabela.html', {'pessoas':Pessoa.objects.raw('select * from myapp_pessoa')})

def cadastro(request):
    if request.method =='POST':
        nome = request.POST.get('nome')
        pais = request.POST.get('pais')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        pessoa = Pessoa()
        pessoa.nome = nome
        pessoa.pais = pais
        pessoa.estado = estado
        pessoa.cidade = cidade
        pessoa.save()
        return HttpResponseRedirect('/tabela')
    
    elif request.method =='GET':
        return render(request, 'cadastro.html')
    
    else:
        return HttpResponseBadRequest()