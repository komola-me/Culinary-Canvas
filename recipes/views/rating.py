from rest_framework import generics, permissions
from recipes.models import Rating
from recipes.serializers import RatingSerializer


class RatingCreateView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        recipe_id = self.request.data.get("recipe_id")
        serializer.save(user=self.request.user, recipe_id=recipe_id)


class RecipeRatingListView(generics.ListAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        recipe_id = self.kwargs["recipe_id"]
        return Rating.objects.filter(recipe_id=recipe_id)