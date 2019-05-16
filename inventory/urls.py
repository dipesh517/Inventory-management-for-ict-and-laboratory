from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('add1/', views.add1, name='add1'),
    path('add2/<int:key>', views.add2, name='add2'),
    path('register/', views.register, name='register'),
    path('', auth_views.LoginView.as_view(template_name='inventory/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='inventory/logout.html'), name='logout'),
    path('addExisting/<int:key>', views.addExisting, name='addExisting'),
    path('allocate/<int:key>', views.allocate, name='allocate'),
    path('search/<int:floorNumber>/<int:roomNumber>', views.search, name='search'),
    path('search2/<int:floorNumber>/<int:roomNumber>', views.search2, name='search2'),
    path('search3/<int:floorNumber>/<int:roomNumber>', views.search3, name='search3'),
    path('delete/<int:key>',views.delete,name='delete'),
    path('edit/<int:key>',views.edit,name='edit'),
    path('editcategory/',views.editcategory,name='editcategory'),
    path('editcategory/<int:key>',views.editcategory2,name='editcategory2'),
    path('createroom/',views.createroom,name='createroom'),
    path('createfloor/',views.createfloor,name='createfloor'),
    path('details/<int:key>',views.detailsView,name='details'),


]
