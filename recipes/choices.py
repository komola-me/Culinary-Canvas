from django.db import models
from django.utils.translation import gettext_lazy as _

class ScoreChoices(models.IntegerChoices):
        ONE = 1, _("1 - Very Bad")
        TWO = 2, _("2 - Bad")
        THREE = 3, _("3 - Okay")
        FOUR = 4, _("4 - Good")
        FIVE = 5, _("5 - Excellent")