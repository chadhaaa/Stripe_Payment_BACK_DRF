from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from django.views.decorators.csrf import csrf_exempt
from .models import Product
from .serializers import ProductSerializer
from rest_framework import permissions
from rest_framework.response import Response
from django.conf import settings 
import stripe 

stripe.api_key = settings.STRIPE_SECRET_KEY 
API_URL="http/locahost:8000"

class ProductPreview(RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes =  [permissions.AllowAny]
    queryset = Product.objects.all()

class CreateStripeCheckoutSession(APIView):
    def post(self, request, *args, **kwargs):
        prod_id = self.kwargs['pk']
        try:
            product = Product.objects.get(id = prod_id)
            checkout_session = stripe.checkout.Session.create(
                line_items = [
                    {
                        'price_data' : {
                            'currency' : 'usd',
                            'unit_amount' : int(product.price) *100,
                            'product_data' : {
                                'name' : product.name,
                                'images':[f"{API_URL}/{product.product_image}"]
                            }

                        },
                        'quantity' : 1 
                    }
                ],

                metadata = {
                    'product_id': product.id 
                },
                mode = 'payment', 
                success_url = settings.SITE_URL + '?success=true', 
                cancel_url = settings.SITE_URL + '?canceled=true'


            )
            return redirect(checkout_session.url)

        except Exception as e:
            return Response({'msg' : 'Something just went wrong', 'error': str(e)}, status=500)