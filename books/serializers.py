from rest_framework import serializers

from books.models import *


class BookSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Books
        fields = "__all__"


class GenresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = "__all__"


class AuthorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Authors
        fields = "__all__"