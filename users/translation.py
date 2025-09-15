from modeltranslation import translator

from .models import User

@translator.register(User)
class UserTranslationOptions(translator.TranslationOptions):
    fields = ('first_name', 'last_name',)
