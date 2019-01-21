from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboardView, name='index'),
    path('', views.loginView, name='login'),
    path('tableICT/', views.tableICTView, name='tableICT'),
    path('tableLAB/', views.tableLABView, name='tableLAB'),
    path('testurl/<int:floorNo>/<int:roomNo>',views.testView,name='testUrl'),

]
