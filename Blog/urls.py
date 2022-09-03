from django.urls import path
from . import views

urlpatterns=[
    path("",views.ArticleView.as_view()),
    path("detail/<int:pk>",views.ArticleDetail.as_view()),
    path("add",views.ArticleAddView.as_view()),
    path("update/<int:pk>",views.ArticleUpdateView.as_view()),
    path("delete/<int:pk>",views.ArticleDeleteView.as_view())
]