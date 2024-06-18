from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken

router = DefaultRouter()
router.register('api/products',views.ProductViewSet,basename="Products")
router.register('login',views.UserView,basename='user')
router.register('cart',views.CartView,basename='Carts')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products', views.ProductView.as_view()),
    path('products/<int:id>', views.ProductDetailsView.as_view()),
    path('deletereview/<int:id>', views.reviewdeleter.as_view()),
    path('token', ObtainAuthToken.as_view()),
    # path('addtocart/<int:id>', views.cartview.as_view()),

    path("owners/",include("owners.urls"))
]+router.urls