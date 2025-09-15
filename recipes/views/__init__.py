from .category_views import CategoryCreateAPIView, CategoryListAPIView, CategoryUpdateAPIView, CategoryDeleteAPIView, CategoryDetailAPIView

from .recipe_views import (
    RecipeCreateAPIView,
    RecipeDetailAPIView,
    RecipeListAPIView,
    RecipeUpdateAPIView,
    RecipeDeleteAPIView
)

from .comment_views import (
    CommentListAPIView,
    CommentCreateAPIView,
    CommentDetailAPIView,
    CommentUpdateAPIView,
    CommentDeleteAPIView,
)

from .rating import RatingCreateView, RecipeRatingListView

__all__ = [
    "CategoryCreateAPIView",
    "CategoryListAPIView",
    "CategoryUpdateAPIView",
    "CategoryDeleteAPIView",
    "CategoryDetailAPIView",

    "RecipeCreateAPIView",
    "RecipeDetailAPIView",
    "RecipeListAPIView",
    "RecipeUpdateAPIView",
    "RecipeDeleteAPIView",

    "CommentListAPIView",
    "CommentCreateAPIView",
    "CommentDetailAPIView",
    "CommentUpdateAPIView",
    "CommentDeleteAPIView",

    "RatingCreateView",
    "RecipeRatingListView",
]