from django.urls import path
from django.contrib import admin
from .import views

app_name = 'forms'
urlpatterns = [

    path('review/', views.SubmissionTableView.as_view(), name='review'),
    path('review/risk_factors', views.RiskFactorTableView.as_view(), name='risk_factor_review'),
    path('review/risk_controls', views.RiskFactorTableView.as_view(), name='risk_control_review'),
    path('submit/<slug:form_name>/',views.DefaultFormView.as_view(), name='display_form'),
    path('submit/<slug:form_name>/wizard/', views.WizardFormView.as_view(), name='display_wizard'),
    path('edit/<slug:form_name>/<int:form_id>/', views.EditFormView.as_view(), name="edit"),
    path('editWizard/<slug:form_name>/<slug:form_id>/', views.EditWizardView.as_view(),name = 'editWizard'),
    path('add/<slug:form_name>/', views.RiskFactorAddView.as_view(), name='addRiskFactor'),
    path('edit_risk_factor/<slug:form_name>/<slug:form_id>/', views.RiskFactorEditView.as_view(), name="editRiskFactor"),

]
