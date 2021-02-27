# Django REST Framework
from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import NotFound

# Models
from foodyplus.foods.models import Sale, SaleDetail

# Permissions
from rest_framework.permissions import IsAuthenticated
from foodyplus.foods.permissions import IsAdminUser

# Serializers
from foodyplus.foods.serializers import SaleDetailModelSerializer


class SaleDetailViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    """SaleDetail view set"""

    serializer_class = SaleDetailModelSerializer

    def dispatch(self, request, *args, **kwargs):
        """Verificamos que la venta exista"""
        sale = kwargs['sale_pk']
        self.sale = get_object_or_404(Sale, id=sale)
        return super(SaleDetailViewSet, self).dispatch(request, *args, **kwargs)

    def get_serializer_context(self):
        """ Añadimos sale al contexto del serializer"""
        context = super(SaleDetailViewSet, self).get_serializer_context()
        context['sale'] = self.sale
        return context

    def get_permissions(self):
        """Asignamos los permisos en base a las acciones."""
        permissions = [IsAuthenticated, IsAdminUser]
        if self.action in ['create', 'delete', 'list']:
            permissions = []
        return [permission() for permission in permissions]

    def get_queryset(self):
        """Retorna los detalles de la venta"""
        queryset = SaleDetail.objects.filter(
            sale_id=self.sale,
            is_active=True,
        )
        if queryset.count() == 0:
            raise NotFound("No se encontro un detalle de venta para ese usuario y venta")
        return queryset
