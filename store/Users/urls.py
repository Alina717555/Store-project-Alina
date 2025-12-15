from django.urls import path
from Users.views import login, register, profile, logout, email_verification

app_name = 'Users'

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('verify-email/', email_verification, name='email_verification'),
]
