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
        roomObj = Room.objects.filter(floor__exact = floorNo)
        for obj in roomObj:
            computerObj |= Computer.objects.filter(room__exact = obj.room_no)
            laptopObj|= Laptop.objects.filter(room__exact = obj.room_no)
            networkObj|= NetworkSwitch.objects.filter(room__exact = obj.room_no)
            printerObj|= Printer.objects.filter(room__exact = obj.room_no)
            additionalObj|= AdditionalItem.objects.filter(room__exact = obj.room_no)
    else:
        room = Room.objects.get(room_no__exact = roomNo)
        floorNo = room.floor
        roomObj = Room.objects.filter(floor__exact=floorNo)
        computerObj |= Computer.objects.filter(room__exact = room.room_no)
        laptopObj |= Laptop.objects.filter(room__exact = room.room_no)
        networkObj|= NetworkSwitch.objects.filter(room__exact = room.room_no)
        printerObj|= Printer.objects.filter(room__exact = room.room_no)
        additionalObj|= AdditionalItem.objects.filter(room__exact = room.room_no)
    objCount = [computerObj.count() , laptopObj.count(), networkObj.count(), printerObj.count(), additionalObj.count()]
    context = {'roomObj':roomObj,'floorObj':floorObj,'computerObj':computerObj,'laptopObj':laptopObj,'networkObj':networkObj,'printerObj':printerObj,'additionalObj':additionalObj,'objCount':objCount}
    return render(request,'inventory/searchICT.html',context)
