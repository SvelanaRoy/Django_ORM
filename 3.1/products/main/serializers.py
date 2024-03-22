from rest_framework import serializers
from main.models import Product
from main.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'mark']


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'price']


#class ProductDetailsSerializer(serializers.ModelSerializer):
    #reviews = ReviewSerializer(many=True, read_only=True)
    
    #class Meta:
        #model = Product
        #fields = ['title', 'description','price','reviews']
        
class ProductDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['title', 'price', 'description']
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['reviews'] = list(
            [ReviewSerializer(rew).data for rew in Review.objects.filter(product=instance)]
        )
        return representation        