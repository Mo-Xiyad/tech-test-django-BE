from rest_framework import serializers
from .models import ProductModel,HotListModel

class ProductModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    price = serializers.FloatField()
    quantity = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = ProductModel
        fields = ('__all__')

class HotListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotListModel
        fields = '__all__'