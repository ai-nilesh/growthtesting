
from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePageView.as_view(), name='home' ),
    path('artical/<int:pk>', views.ArticalPageView.as_view(), name= 'art')
  

]
