from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns=[
    path("",views.ArticleView.as_view()),
    path("detail/<int:pk>",views.ArticleDetail.as_view()),
    path("add",views.ArticleAddView.as_view()),
    path("update/<int:pk>",views.ArticleUpdateView.as_view()),
    path("delete/<int:pk>",views.ArticleDeleteView.as_view()),
    path("comment/<int:pk>",views.CommentArticle.as_view())
]
router = DefaultRouter()
router.register(r'article', views.ArticleViewSet, basename='article')

urlpatterns += router.urls