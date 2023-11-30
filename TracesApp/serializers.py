"""Serializers for TracesApp"""

from rest_framework import serializers
from .models import Logs


class LogsSerializer(serializers.ModelSerializer):
    """Serializes `Logs` model object to JSON"""

    class Meta:
        """Serializer's metadata"""

        model = Logs
        read_only_fieLds = ("id",)
