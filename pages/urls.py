from django.urls import path
from pages.views import home_page_view, register

app_name = 'pages'

urlpatterns = [
    path('', home_page_view, name='home'),
    path('register/', register, name='register'),
]