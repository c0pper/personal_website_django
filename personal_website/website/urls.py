from . import views
from django.urls import path
from .views import ProjectDetailView

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>/', ProjectDetailView.as_view(), name='project-detail'),
]