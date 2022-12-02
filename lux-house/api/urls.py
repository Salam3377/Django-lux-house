from django.urls import path , include
from .views.mango_views import Mangos, MangoDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.menu_views import ProductView, ProductDetailView
from .views.cart_views import CartView, CartDetailView


urlpatterns = [
  	# Restful routing
    path('mangos/', Mangos.as_view(), name='mangos'),
    path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),

    path('product/', ProductView.as_view(), name='product' ),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product' ),
    
    path('cart/', CartView.as_view(), name='cart' ),
    path('cart/<int:pk>/', CartDetailView.as_view(), name='cart' ),

]
