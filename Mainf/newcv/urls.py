from django.urls import path
from newcv import views


urlpatterns = [
    path('newcv/', views.Newcv, name='NEWCV')
]


