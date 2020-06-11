from django.apps import AppConfig


class DjangoTicketsConfig(AppConfig):
    name = 'django_tickets_2'

    def ready(self, *args, **kwargs):
        import django_tickets_2.signals
