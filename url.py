from django.urls import path
from mycart import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.add, name='add'),
    path('addcart/Templates', views.addcart, name='addcart'),
    path('delete/Templates/<int:id>', views.delete, name='delete'),
    path('edit/Templates/<int:id>', views.edit, name='edit'),
    path('listproduct/Templates', views.listproduct, name='listproduct'),
    path('login/Templates', views.login, name='login'),
    path('signup/Templates', views.signup, name='signup'),
    path('viewcart/Templates', views.viewcart , name='viewcart'),
    path('viewproduct/Templates', views.viewproduct, name='viewproduct'),

]