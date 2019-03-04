from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboardView, name='index'),
    path('', views.loginView, name='login'),
    path('tableICT/', views.tableICTView, name='tableICT'),
    path('tableLAB/', views.tableLABView, name='tableLAB'),
    path('testurl/<int:floorNo>/<int:roomNo>', views.testView, name='testUrl'),
    path('dashsearch/<int:floorNo>/<int:roomNo>', views.dashSearchView, name='dashsearchUrl'),
    path('dashsearch2/<int:floorNo>/<int:roomNo>', views.dashSearch2View, name='dashsearch2Url'),
    path('addByQuantityComputer',views.addItemByQuantityComputerView,name="addByQuantityComputer"),
    path('addByQuantityLaptop',views.addItemByQuantityLaptopView,name="addByQuantityLaptop"),
    path('addByQuantityNetworkSwitch',views.addItemByQuantityNetworkSwitchView,name="addByQuantityNetworkSwitch"),
    path('addByQuantityPrinter',views.addItemByQuantityPrinterView,name="addByQuantityPrinter"),
    path('addByQuantityAdditionalItem',views.addItemByQuantityAdditionalItemView,name="addByQuantityAdditionalItem"),
    path('addByQuantityBase',views.addItemByQuantityBaseView,name="addByQuantityBase"),
    path('add',views.addItemsView,name='addview'),
    path('delete/Computer/<int:key>',views.deleteComputerView,name='deleteComputer'),
    path('delete/Laptop/<int:key>',views.deleteLaptopView,name='deleteLaptop'),
    path('delete/NetworkSwitch/<int:key>',views.deleteNetworkSwitchView,name='deleteNetworkSwitch'),
    path('delete/Printer/<int:key>',views.deletePrinterView,name='deletePrinter'),
    path('delete/AdditionalItem/<int:key>',views.deleteAdditionalItemView,name='deleteAdditionalItem'),
    path('edit/Computer/<int:key>',views.editComputerView,name='editComputer'),
    path('edit/Laptop/<int:key>',views.editLaptopView,name='editLaptop'),
    path('edit/NetworkSwitch/<int:key>',views.editNetworkSwitchView,name='editNetworkSwitch'),
    path('edit/Printer/<int:key>',views.editPrinterView,name='editPrinter'),
    path('edit/AdditionalItem/<int:key>',views.editAdditionalItemView,name='editAdditionalItem'),

]
