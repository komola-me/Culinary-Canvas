from modeltranslation.translator import TranslationOptions
from modeltranslation import translator

from recipes.models import Recipe, Category

@translator.register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name", )


@translator.register(Recipe)
class RecipeTranslationOptions(TranslationOptions):
    fields = ("title", "description", "ingredients", 'instructions',)
