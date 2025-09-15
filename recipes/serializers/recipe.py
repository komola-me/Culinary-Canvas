from rest_framework import serializers

from recipes.models import Recipe, Rating
from users.models import User

class RatingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Rating
        fields = ["id", "user", "score", "review", "created_at"]
        read_only_fields = ["id", "user", "created_at"]


class RecipeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.email")
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = [
            "id", "author", "category", "title", "description",
            "ingredients", "instructions", "image",
            "is_draft", "created_at", "updated_at", "average_rating",
        ]
        read_only_fields = ["id", "author", "created_at", "updated_at", "average_rating"]

    def get_average_rating(self, obj):
        ratings = obj.ratings.all()
        if ratings.exists():
            return sum(r.score for r in ratings) / ratings.count()

        return None