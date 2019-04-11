from django.urls import path
from .views import (
    CreatePrescription,
    HospitalListView,
    GeneratePDF,
)
from . import views

urlpatterns = [
    #path('', views.home, name = 'blog-home'),
    path('newPres/', views.CreatePrescription.as_view(), name = 'createPres'),
    path('hospitals/', HospitalListView.as_view(),name='hospitals'),
    path('pdf/',GeneratePDF.as_view(),name="pdf"),
]
