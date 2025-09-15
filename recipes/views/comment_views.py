from rest_framework import generics, permissions
from recipes.models import Comment
from recipes.serializers import CommentSerializer
from recipes.permissions import IsOwnerOrReadOnly
from recipes.models import Recipe

class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        recipe_id = self.kwargs["recipe_id"]
        return Comment.objects.filter(recipe_id=recipe_id, parent=None, is_active=True)


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        recipe_id = self.kwargs["recipe_id"]
        recipe = Recipe.objects.get(pk=recipe_id)
        serializer.save(user=self.request.user, recipe=recipe)


class CommentDetailAPIView(generics.RetrieveAPIView):
    queryset = Comment.objects.filter(is_active=True)
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]


class CommentUpdateAPIView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CommentDeleteAPIView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()