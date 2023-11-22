from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, BooksViewSet





router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'books', BooksViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
