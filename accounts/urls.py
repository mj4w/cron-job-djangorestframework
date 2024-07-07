from django.urls import path
from . import views
urlpatterns = [
    # path('sample/', views.sample, name='sample')
    path('user/', views.UserView.as_view(), name='user'),
]