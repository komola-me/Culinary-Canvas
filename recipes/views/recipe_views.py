from rest_framework import generics, permissions
import logging
from rest_framework.exceptions import PermissionDenied

from recipes.models import Recipe
from recipes.serializers import RecipeSerializer
from recipes.permissions import IsOwnerOrReadOnly

logger = logging.getLogger("culinary")

class RecipeListAPIView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.AllowAny]


class RecipeCreateAPIView(generics.CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        recipe = serializer.save(author=self.request.user)
        logger.info(f"New recipe created: {recipe.title} by {self.request.user.email}")


class RecipeDetailAPIView(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.AllowAny]


class RecipeUpdateAPIView(generics.UpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            logger.warning(
                f"Unauthorized access: User {self.request.user.email} tried to edit Recipe {serializer.instance.id}"
            )
            raise PermissionDenied("You cannot edit someone else’s recipe.")
        serializer.save()


class RecipeDeleteAPIView(generics.DestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsOwnerOrReadOnly]