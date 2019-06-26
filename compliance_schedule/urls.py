from django.urls import path, re_path
from . import views
app_name="compliance_schedule"
urlpatterns = [
    path('addItem/', views.ItemView.as_view(), name='addItem'),
    path('viewCompliance/', views.ComplianceTableView.as_view(), name='viewCompliance'),
    path('update/<int:form_id>/', views.UpdateView.as_view(), name='updateCompliance'),
    path('addPolicy/', views.PolicyFormView.as_view(), name='addPolicy'),
    path('viewPolicy/', views.PolicyTableView.as_view(), name='viewPolicy'),
    path('updatePolicy/<int:form_id>/',views.UpdatePolicyView.as_view(), name='updatePolicy' )
]
