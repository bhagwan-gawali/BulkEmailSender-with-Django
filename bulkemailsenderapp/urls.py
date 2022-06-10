from django.urls import path
from bulkemailsenderapp import views

urlpatterns = [
    path('home/', views.indexView, name='index'),
]