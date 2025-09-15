from rest_framework import serializers

from recipes.models import Comment
from users.models import User

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    recipe = serializers.PrimaryKeyRelatedField(read_only=True)
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id", "content", "user", "recipe",
            "parent", "replies", "is_active",
            "created_at", "updated_at"
        ]
        read_only_fields = ["id", "user", "recipe", "created_at", "updated_at", "replies"]

    def get_replies(self, obj):
        # recursive replies
        return CommentSerializer(obj.replies.all(), many=True).data