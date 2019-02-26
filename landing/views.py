from django.shortcuts import render

def mostrar_index(request):
    nome = 'Enrrike'
    lista_compras = ['arroz', 'feijão', 'açai']
    return render(request, 'index.html', {'item' : nome, 'lista' : lista_compras})
