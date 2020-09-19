from django.conf.urls import url
from start_my_app import views


urlpatterns = [
    url(r'^$', views.index, name="index"),

    # Home page
    url(r'myposts/', views.myposts, name="mypost"),
    url(r'about/', views.about, name="about"),
    url(r'signup/',views.signup_form, name="signup"),
    url(r'^login/', views.UserLogin.as_view(), name="login"),
    url(r'logout/', views.logout, name="logout")

]