from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Register your models here.
from django.contrib import admin
from .models import Recipe, Category, Comment, Rating
from modeltranslation.admin import TranslationAdmin


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id",
        "title",
        "author",
        "category",
        "is_draft",
        "created_at",)
    list_display_links = ("id", "title",)
    search_fields = ("title", "content",)

    fieldsets = (
        (
            _("Main"),
            {
                "fields": (
                    "author",
                    "slug",
                    "image",
                    "category",
                    "is_draft",
                ),
            },
        ),
        (
            _("Uzbek"),
            {
                "fields": (
                    "title_uz",
                    "description_uz",
                    "ingredients_uz",
                    "instructions_uz",
                ),
            },
        ),
        (
            _("English"),
            {
                "fields": (
                    "title_en",
                    "description_en",
                    "ingredients_en",
                    "instructions_en",
                ),
            },
        ),
        (
            _("Russian"),
            {
                "fields": (
                    "title_ru",
                    "description_ru",
                    "ingredients_ru",
                    "instructions_ru",
                ),
            },
        ),
    )
    readonly_fields = ("slug",)


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = (
        "id",
        "name",
    )
    list_display_links = ("id", "name",)
    search_fields = ("name",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "recipe", "is_active",)
    list_display_links = ("id", "user", "recipe",)
    list_filter = ("is_active",)
    search_fields = ("user", "post",)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("recipe", "user", "score", "review", "created_at",)
    list_filter = ("score", "created_at",)
    search_fields = ("recipe__title", "user__email",)