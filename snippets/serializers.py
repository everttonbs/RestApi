
from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, Profundidade


class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        
        #fields = ('id', 'title', 'code', 'linenos',
                  #'language', 'style', )

        #fields = ('id', 'well_name', 'Prof', 'Gamma', 'SUTT')
        fields = ('id', 'well_name', 'Prof')
      

    class Meta_2:
        model = Profundidade

        fields = ('id', 'prof_P')


        



                  