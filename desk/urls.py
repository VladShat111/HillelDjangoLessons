from django.urls import path, include
from .views import fileDesk, registration

urlpatterns = [

    path('reqistration/', registration, name='registration'),
    path('filedesk/', fileDesk, name='fileDesk'),
    path('', include('django.contrib.auth.urls')),

]
