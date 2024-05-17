from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/signup', views.SignUpView.as_view(), name='signup'),
    path('accounts/', include('allauth.urls')),
]
