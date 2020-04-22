from haystack import indexes

from .models import Movie


class MovieIndex(indexes.SearchIndex,indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True)



    def get_model(self):

        return Movie

    def index_queryset(self, using=None):

        return self.get_model().objects.all()