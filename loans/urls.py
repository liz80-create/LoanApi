from django.urls import re_path as url
from . import views
urlpatterns=[
    url(r'^loan$',views.loancalc),
]