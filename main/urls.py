from django.contrib.auth import urls
from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [

    path("", Landing.as_view(),name="index"),
    path("coachs", CoachExplore.as_view(),name="coachs"),
    path("Request", ProgramRequestView.as_view(),name="ProgramRequest"),
    
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    
    path('program/<int:program_id>/', ProgramDetail.as_view() , name='program_detail'),
    path('nutrient/<int:program_id>/', NutrientDetail.as_view() , name='nutrient_detail'),
]