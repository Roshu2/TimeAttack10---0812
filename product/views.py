from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models.query_utils import Q
from .models import Product, Subscribe
from product.serializers import ProductSerializer, SubscribeSerializer
import datetime


class ProductView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        products = Product.objects.filter(is_active=True)
        
        if products.exists():
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"msg": "조회 가능한 상품이 없습니다."},
            status=status.HTTP_404_NOT_FOUND
            )
    
    def post(self, request, product_id):
        try:
            user = request.user
            product = Product.objects.get(id=product_id)
            year = datetime.timedelta(days=365)
            subscribe_end = datetime.datetime.now() + year
            
            product_data = {
                "user": user,
                "product": product,
                "subscribe_end": subscribe_end
            }
            
            serializer = SubscribeSerializer(data=product_data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"msg": "상품 구독이 완료되었습니다.", "subscribe_info": serializer.data},
                    status=status.HTTP_200_OK
                )
            return Response(
                {"msg": "유효하지 않은 요청입니다."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        except Product.DoesNotExist:
            return Response(
                {"msg": "상품이 더이상 존재하지 않거나, 활성화 되지 않았습니다."},
                status=status.HTTP_404_NOT_FOUND
            )
            
        