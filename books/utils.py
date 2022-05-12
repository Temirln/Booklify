class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        # context = super().get_context_data(**kwargs)
        # context['title'] = context['book']
        return context