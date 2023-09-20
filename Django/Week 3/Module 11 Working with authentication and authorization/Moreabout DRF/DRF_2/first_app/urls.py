from django.urls import include, path
from rest_framework import routers
from .views import ProductReviewSet, ProductReviewViewset

router = routers.DefaultRouter()
router.register('products', ProductReviewSet, basename='product')
router.register('reviews', ProductReviewViewset, basename='product_review')

urlpatterns = [
    path('', include(router.urls)),
    # path('api_auth/', include('rest_framework.urls')),
]
