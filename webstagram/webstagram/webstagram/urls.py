from django.contrib import admin
from django.urls import path
from webstaApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name="login"),
    path('signup/', signup, name="signup"),
    path('profile/', profile, name="profile"),
    path('feed/', feed, name="feed")
]
