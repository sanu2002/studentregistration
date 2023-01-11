from django.urls import path

from.import views


urlpatterns =[
    path('',views.loginaction,name ='loginaction'),
    path('signup',views.signup,name ='signup'),
    path('home',views.home,name ='home'),
    path('display',views.display_fun,name ='display'),
    path('add',views.add,name ='add'),
    path('main',views.main,name ='main'),
    path('update/<int:id>',views.update_fun,name ='update'),
    path('dlt/<int:id>',views.delete_fun,name ='dlt'),
]


