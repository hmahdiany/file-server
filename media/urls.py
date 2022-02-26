from django.urls import path
from . import views


urlpatterns = [
    path('', views.qcow_list, name='qcow_list'),
    #path('upload/', views.upload, name='upload'),
    path('qcow/upload/', views.upload_qcow, name='upload_qcow'),
    path('qcow/<int:pk>/', views.delete_qcow, name='delete_qcow' )
]