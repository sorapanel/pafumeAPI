from rest_framework import viewsets
from .models import perfumeInfo
from .serializers import perfumeInfoSerializer
from .pagination import PerfumePaginationClass

# Create your views here.
class perfumeInfoViewSet(viewsets.ModelViewSet):
    queryset = perfumeInfo.objects.all().prefetch_related('categories')
    serializer_class = perfumeInfoSerializer
    http_method_names = ['get', 'head', 'options']
    pagination_class = PerfumePaginationClass

    def  get_queryset(self):
        queryset = perfumeInfo.objects.all().prefetch_related('categories')
        title = self.request.query_params.get('title', None)
        category = self.request.query_params.get('category', None)
        brand = self.request.query_params.get('brand', None)
        brandJp = self.request.query_params.get('brandJp', None)
        

        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        if category is not None:
            queryset = queryset.filter(categories__category__icontains=category)
        if brand is not None:
            queryset = queryset.filter(brand__icontains=brand)
        if brandJp is not None:
            queryset = queryset.filter(brandJp__icontains=brandJp)


        return queryset