from django.shortcuts import render, redirect
from .models import Categorie, Item, Floor, Room
from .forms import addCategoryForm, addItemForm, addExistingForm, allocateForm,addRoomForm,addFloorForm,categoryEditForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dashboardView(request):
    categoryDetails = []
    working_count = in_maintenanace_count = out_of_order_count = 0
    categoryObj = Categorie.objects.order_by('id')
    for cat in categoryObj:
        itemObj = Item.objects.filter(category = cat)
        for obj in itemObj:
            working_count += obj.working if obj.working!=0 else 0
            in_maintenanace_count += obj.in_maintenance if obj.in_maintenance!=0 else 0
            out_of_order_count += obj.out_of_order if obj.out_of_order!=0 else 0
        temp = [cat.category_name,working_count,out_of_order_count,in_maintenanace_count]
        categoryDetails.append(temp)
        working_count = in_maintenanace_count = out_of_order_count = 0
    context = {'categoryDetails':categoryDetails}
    return render(request, 'inventory/base.html',context)

@login_required
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!.LogIn again')
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'inventory/register.html', context)

@login_required
def add1(request):
    categories = Categorie.objects.all()
    dataTemp = {}
    if request.method == 'POST':
        addCategoryform = addCategoryForm(request.POST)
        if addCategoryform.is_valid():
            if (request.POST['extraField1']):
                temp = request.POST['extraField1']
                dataTemp.update({'field1': temp})
            if (request.POST['extraField2']):
                temp = request.POST['extraField2']
                dataTemp.update({'field2': temp})
            if (request.POST['extraField3']):
                temp = request.POST['extraField3']
                dataTemp.update({'field3': temp})
            Categorie.objects.create(
                category_name=request.POST['categoryName'], extra_fields=dataTemp)
            messages.success(request, f'Category created successfully! Select the category to add some equipments')
            return redirect('add1')
    else:
        addCategoryform = addCategoryForm()
    context = {'categories': categories, 'addCategoryForm': addCategoryform}
    return render(request, 'inventory/add1.html', context)

