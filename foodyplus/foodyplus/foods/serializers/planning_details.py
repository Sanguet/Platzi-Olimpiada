# Django REST Framework
from rest_framework import serializers

# Model
from foodyplus.foods.models import PlanningDetail

# Validators
from foodyplus.foods.validators import Validators


class PlanningDetailModelSerializer(serializers.ModelSerializer):
    """Modelo serializer del circulo"""

    recipe = serializers.CharField()
    day = serializers.IntegerField(min_value=0)

    class Meta:
        """Meta class"""

        model = PlanningDetail
        fields = (
            'id',
            'planning', 'recipe',
            'day', 'time'
        )
        read_only_fields = (
            'id', 'planning'
        )

    def validate_recipe(self, data):
        """Validador individual del recipe"""
        self.context['recipe'] = Validators.recipe(pk=data)
        return data

    def create(self, data):
        """Creacion del detalle de la planificacion"""
        # Obtenemos los datos del contexto
        planning = self.context['planning']
        recipe = self.context['recipe']
        data.pop('recipe')

        # Creamos el detalle
        planning_detail = PlanningDetail.objects.create(
            planning=planning,
            recipe=recipe,
            **data
        )

        return planning_detail

    def update(self, instance, data):
        """Update del detalle de la planificacion"""
        # Validamos que el dato existe, sino lo ponemos como estaba
        try:
            self.context['recipe']
        except KeyError:
            self.context['recipe'] = instance.recipe

        instance.recipe = self.context['recipe']
        instance.day = data.get('day', instance.day)
        instance.time = data.get('time', instance.time)

        return instance
