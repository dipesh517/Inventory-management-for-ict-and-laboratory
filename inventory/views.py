from django.shortcuts import render, redirect

# Create your views here.


def dashboardView(request):
    return render(request, 'inventory/index.html')


def loginView(request):
    return render(request, 'inventory/login.html')


def tableICTView(request):
    return render(request, 'inventory/tableICT.html')


def tableLABView(request):
    return render(request, 'inventory/tableLAB.html')
