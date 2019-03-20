
# Create your models here.
from django.db import models

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Profundidade(models.Model):
    prof_P = models.DecimalField(max_digits = 5, decimal_places = 2)

    class Meta_2:
        ordering = ('created1',)

    def __str__(self):
        return self.prof_P





class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    well_name = models.CharField(max_length=100, blank=True, default='')
    #Prof = models.DecimalField(max_digits = 5, decimal_places = 2)
    #Prof = models.ManyToManyField(Profundidade)
    Prof = models.ForeignKey(Profundidade, on_delete=models.CASCADE)

    #Gamma = models.DecimalField(max_digits = 5, decimal_places = 2)
    #SUTT = models.DecimalField(max_digits = 5, decimal_places = 2)


    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.well_name
        







        