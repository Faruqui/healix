from django.urls import path
from services import views
from . import views
urlpatterns = [
    path('eprescription/',views.eprescription,name='prescription')

]
