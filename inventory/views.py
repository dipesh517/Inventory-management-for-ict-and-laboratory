from django.shortcuts import render, redirect
from .models import Room
from .models import Floor
from .models import Computer
from .models import Laptop
from .models import NetworkSwitch
from .models import Printer
from .models import AdditionalItem
# Create your views here.

def dashboardView(request):
    return render(request, 'inventory/index.html')


def loginView(request):
    return render(request, 'inventory/login.html')


def tableICTView(request):
    return render(request, 'inventory/tableICT.html')


def tableLABView(request):
    return render(request, 'inventory/tableLAB.html')

def testView(request,floorNo,roomNo):
    computerObj = Computer.objects.none()
    laptopObj = Laptop.objects.none()
    networkObj = NetworkSwitch.objects.none()
    printerObj = Printer.objects.none()
    additionalObj = AdditionalItem.objects.none()
    floorObj=Floor.objects.all()
    objCount = []
    if (floorNo==500 and roomNo==500):
        roomObj = Room.objects.all()
        computerObj=Computer.objects.all()
        laptopObj = Laptop.objects.all()
        networkObj = NetworkSwitch.objects.all()
        printerObj = Printer.objects.all()
        additionalObj = AdditionalItem.objects.all()

    elif (floorNo!=500 and roomNo==500):
        roomObj = Room.objects.filter(floor=floorNo)
        for obj in roomObj:
            computerObj |= Computer.objects.filter(room=obj.room_no)
            laptopObj |= Laptop.objects.filter(room=obj.room_no)
            networkObj |= NetworkSwitch.objects.filter(room=obj.room_no)
            printerObj |= Printer.objects.filter(room=obj.room_no)
            additionalObj |= AdditionalItem.objects.filter(room=obj.room_no)
    else:
        room = Room.objects.get(room_no=roomNo)
        floorNo = room.floor
        roomObj = Room.objects.filter(floor=floorNo)
        computerObj |= Computer.objects.filter(room=room.room_no)
        laptopObj |= Laptop.objects.filter(room=room.room_no)
        networkObj |= NetworkSwitch.objects.filter(room=room.room_no)
        printerObj |= Printer.objects.filter(room__exact=room.room_no)
        additionalObj |= AdditionalItem.objects.filter(room=room.room_no)
    objCount = [computerObj.count(), laptopObj.count(), networkObj.count(), printerObj.count(), additionalObj.count()]
    context = {'roomObj': roomObj, 'floorObj': floorObj, 'computerObj': computerObj, 'laptopObj': laptopObj, 'networkObj': networkObj, 'printerObj': printerObj, 'additionalObj': additionalObj, 'objCount': objCount}
    return render(request, 'inventory/searchICT.html', context)


def dashSearchView(request, floorNo, roomNo):
    computerObj = Computer.objects.none()
    laptopObj = Laptop.objects.none()
    networkObj = NetworkSwitch.objects.none()
    printerObj = Printer.objects.none()
    additionalObj = AdditionalItem.objects.none()
    floorObj=Floor.objects.all()
    objCount = []
    if (floorNo==500 and roomNo==500):
        roomObj = Room.objects.all()
        computerObj=Computer.objects.filter(status='OO')
        laptopObj = Laptop.objects.filter(status='OO')
        networkObj = NetworkSwitch.objects.filter(status='OO')
        printerObj = Printer.objects.filter(status='OO')
        additionalObj = AdditionalItem.objects.filter(status='OO')

    elif (floorNo!=500 and roomNo==500):
        roomObj = Room.objects.filter(floor=floorNo)
        for obj in roomObj:
            computerObj |= Computer.objects.filter(room=obj.room_no).filter(status='OO')
            laptopObj |= Laptop.objects.filter(room=obj.room_no).filter(status='OO')
            networkObj |= NetworkSwitch.objects.filter(room=obj.room_no).filter(status='OO')
            printerObj |= Printer.objects.filter(room=obj.room_no).filter(status='OO')
            additionalObj |= AdditionalItem.objects.filter(room=obj.room_no).filter(status='OO')
    else:
        room = Room.objects.get(room_no=roomNo)
        floorNo = room.floor
        roomObj = Room.objects.filter(floor=floorNo)
        computerObj |= Computer.objects.filter(room=room.room_no).filter(status='OO')
        laptopObj |= Laptop.objects.filter(room=room.room_no).filter(status='OO')
        networkObj |= NetworkSwitch.objects.filter(room=room.room_no).filter(status='OO')
        printerObj |= Printer.objects.filter(room__exact=room.room_no).filter(status='OO')
        additionalObj |= AdditionalItem.objects.filter(room=room.room_no).filter(status='OO')
    objCount = [computerObj.count(), laptopObj.count(), networkObj.count(), printerObj.count(), additionalObj.count()]
    context = {'roomObj': roomObj, 'floorObj': floorObj, 'computerObj': computerObj, 'laptopObj': laptopObj, 'networkObj': networkObj, 'printerObj': printerObj, 'additionalObj': additionalObj, 'objCount': objCount}
    return render(request, 'inventory/dash_search.html', context)


def dashSearch2View(request, floorNo, roomNo):
    computerObj = Computer.objects.none()
    laptopObj = Laptop.objects.none()
    networkObj = NetworkSwitch.objects.none()
    printerObj = Printer.objects.none()
    additionalObj = AdditionalItem.objects.none()
    floorObj=Floor.objects.all()
    objCount = []
    if (floorNo==500 and roomNo==500):
        roomObj = Room.objects.all()
        computerObj=Computer.objects.filter(status='IM')
        laptopObj = Laptop.objects.filter(status='IM')
        networkObj = NetworkSwitch.objects.filter(status='IM')
        printerObj = Printer.objects.filter(status='IM')
        additionalObj = AdditionalItem.objects.filter(status='IM')

    elif (floorNo!=500 and roomNo==500):
        roomObj = Room.objects.filter(floor=floorNo)
        for obj in roomObj:
            computerObj |= Computer.objects.filter(room=obj.room_no).filter(status='IM')
            laptopObj |= Laptop.objects.filter(room=obj.room_no).filter(status='IM')
            networkObj |= NetworkSwitch.objects.filter(room=obj.room_no).filter(status='IM')
            printerObj |= Printer.objects.filter(room=obj.room_no).filter(status='IM')
            additionalObj |= AdditionalItem.objects.filter(room=obj.room_no).filter(status='IM')
    else:
        room = Room.objects.get(room_no=roomNo)
        floorNo = room.floor
        roomObj = Room.objects.filter(floor=floorNo)
        computerObj |= Computer.objects.filter(room=room.room_no).filter(status='IM')
        laptopObj |= Laptop.objects.filter(room=room.room_no).filter(status='IM')
        networkObj |= NetworkSwitch.objects.filter(room=room.room_no).filter(status='IM')
        printerObj |= Printer.objects.filter(room__exact=room.room_no).filter(status='IM')
        additionalObj |= AdditionalItem.objects.filter(room=room.room_no).filter(status='IM')
    objCount = [computerObj.count(), laptopObj.count(), networkObj.count(), printerObj.count(), additionalObj.count()]
    context = {'roomObj': roomObj, 'floorObj': floorObj, 'computerObj': computerObj, 'laptopObj': laptopObj, 'networkObj': networkObj, 'printerObj': printerObj, 'additionalObj': additionalObj, 'objCount': objCount}
    return render(request, 'inventory/dash_search2.html', context)


