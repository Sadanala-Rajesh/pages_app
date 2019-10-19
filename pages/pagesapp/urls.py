from django.urls import path
from .views import display,HomePageView,AboutPageView

urlpatterns = [
    path('', display,name='display'),
    
    path('data/',HomePageView.as_view(),name ='home'),
    path('about/',AboutPageView.as_view(),name='about'),
    
]
