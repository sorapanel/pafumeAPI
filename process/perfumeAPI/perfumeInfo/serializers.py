from rest_framework import serializers
from .models import perfumeInfo, perfumeCategory

class perfumeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = perfumeCategory
        fields = '__all__'


class perfumeInfoSerializer(serializers.ModelSerializer):
    categories = perfumeCategorySerializer(read_only=True, many=True)

    class Meta:
        model = perfumeInfo
        fields = '__all__'