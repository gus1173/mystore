from rest_framework import serializers
from api.models import Products,Carts,Reviews
from django.contrib.auth.models import User

class ProductSerializer(serializers.Serializer):
    
    name = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    category =serializers.CharField()
    image = serializers.ImageField

class ProductModelSerializer(serializers.ModelSerializer):
    avg_rating = serializers.CharField(read_only=True)
    review_count = serializers.CharField(read_only=True)
    class Meta:
        model = Products
        fields = "__all__"

class usersrl(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
    
class cartsrl(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    Products = serializers.CharField(read_only=True)
    date = serializers.CharField(read_only=True)
    class Meta:
        model = Carts
        fields = "__all__"

class reviwsrl(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    Products = serializers.CharField(read_only=True)
    class Meta:
        model = Reviews
        fields = "__all__"