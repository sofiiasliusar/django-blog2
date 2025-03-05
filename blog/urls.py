from django.urls import path
from blog import views

urlpatterns = [
    path(r'', views.HomePageView.as_view())
]
