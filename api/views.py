from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from api.models import Products,Carts,Reviews
from django.contrib.auth.models import User
from api.serializers import ProductSerializer,ProductModelSerializer,usersrl,cartsrl,reviwsrl
from rest_framework import authentication,permissions

class ProductView(APIView):

    def get(self,request,*args,**kw):
        qs = Products.objects.all()
        srl=ProductSerializer(qs,many=True)
        return Response(data=srl.data)
    
    def post(self,request,*args,**kw):
        srl=ProductSerializer(data=request.data)
        if srl.is_valid():
            Products.objects.create(**srl.data)
            return Response(data=srl.data)
        else:
            return Response(data=srl.errors)
class ProductDetailsView(APIView):

    def get(self,request,*args,**kw):
        qs = Products.objects.get(id=kw.get('id'))
        srl=ProductSerializer(qs)
        return Response(data=srl.data)
    
    def put(self,request,*args,**kw):
        srl=ProductSerializer(data=request.data)
        if srl.is_valid():
            Products.objects.filter(id=kw.get('id')).update(**request.data)
            return Response(data=srl.data)
        else:
            return Response(data=srl.errors)
    
    def delete(self,request,*args,**kw):
        Products.objects.filter(id=kw.get('id')).delete()
        return Response(data='Object deleted')

"""class ProductViewSet(ViewSet):

    def list(self,request,*args,**kw):
        qs = Products.objects.all()
        srl=ProductModelSerializer(qs,many=True)
        return Response(data=srl.data)
    
    def create(self,request,*args,**kw):
        srl=ProductModelSerializer(data=request.data)
        if srl.is_valid():
            srl.save()
            return Response(data=srl.data)
        else:
            return Response(data=srl.errors)
        
    def retrieve(self,request,*args,**kw):
        qs = Products.objects.get(id=kw.get('pk'))
        srl=ProductModelSerializer(qs)
        return Response(data=srl.data)

    def update(self,request,*args,**kw):
        obj=Products.objects.get(id=kw.get('pk'))
        srl=ProductModelSerializer(data=request.data,instance=obj)
        if srl.is_valid():
            srl.save()
            return Response(data=srl.data)
        else:
            return Response(data=srl.errors)
    
    def destroy(self,request,*args,**kw):
        Products.objects.filter(id=kw.get('pk')).delete()
        return Response(data='Object deleted')

    @action(methods=['GET'],detail=False)
    def categories(self,request,*args,**kw):
        res=Products.objects.values_list('category',flat=True).distinct()
        return Response(data=res)
    
    @action(methods=['GET'],detail=False)
    def descriptions(self,request,*args,**kw):
        tes=Products.objects.values_list('description',flat=True).distinct()
        return Response(data=tes)
"""
"""class UserView(ViewSet):
    def create(self,request,*args,**kw):
       srl=usersrl(data=request.data)
       if srl.is_valid():
           srl.save()
           return Response(data=srl.data)
       else:
           return Response(data=srl.errors)

"""

class ProductViewSet(ModelViewSet):
    serializer_class=ProductModelSerializer
    queryset=Products.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    @action(methods=['POST'],detail=True)
    def add_to_cart(self,request,*args,**kw):
        id=kw.get('pk')
        item=Products.objects.get(id=id)
        user = request.user
        user.carts_set.create(Products=item)
        return Response(data='item added to cart')
    
    @action(methods=['POST'],detail=True)
    def add_review(self,request,*args,**kw):
        usr = request.user
        id=kw.get('pk')
        prd=Products.objects.get(id=id)
        srl=reviwsrl(data=request.data)
        if srl.is_valid():
            srl.save(Products=prd,user=usr)
            return Response(data=srl.data)
        else:
            return Response(data=srl.errors)
    @action(methods=['GET'],detail=True)
    def view_reviews(self,request,*args,**kw):
        Prd=Products.objects.get(id=kw.get("pk"))
        # prd=self.get_object()
        qs=Prd.reviews_set.all()
        return Response(reviwsrl(qs,many=True).data)

class UserView(ModelViewSet):
    serializer_class=usersrl
    queryset=User.objects.all()

"""class cartview(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def post(self,request,*args,**kw):
        item=Products.objects.get(id=kw.get('id'))
        user = request.user
        user.carts_set.create(Products=item)
        return Response(data='item added to cart')
"""

class CartView(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=cartsrl
    queryset=Carts.objects.all()
    def get_queryset(self):
        return self.request.user.carts_set.all()
    
    """def list(self,request,*args,**kw):
        qs=request.user.carts_set.all()
        # qs=Carts.objects.filter(user=request.user)
        srl=cartsrl(qs,many=True)
        return Response(data=srl.data)"""

class reviewdeleter(APIView):
    def delete(self,request,*args,**kw):
        sr=Reviews.objects.filter(id=kw.get('id')).delete()
        return Response(data='review deleted successfully')
        