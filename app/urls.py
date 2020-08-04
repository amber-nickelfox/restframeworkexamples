from django.contrib import admin
from django.urls import path, include
from .views import company_view, EmployeeAPIView ,company_details, CompanyAPIView, CompanyMixinsAPIView, CompanyDetailAPIView

urlpatterns = [
        path('company', CompanyAPIView.as_view(), name="company-post"),
        path('company/<int:pk>', CompanyDetailAPIView.as_view(), name="company-details"),
        path('employee/<int:company_id>', EmployeeAPIView.as_view(), name="employee")
]
