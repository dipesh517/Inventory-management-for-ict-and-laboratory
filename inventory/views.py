from django.shortcuts import render, redirect
from .models import Room
from .models import Floor
from .models import Computer
from .models import Laptop
from .models import NetworkSwitch
from .models import Printer
from .models import AdditionalItem
from .addQuantityForm import addQuantityForm
from django.contrib import messages
from .addDataForm import LaptopForm,ComputerForm,PrinterForm,AdditionalItemForm,NetworkSwitchForm,LaptopForm
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def addItemByQuantityBaseView(request):
        return render(request,'inventory/addByQuantity/addByQuantityBase.html')

def addItemByQuantityComputerView(request):
    if request.method == "POST":
        form = addQuantityForm(request.POST)
        if form.is_valid():
            for quantity in range(int(request.POST['Quantity'])):
                newObj = Computer()
                if (request.POST['Room']):
                    if Room.objects.get(room_no = int(request.POST['Room'])):
                        newObj.room= Room.objects.get(room_no = int(request.POST['Room']))

                newObj.save()
            return redirect('addByQuantityBase')
    else:
        form = addQuantityForm()
    context = {'form':form}
    return render(request,'inventory/addByQuantity/addByQuantityComputer.html',context)

def addItemByQuantityLaptopView(request):
    if request.method == "POST":
        form = addQuantityForm(request.POST)
        if form.is_valid():
            for quantity in range(int(request.POST['Quantity'])):
                newObj = Laptop()
                if (request.POST['Room']):
                    if Room.objects.get(room_no = int(request.POST['Room'])):
                        newObj.room= Room.objects.get(room_no = int(request.POST['Room']))

                newObj.save()
            return redirect('addByQuantityBase')
    else:
        form = addQuantityForm()
    context = {'form':form}
    return render(request,'inventory/addByQuantity/addByQuantityLaptop.html',context)

def addItemByQuantityNetworkSwitchView(request):
    if request.method == "POST":
        form = addQuantityForm(request.POST)
        if form.is_valid():
            for quantity in range(int(request.POST['Quantity'])):
                newObj = NetworkSwitch()
                if (request.POST['Room']):
                    if Room.objects.get(room_no = int(request.POST['Room'])):
                        newObj.room= Room.objects.get(room_no = int(request.POST['Room']))

                newObj.save()
            return redirect('addByQuantityBase')
    else:
        form = addQuantityForm()
    context = {'form':form}
    return render(request,'inventory/addByQuantity/addByQuantityNetworkSwitch.html',context)

def addItemByQuantityPrinterView(request):
    if request.method == "POST":
        form = addQuantityForm(request.POST)
        if form.is_valid():
            for quantity in range(int(request.POST['Quantity'])):
                newObj = Printer()
                if (request.POST['Room']):
                    if Room.objects.get(room_no = int(request.POST['Room'])):
                        newObj.room= Room.objects.get(room_no = int(request.POST['Room']))

                newObj.save()
            return redirect('addByQuantityBase')
    else:
        form = addQuantityForm()
    context = {'form':form}
    return render(request,'inventory/addByQuantity/addByQuantityPrinter.html',context)

