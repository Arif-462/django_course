from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination, CursorPagination

# creating page numbers in our website
class ProductPagination(PageNumberPagination):
    page_size = 1 # total 3 ta content 1 page 1 ta dekhabe
    page_query_param = 'p' # page name k re write kore
    page_size_query_param = 'size' # page size customize kore
    max_page_size = 3 # page size handle kore
    
    
class ProductLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    limit_query_param = 'l'
    max_limit = 5
    offset_query_param = 'start'
    
    
class ProductCursorPagination(CursorPagination):
    page_size = 1
    ordering = 'price'
    cursor_query_param = 'data'
    
    