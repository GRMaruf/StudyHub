from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signin/', auth_views.LoginView.as_view(template_name='accounts/signin.html', next_page='home'), name='signin'),
    path('signout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
]
