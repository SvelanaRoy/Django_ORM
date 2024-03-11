from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from main.models import Review

from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer
from .models import Product

@api_view(['GET'])
def products_list_view(request):
    products = Product.objects.all()
    ser = ProductListSerializer(products, many=True)
    return Response(ser.data)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            ser = ProductDetailsSerializer(product)
            return Response(ser.data)
        except Product.DoesNotExist:
            raise Http404('Product not found')




# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """обработайте значение параметра mark и
        реализуйте получение отзывов по конкретному товару с определённой оценкой
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        pass
