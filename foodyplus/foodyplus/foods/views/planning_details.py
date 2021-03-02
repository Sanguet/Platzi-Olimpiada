# Django REST Framework
from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404

# Models
from foodyplus.foods.models import Planning, PlanningDetail

# Serializers
from foodyplus.foods.serializers import PlanningDetailModelSerializer

# Permissions
from foodyplus.users.permissions import IsUserAdmin, IsAccountOwner
from rest_framework.permissions import IsAuthenticated, AllowAny


class PlanningDetailViewSet(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    """PlanningDetail view set"""

    serializer_class = PlanningDetailModelSerializer

    def dispatch(self, request, *args, **kwargs):
        """Verificamos que la venta exista"""
        planning = kwargs['planning_pk']
        self.planning = get_object_or_404(Planning, id=planning)
        return super(PlanningDetailViewSet, self).dispatch(request, *args, **kwargs)

    def get_serializer_context(self):
        """ Añadimos planning al contexto del serializer"""
        context = super(PlanningDetailViewSet, self).get_serializer_context()
        context['planning'] = self.planning
        return context

    def get_permissions(self):
        """Asigna permisos dependiendo de la accion"""
        permissions = [AllowAny]
        if self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            permissions = [IsAuthenticated, IsAccountOwner]
        elif self.action in ['list', 'create']:
            permissions = [IsAuthenticated, IsUserAdmin]
        return [p() for p in permissions]

    def get_queryset(self):
        """Retorna los detalles de la venta"""
        queryset = PlanningDetail.objects.filter(
            planning_id=self.planning,
            is_active=True,
        )
        return queryset
