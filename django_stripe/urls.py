from django.urls import path
from .views import ProductPreview, CreateStripeCheckoutSession

urlpatterns = [
    path('product/<int:pk>/', ProductPreview.as_view(), name="product"),
    path('create-checkout-session/<pk>/',CreateStripeCheckoutSession.as_view(), name='checkout_session')
]
