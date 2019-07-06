from django.urls import path,include
from userdata.views import *

urlpatterns = [
    path('/create_data/', DataCreate.as_view()),
]