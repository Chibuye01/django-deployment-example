
from django.urls import path
from basic_app import views


# FOR TEMPLATE TAGGING USE APP_NAME TO CREATE GLOBGAL VARIABLE & ASSIGN YOUR APP NAME
app_name = 'basic_app'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
