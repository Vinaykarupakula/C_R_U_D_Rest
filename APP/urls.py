import imp
from django.urls import path
from .views import *

urlpatterns = [
    path('', bookList),
    path('create/', bookCreate),

]