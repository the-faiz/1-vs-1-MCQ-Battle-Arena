from rest_framework import serializers

class OptionSerializer(serializers.Serializer):
    body = serializers.CharField(max_length=1000)
    is_correct = serializers.BooleanField()

class MCQSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    body = serializers.CharField(max_length=2000)
    explanation = serializers.CharField(max_length=2000)
    options = OptionSerializer(many=True)