def addItemByQuantityAdditionalItemView(request):
    if request.method == "POST":
        form = addQuantityForm(request.POST)
        if form.is_valid():
            for quantity in range(int(request.POST['Quantity'])):
                newObj = AdditionalItem()
                if (request.POST['Room']):
                    if Room.objects.get(room_no = int(request.POST['Room'])):
                        newObj.room= Room.objects.get(room_no = int(request.POST['Room']))

                newObj.save()
            return redirect('addByQuantityBase')
    else:
        form = addQuantityForm()
    context = {'form':form}
    return render(request,'inventory/addByQuantity/addByQuantityAdditionalItem.html',context)

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
        roomObj = Room.objects.all().order_by('room_no')
        computerObj=Computer.objects.all()
        laptopObj = Laptop.objects.all()
        networkObj = NetworkSwitch.objects.all()
        printerObj = Printer.objects.all()
        additionalObj = AdditionalItem.objects.all()

    elif (floorNo!=500 and roomNo==500):
        roomObj = Room.objects.filter(floor=floorNo).order_by('room_no')
        for obj in roomObj:
            computerObj |= Computer.objects.filter(room=obj.room_no)
            laptopObj |= Laptop.objects.filter(room=obj.room_no)
            networkObj |= NetworkSwitch.objects.filter(room=obj.room_no)
            printerObj |= Printer.objects.filter(room=obj.room_no)
            additionalObj |= AdditionalItem.objects.filter(room=obj.room_no)
    else:
        room = Room.objects.get(room_no=roomNo)
        floorNo = room.floor
        roomObj = Room.objects.filter(floor=floorNo).order_by('room_no')
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
        roomObj = Room.objects.all().order_by('room_no')
        computerObj=Computer.objects.filter(status='OO')
        laptopObj = Laptop.objects.filter(status='OO')
        networkObj = NetworkSwitch.objects.filter(status='OO')
        printerObj = Printer.objects.filter(status='OO')
        additionalObj = AdditionalItem.objects.filter(status='OO')

    elif (floorNo!=500 and roomNo==500):
        roomObj = Room.objects.filter(floor=floorNo).order_by('room_no')
        for obj in roomObj:
            computerObj |= Computer.objects.filter(room=obj.room_no).filter(status='OO')
            laptopObj |= Laptop.objects.filter(room=obj.room_no).filter(status='OO')
            networkObj |= NetworkSwitch.objects.filter(room=obj.room_no).filter(status='OO')
            printerObj |= Printer.objects.filter(room=obj.room_no).filter(status='OO')
            additionalObj |= AdditionalItem.objects.filter(room=obj.room_no).filter(status='OO')
    else:
        room = Room.objects.get(room_no=roomNo)
        floorNo = room.floor
        roomObj = Room.objects.filter(floor=floorNo).order_by('room_no')
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
        roomObj = Room.objects.all().order_by('room_no')
        computerObj=Computer.objects.filter(status='IM')
        laptopObj = Laptop.objects.filter(status='IM')
        networkObj = NetworkSwitch.objects.filter(status='IM')
        printerObj = Printer.objects.filter(status='IM')
        additionalObj = AdditionalItem.objects.filter(status='IM')

    elif (floorNo!=500 and roomNo==500):
        roomObj = Room.objects.filter(floor=floorNo).order_by('room_no')
        for obj in roomObj:
            computerObj |= Computer.objects.filter(room=obj.room_no).filter(status='IM')
            laptopObj |= Laptop.objects.filter(room=obj.room_no).filter(status='IM')
            networkObj |= NetworkSwitch.objects.filter(room=obj.room_no).filter(status='IM')
            printerObj |= Printer.objects.filter(room=obj.room_no).filter(status='IM')
            additionalObj |= AdditionalItem.objects.filter(room=obj.room_no).filter(status='IM')
    else:
        room = Room.objects.get(room_no=roomNo)
        floorNo = room.floor
        roomObj = Room.objects.filter(floor=floorNo).order_by('room_no')
        computerObj |= Computer.objects.filter(room=room.room_no).filter(status='IM')
        laptopObj |= Laptop.objects.filter(room=room.room_no).filter(status='IM')
        networkObj |= NetworkSwitch.objects.filter(room=room.room_no).filter(status='IM')
        printerObj |= Printer.objects.filter(room__exact=room.room_no).filter(status='IM')
        additionalObj |= AdditionalItem.objects.filter(room=room.room_no).filter(status='IM')
    objCount = [computerObj.count(), laptopObj.count(), networkObj.count(), printerObj.count(), additionalObj.count()]

    context = {'roomObj': roomObj, 'floorObj': floorObj, 'computerObj': computerObj, 'laptopObj': laptopObj, 'networkObj': networkObj, 'printerObj': printerObj, 'additionalObj': additionalObj, 'objCount': objCount}
    return render(request, 'inventory/dash_search2.html', context)

