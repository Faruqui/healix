from django.urls import path
from services import views

urlpatterns = [
    path('eprescription/',views.eprescription.as_view(),name='prescription')

]
