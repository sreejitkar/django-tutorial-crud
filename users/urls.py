from django.contrib import admin
from django.urls import path
import users.views as views

urlpatterns = [
    # path("", views.homepage, name="homepage"),
    # path("register/", views.register, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("login", views.login_request, name="login"),
    path("signup",views.signup,name="signup"),
    path("register",views.register_request,name="register"),
    path("add-trans",views.submit_transaction),
    path("test",views.test,name="test"),
    path("home",views.home),
    path("delete-transac",views.delete_transac),
    path("update-transac",views.update_transac)
    

]