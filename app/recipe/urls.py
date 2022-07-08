"""
URL mappings for the recipe app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)
router.register('tags', views.TagViewSet)

# learning: name used when performing reverse lookup of urls
app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
