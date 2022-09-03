from django.urls import path
from . import views

urlpatterns=[
    path("",views.ArticleView.as_view())
]