# Django REST Framework
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed

# Serializers
from foodyplus.foods.serializers import SaleModelSerializer, TrackingSerializer

# Models
from foodyplus.foods.models import Sale

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Permissions
from foodyplus.foods.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated, AllowAny


class SaleViewSet(viewsets.ModelViewSet):

    serializer_class = SaleModelSerializer

    # Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('detail', 'payment_method', 'user',
                     'total', 'comment', 'shipping_info', 'discount', 'delivery_date', 'steps', 'tracking_code')
    ordering_fields = ('detail', 'payment_method', 'user',
                       'shipping_info', 'discount', 'delivery_date', 'steps', 'tracking_code')
    ordering = ()
    filter_fields = ('detail', 'payment_method', 'user',
                     'total', 'comment', 'shipping_info', 'discount', 'delivery_date', 'steps', 'tracking_code')

    def get_permissions(self):
        """Asignamos los permisos en base a las acciones."""
        permissions = [IsAuthenticated, IsAdminUser]
        if self.action in ['create', 'tracking']:
            permissions = [AllowAny]
        return [permission() for permission in permissions]

    def get_queryset(self):
        user = self.request.user
        queryset = Sale.objects.all()
        if user.account_type == 'A':
            queryset = queryset.filter(is_active=True)
        else:
            queryset = queryset.filter(user=user, is_active=True)

        return queryset

    def perform_destroy(self, instance):
        """Solo desactivamos la venta"""
        # Delete
        instance.is_active = False
        instance.save()

    def update(self, request, pk=None):
        raise MethodNotAllowed('UPDATE')

    @action(detail=False, methods=["post"])
    def tracking(self, request):
        """Seguimiento de la venta"""
        serializer = TrackingSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        sale_step = serializer.save()
        data = {
            'message': 'Venta recuperada con exito!',
            'step': sale_step
        }
        return Response(data, status=status.HTTP_200_OK)
