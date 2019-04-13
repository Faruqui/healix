from django.urls import path
from .views import (
    CreatePrescription,
    HospitalListView,
    GeneratePDF, GeneratePdf,
    UserPrescriptionList,
    PrescriptionDetailView,
)
from . import views

urlpatterns = [
    #path('', views.home, name = 'blog-home'),
    path('newPres/', views.CreatePrescription.as_view(), name = 'createPres'),
    path('hospitals/', HospitalListView.as_view(),name='hospitals'),
    #path('pdf/',GeneratePDF.as_view(),name="pdf"),
    path('pdf/<int:pk>',GeneratePdf.as_view(),name="pdf"),
    #path('prescriptions/',UserPrescriptionList.as_view(),name="prescriptions"),
    path('prescriptions/', views.prescription_list, name = 'prescriptions'),
    path('prescriptions/<int:pk>/', PrescriptionDetailView.as_view(), name = 'prescription-detail'),
]
