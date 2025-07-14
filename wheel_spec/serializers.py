from rest_framework import serializers
from .models import WheelSpecification
import datetime

class WheelSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelSpecification
        fields = '__all__'

    def validate_formNumber(self, value):
        if not value.strip():
            raise serializers.ValidationError("Form number cannot be blank.")
        return value

    def validate_submittedBy(self, value):
        if not value.strip():
            raise serializers.ValidationError("Submitted By is required.")
        return value

    def validate_submittedDate(self, value):
        if value > datetime.date.today():
            raise serializers.ValidationError("Submitted date cannot be in the future.")
        return value

    def validate_fields(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError("Fields must be a JSON object.")
        if not value:
            raise serializers.ValidationError("Fields cannot be empty.")
        return value
