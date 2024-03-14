from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
        path('create/', CreateReminderView.as_view(), name='create_reminder'),

]
