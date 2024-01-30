from django.shortcuts import render
from django.http import HttpResponse

def calculadora(request):
    return render(request, 'calculadora_app/calculadora.html')

def calcular(request):
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operacao = request.POST.get('operacao')

        if operacao == 'soma':
            resultado = num1 + num2
        elif operacao == 'subtracao':
            resultado = num1 - num2
        elif operacao == 'multiplicacao':
            resultado = num1 * num2
        elif operacao == 'divisao':
            if num2 != 0:
                resultado = num1 / num2
            else:
                return HttpResponse('Erro: divisão por zero não é permitida.')
        else:
            return HttpResponse('Operação inválida.')

        return render(request, 'calculadora_app/calculadora.html', {'resultado': resultado})

    return HttpResponse('Método não permitido.')

