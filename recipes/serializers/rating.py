from rest_framework import serializers
from recipes.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # show username/email
    recipe = serializers.StringRelatedField(read_only=True)  # show recipe title

    class Meta:
        model = Rating
        fields = ["id", "user", "recipe", "score", "review", "created_at"]
        read_only_fields = ["id", "user", "recipe", "created_at"]