@login_required
def add2(request, key):
    categoryObj = Categorie.objects.get(pk=key)
    itemObj = Item.objects.filter(category=categoryObj)
    if request.method == 'POST':
        addItemform = addItemForm(data=request.POST, extra_fields_dict=categoryObj.extra_fields)
        if (addItemform.is_valid):
            addItemform.save()
            obj = Item.objects.latest('created')
            obj.category = categoryObj
            obj.save()
            if len(categoryObj.extra_fields) == 1:
                temp = categoryObj.extra_fields['field1']
                # vars()[temp] = forms.CharField(max_length=100,required=False)
                obj.extra_value.update({temp: request.POST[temp]})
            elif len(categoryObj.extra_fields) == 2:
                temp1 = categoryObj.extra_fields['field1']
                temp2 = categoryObj.extra_fields['field2']
                temp = {temp1: request.POST[temp1], temp2: request.POST[temp2]}
                obj.extra_value.update(temp)
            elif len(categoryObj.extra_fields) == 3:
                temp1 = categoryObj.extra_fields['field1']
                temp2 = categoryObj.extra_fields['field2']
                temp3 = categoryObj.extra_fields['field3']
                temp = {temp1: request.POST[temp1],
                        temp2: request.POST[temp2], temp3: request.POST[temp3]}
                obj.extra_value.update(temp)
            obj.save()
            if (request.POST['room']):
                pass
            else:
                obj.room = Room.objects.get(room_name__exact= 'Store')
                obj.save()

            messages.success(request, f'Added Successfully!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    else:
        addItemform = addItemForm(extra_fields_dict=categoryObj.extra_fields)
    context = {'itemObj': itemObj, 'addItemform': addItemform}
    return render(request, 'inventory/add2.html', context)

@login_required
def addExisting(request, key):
    obj = Item.objects.get(pk=key)
    if request.method == 'POST':
        addExistingform = addExistingForm(request.POST)
        if addExistingform.is_valid:
            obj.working += int(request.POST['quantity'])
            obj.save()
            messages.success(request, f'Added Successfully!')
            return redirect('dashboard')
    else:
        addExistingform = addExistingForm(request.POST)
    context = {'addExistingform': addExistingform}
    return render(request, 'inventory/addExisting.html', context)

@login_required
def allocate(request, key):
    obj = Item.objects.get(pk=key)
    if request.method == 'POST':
        allocateform = allocateForm(request.POST)
        if allocateform.is_valid:
            wk = int(request.POST['working']) if (request.POST['working']) else 0
            oo = int(request.POST['out_of_order']) if (request.POST['out_of_order']) else 0
            im = int(request.POST['in_maintenance']) if (request.POST['in_maintenance']) else 0
            dr = int(request.POST['room'])
            if (dr):
                dr = Room.objects.get(pk=dr)
            if(wk > obj.working or oo > obj.out_of_order or im > obj.in_maintenance or (dr == None)):
                messages.warning(request, f'Error! Enter a valid value')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            else:
                itemDestination = Item.objects.filter(room=dr).filter(
                    name=obj.name).filter(model=obj.model)
                if (itemDestination):
                    itemDestination[0].working += wk
                    itemDestination[0].out_of_order += oo
                    itemDestination[0].in_maintenance += im
                    itemDestination[0].save()
                else:
                    Item.objects.create(category=obj.category, name=obj.name, model=obj.model, working=wk, out_of_order=oo, in_maintenance=im,
                                        date_of_acquire=obj.date_of_acquire, cost_per_item=obj.cost_per_item, room=dr, extra_value=obj.extra_value)
                obj.working -= wk
                obj.in_maintenance -= im
                obj.out_of_order -= oo
                obj.save()
                if (obj.working <= 0 and obj.in_maintenance <= 0 and obj.out_of_order <= 0):
                    obj.delete()
                messages.success(request, f'Allocated Successfully!')
    else:
        allocateform = allocateForm()
    dict ={}
    dict.update({"working":obj.working,"out_of_order":obj.out_of_order,"in_maintenance":obj.in_maintenance,"room":obj.room})
    context = {'allocateform': allocateform}
    context.update(dict)
    return render(request, 'inventory/allocate.html', context)

@login_required
def search(request, floorNumber, roomNumber):
    item = Item.objects.none()
    dict = {}
    floor = Floor.objects.order_by('floor')
    if (floorNumber == 999):  # all floors
        room = Room.objects.all()
    else:
        floorObj = Floor.objects.get(pk=floorNumber)
        # when any floor number is clicked, filter all rooms from that floor
        room = Room.objects.filter(floor=floorObj)
    if(roomNumber == 999 and floorNumber == 999):  # all floors and all rooms
        item |= Item.objects.all()
    elif (roomNumber == 999 and floorNumber != 999):  # when any floorNo is clicked but roomNo is not clicked
        for roomObj in room:
            # append all the items from all the rooms that belong to that floor (filtered on line 124 and 125)
            item |= Item.objects.filter(room=roomObj)
    else:
        roomObj = Room.objects.get(pk=roomNumber)  # when a particular room number is clicked
        floorObj = roomObj.floor  # get the floor number of the clicked room number
        # rooms must be displayed that is located on floor of the clicked room
        room = Room.objects.filter(floor=floorObj)
        item |= Item.objects.filter(room=roomObj)  # items belonging to the clicked room
    categories = Categorie.objects.all()  # all categories are displayed
    count = 0
    itemno = [a for a in range(100)]  # temporary 100 values for array definition
    print(count)
    for categoryno in categories:
        # itemno[0] = items of 1st category, and so on(filter for already filtered item)
        itemno[count] = item.filter(category=categoryno)
        count += 1  # counts the total number of categories
    for i in range(count):
        # {item0:itemno[0],item1:itemno[1],item2:itemno[2]}....and so on
        dict.update({"item"+str(i): itemno[i]})
    room.order_by('room_no')
    context = {'floor': floor, 'room': room, 'categories': categories, 'count': count}
    # {%for item in item0%} represents filterd item list of 1st category and so on upto count number of categories in template
    context.update(dict)
    return render(request, 'inventory/search.html', context)

@login_required
def delete(request,key):
    Item.objects.get(pk=key).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def edit(request,key):
    obj = Item.objects.get(pk=key)
    categoryObj = obj.category
    if request.method == 'POST':
        addItemform = addItemForm(data=request.POST,extra_fields_dict=categoryObj.extra_fields,instance = obj)
        if (addItemform.is_valid):
            addItemform.save()
            obj.save()
            if len(categoryObj.extra_fields) ==1:
                temp = categoryObj.extra_fields['field1']
                # vars()[temp] = forms.CharField(max_length=100,required=False)
                if (request.POST[temp]):
                    obj.extra_value.update({temp:request.POST[temp]})
            elif len(categoryObj.extra_fields) ==2:
                temp1 = categoryObj.extra_fields['field1']
                temp2 = categoryObj.extra_fields['field2']
                if (request.POST[temp1]):
                    obj.extra_value.update({temp1:request.POST[temp1]})
                if (request.POST[temp2]):
                    obj.extra_value.update({temp2:request.POST[temp2]})

            elif len(categoryObj.extra_fields) ==3:
                temp1 = categoryObj.extra_fields['field1']
                temp2 = categoryObj.extra_fields['field2']
                temp3 = categoryObj.extra_fields['field3']
                if (request.POST[temp1]):
                    obj.extra_value.update({temp1:request.POST[temp1]})
                if (request.POST[temp2]):
                    obj.extra_value.update({temp2:request.POST[temp2]})
                if (request.POST[temp3]):
                    obj.extra_value.update({temp3:request.POST[temp3]})
            obj.save()
            messages.success(request, f'Edit Successful!')
            return redirect('dashboard')

    else:
        addItemform = addItemForm(extra_fields_dict=categoryObj.extra_fields,instance = obj)
    context = {'addItemform':addItemform}
    return render(request,'inventory/edit.html',context)

@login_required
def editcategory(request):
    categoryObj = Categorie.objects.all()
    return render(request,'inventory/editcategory.html',{'categoryObj':categoryObj})

@login_required
def editcategory2(request,key):
    categoryObj = Categorie.objects.get(pk=key)
    if request.method == 'POST':
        form = categoryEditForm(request.POST,instance=categoryObj)
        if form.is_valid:
            try:
                form.save()
                messages.success(request, f'Edit successful!')
            except:
                messages.warning(request, f'Edit failed! Invalid name')
            return redirect('editcategory')
    else:
        form = categoryEditForm(instance=categoryObj)
    context = {'form': form}
    return render(request,'inventory/editcategory2.html',context)

@login_required
def createroom(request):
    if request.method == 'POST':
        createRoomform = addRoomForm(request.POST)
        if createRoomform.is_valid:
            try:
                createRoomform.save()
                messages.success(request, f'Room is successfully created!')
            except:
                messages.warning(request, f'Room is either invalid or already available!')
            return redirect('createroom')
    else:
        createRoomform = addRoomForm()
    context = {'createRoomform': createRoomform}
    return render(request,'inventory/createroom.html',context)

@login_required
def createfloor(request):
    if request.method == 'POST':
        createFloorform = addFloorForm(request.POST)
        if createFloorform.is_valid:
            try:
                createFloorform.save()
                messages.success(request, f'Floor is successfully created!')
            except:
                messages.warning(request, f'Floor is either invalid or already available!')

            return redirect('createfloor')
    else:
        createFloorform = addFloorForm()
    context = {'createFloorform': createFloorform}
    return render(request,'inventory/createfloor.html',context)

@login_required
def search2(request, floorNumber, roomNumber):
    item = Item.objects.none()
    dict = {}
    floor = Floor.objects.order_by('floor')
    if (floorNumber == 999):  # all floors
        room = Room.objects.all()
    else:
        floorObj = Floor.objects.get(pk=floorNumber)
        # when any floor number is clicked, filter all rooms from that floor
        room = Room.objects.filter(floor=floorObj)
    if(roomNumber == 999 and floorNumber == 999):  # all floors and all rooms
        item |= Item.objects.filter(out_of_order__gt=0)
    elif (roomNumber == 999 and floorNumber != 999):  # when any floorNo is clicked but roomNo is not clicked
        for roomObj in room:
            # append all the items from all the rooms that belong to that floor (filtered on line 124 and 125)
            item |= Item.objects.filter(room=roomObj).filter(out_of_order__gt=0)
    else:
        roomObj = Room.objects.get(pk=roomNumber)  # when a particular room number is clicked
        floorObj = roomObj.floor  # get the floor number of the clicked room number
        # rooms must be displayed that is located on floor of the clicked room
        room = Room.objects.filter(floor=floorObj)
        item |= Item.objects.filter(room=roomObj).filter(out_of_order__gt=0)  # items belonging to the clicked room
    categories = Categorie.objects.all()  # all categories are displayed
    count = 0
    itemno = [a for a in range(100)]  # temporary 100 values for array definition
    print(count)
    for categoryno in categories:
        # itemno[0] = items of 1st category, and so on(filter for already filtered item)
        itemno[count] = item.filter(category=categoryno)
        count += 1  # counts the total number of categories
    for i in range(count):
        # {item0:itemno[0],item1:itemno[1],item2:itemno[2]}....and so on
        dict.update({"item"+str(i): itemno[i]})
    room.order_by('room_no')
    context = {'floor': floor, 'room': room, 'categories': categories, 'count': count}
    # {%for item in item0%} represents filterd item list of 1st category and so on upto count number of categories in template
    context.update(dict)
    return render(request, 'inventory/search2.html', context)

@login_required
def search3(request, floorNumber, roomNumber):
    item = Item.objects.none()
    dict = {}
    floor = Floor.objects.order_by('floor')
    if (floorNumber == 999):  # all floors
        room = Room.objects.all()
    else:
        floorObj = Floor.objects.get(pk=floorNumber)
        # when any floor number is clicked, filter all rooms from that floor
        room = Room.objects.filter(floor=floorObj)
    if(roomNumber == 999 and floorNumber == 999):  # all floors and all rooms
        item |= Item.objects.filter(in_maintenance__gt=0)
    elif (roomNumber == 999 and floorNumber != 999):  # when any floorNo is clicked but roomNo is not clicked
        for roomObj in room:
            # append all the items from all the rooms that belong to that floor (filtered on line 124 and 125)
            item |= Item.objects.filter(room=roomObj).filter(in_maintenance__gt=0)
    else:
        roomObj = Room.objects.get(pk=roomNumber)  # when a particular room number is clicked
        floorObj = roomObj.floor  # get the floor number of the clicked room number
        # rooms must be displayed that is located on floor of the clicked room
        room = Room.objects.filter(floor=floorObj)
        item |= Item.objects.filter(room=roomObj).filter(in_maintenance__gt=0)  # items belonging to the clicked room
    categories = Categorie.objects.all()  # all categories are displayed
    count = 0
    itemno = [a for a in range(100)]  # temporary 100 values for array definition
    print(count)
    for categoryno in categories:
        # itemno[0] = items of 1st category, and so on(filter for already filtered item)
        itemno[count] = item.filter(category=categoryno)
        count += 1  # counts the total number of categories
    for i in range(count):
        # {item0:itemno[0],item1:itemno[1],item2:itemno[2]}....and so on
        dict.update({"item"+str(i): itemno[i]})
    room.order_by('room_no')
    context = {'floor': floor, 'room': room, 'categories': categories, 'count': count}
    # {%for item in item0%} represents filterd item list of 1st category and so on upto count number of categories in template
    context.update(dict)
    return render(request, 'inventory/search3.html', context)

def detailsView(request,key):
    categoryObj = Categorie.objects.get(pk=key)
    itemObj = Item.objects.filter(category = categoryObj)
    context = {'itemObj':itemObj,'categoryObj':categoryObj}
    return render(request,'inventory/details.html',context)
