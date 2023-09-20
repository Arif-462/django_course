from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from . import permissions 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from . import paginations



# Create your views here.

class ProductReviewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AdminOrReadOnly]
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    # searching by django
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name', 'description']
    # ordering handling by django
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['price']
    # pagination_class = paginations.ProductPagination
    # pagination_class = paginations.ProductLimitOffsetPagination
    # cursor pagination kaj korale filtering kaj bondho kore dite hobe
    pagination_class = paginations.ProductCursorPagination
    
    
    
    
    
    
    
    
    
class ProductReviewViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.ReviewerOrReadOnly]
    queryset = models.ProductReview.objects.all()
    serializer_class = serializers.ProductReviewSerializer
    # 1 .filtering by django accoriding to reviews
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['rating', 'product'] 
    # ordering with rating handling by django
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['rating']  
    # or 2. way get requestion handling/filtering handling by django    
    # def get_queryset(self):        
    #     queryset = models.ProductReview.objects.all()
    #     username = self.request.query_params.get('username')
    #     if username is not None:
    #         queryset = queryset.filter(user__username__icontains=username)#icontains case sensetive kaj kore
    #     return queryset
    
  