def addItemsView(request):
    test = False
    if request.method =='POST':
        if request.POST.get("type") == 'computer':
            computerform = ComputerForm(request.POST)

            if computerform.is_valid():
                obj =computerform.save(commit=False)
                obj.save()

                return redirect('addview')
            context ={'form1':computerform}

        elif request.POST.get("type") == 'laptop':
            laptopform = LaptopForm(request.POST)

            if laptopform.is_valid():
                obj =laptopform.save(commit=False)
                obj.save()

                return redirect('addview')
            context = {'form2':laptopform}

        elif request.POST.get("type") == 'printer':
            printerform = PrinterForm(request.POST)

            if printerform.is_valid():
                obj =printerform.save(commit=False)
                obj.save()

                return redirect('addview')
            context = {'form3':printerform}

        elif request.POST.get("type") == 'networkswitch':
            networkswitchform = NetworkSwitchForm(request.POST)

            if networkswitchform.is_valid():
                obj =networkswitchform.save(commit=False)
                obj.save()
                return redirect('addview')
            context = {'form4':networkswitchform}

        elif request.POST.get("type") == 'additionalitem':
            additionalitemform = AdditionalItemForm(request.POST)

            if additionalitemform.is_valid():
                obj =additionalitemform.save(commit=False)
                obj.save()
                return redirect('addview')
            context = {'form5':additionalitemform}
    else:
        computerform = ComputerForm()
        laptopform = LaptopForm()
        printerform = PrinterForm()
        additionalitemform = AdditionalItemForm()
        networkswitchform = NetworkSwitchForm()
        test = True
    # context = {'form1':computerform,'form2':laptopform,'form3':printerform,'form4':networkswitchform,'form5':additionalitemform}
    if test == False:
        return render(request,'inventory/add.html',context)

    else:
        context = {'form1':computerform,'form2':laptopform,'form3':printerform,'form4':networkswitchform,'form5':additionalitemform}
        return render(request,'inventory/add.html',context)

def deleteComputerView(request,key):
    Computer.objects.get(pk=key).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def deleteLaptopView(request,key):
    Laptop.objects.get(pk=key).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def deleteNetworkSwitchView(request,key):
    NetworkSwitch.objects.get(pk=key).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def deletePrinterView(request,key):
    Printer.objects.get(pk=key).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def deleteAdditionalItemView(request,key):
    AdditionalItem.objects.get(pk=key).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def editComputerView(request,key):
    myObj = Computer.objects.get(pk=key)
    if request.method =='POST':
        editform = ComputerForm(request.POST,instance = myObj)
        if editform.is_valid():
            editform.save()
            return redirect('index')
    else:
        editform=ComputerForm(instance=myObj)
    context ={'editForm':editform}
    return render(request,'inventory/editTemplates/editICTC.html',context)

def editLaptopView(request,key):
    myObj = Laptop.objects.get(pk=key)
    if request.method =='POST':
        editform = LaptopForm(request.POST,instance = myObj)

        if editform.is_valid():
            editform.save()
            return redirect('index')
    else:
        editform=LaptopForm(instance=myObj)
    context ={'editForm':editform}
    return render(request,'inventory/editTemplates/editICTC.html',context)

def editNetworkSwitchView(request,key):
    myObj = NetworkSwitch.objects.get(pk=key)
    if request.method =='POST':
        editform = NetworkSwitchForm(request.POST,instance = myObj)

        if editform.is_valid():
            editform.save()
            return redirect('index')
    else:
        editform=NetworkSwitchForm(instance=myObj)
    context ={'editForm':editform}
    return render(request,'inventory/editTemplates/editICTC.html',context)

def editPrinterView(request,key):
    myObj = Printer.objects.get(pk=key)
    if request.method =='POST':
        editform = PrinterForm(request.POST,instance = myObj)

        if editform.is_valid():
            editform.save()
            return redirect('index')
    else:
        editform=PrinterForm(instance=myObj)
    context ={'editForm':editform}
    return render(request,'inventory/editTemplates/editICTC.html',context)

def editAdditionalItemView(request,key):
    myObj = AdditionalItem.objects.get(pk=key)
    if request.method =='POST':
        editform = AdditionalItemForm(request.POST,instance = myObj)

        if editform.is_valid():
            editform.save()
            return redirect('index')
    else:
        editform=AdditionalItemForm(instance=myObj)
    context ={'editForm':editform}
    return render(request,'inventory/editTemplates/editICTC.html',context)
