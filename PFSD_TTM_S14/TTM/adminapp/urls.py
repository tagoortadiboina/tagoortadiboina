from django.urls import path
from . import views

urlpatterns = [
    path('checkadminlogin/', views.checkadminlogin, name="checkadminlogin"),
    path('checkregistration/', views.checkregistration, name="checkregistration"),  # corrected typo
    path('userhome/', views.userhome, name="userhome"),
    path('addpackage/', views.addpackage, name="addpackage"),
    path('checkpackage/', views.checkpackage, name="checkpackage"),
    path("adminhome/", views.adminhome, name="adminhome"),
    path("viewpackage/", views.viewpackage, name="viewpackage"),
    path("userpackage/", views.userpackage, name="userpackage"),
    path("changepassword/", views.changepassword, name="change password"),
]
