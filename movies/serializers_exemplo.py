from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie

# from genres.models import Genre
# from actors.models import Actor


# class MovieSerialier(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField()
#     genre = serializers.PrimaryKeyRelatedField(
#         queryset = Genre.objects.all()
#     )
#     release_date = serializers.DateField()
#     actors = serializers.PrimaryKeyRelatedField(
#         queryset = Actor.objects.all(),
#         many=True,
#     )
#     resume = serializers.CharField()


# read_only=True significa que este campo e apenas de leitura.
class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    # Esta função tem que começar com get_ para que o Django entenda que e um campo calculado.
    # obj seria cada movie cadastrado, linha por linha.

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None

    # Esta função tem que começar com get_ para que o Django entenda que e um campo calculado.
    # obj seria cada movie cadastrado, linha por linha.

    # def get_rate(self, obj):
    #     reviews = obj.reviews.all()

    #     if reviews:
    #         sum_reviews = 0

    #         for review in reviews:
    #             sum_reviews += review.stars

    #         reviews_count = reviews.count()

    #         return round(sum_reviews / reviews_count, 1)

    #     return None

    # Esta função tem que começar com validate_ para que o Django entenda a validação.

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError(
                'A data de lançamento não pode ser anterior a 1900'
            )
        return value

    # Esta função tem que começar com validate_ para que o Django entenda a validação.
    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError(
                'Resumo não deve ser maior que 500 caracteres.'
            )
        return value
