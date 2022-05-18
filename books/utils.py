from django.shortcuts import get_object_or_404
from .models import Books


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        return context