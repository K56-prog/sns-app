from django.urls import path
from .views import listfunc, detailfunc, goodfunc, readfunc, SnsCreate, signupfunc, loginfunc, logoutfunc

urlpatterns = [
    path('list/', listfunc, name='list'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('read/<int:pk>', readfunc, name='read'),
    path('create/', SnsCreate.as_view(), name='create'),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
]
