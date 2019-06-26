from django.urls import path, re_path
from . import views
app_name="dashboard"
urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
#    re_path(r'^.*\.html', views.gentella_html, name='gentella'),

    # The home page

    path('', views.index, name='index'),
    
    path('incident/', views.incident, name="incident"),
    path('complaint/', views.complaint, name="complaint")

]
