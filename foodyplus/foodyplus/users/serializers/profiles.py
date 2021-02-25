# Django REST Framework
from rest_framework import serializers

# Models
from foodyplus.users.models import Profile


class ProfileModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    class Meta:
        """Meta class."""

        model = Profile
        fields = (
            'id',
            'first_name', 'last_name',
            'picture',
            'biografy', 'points',
        )

        read_only_fields = (
            'points', 'id'
        )
