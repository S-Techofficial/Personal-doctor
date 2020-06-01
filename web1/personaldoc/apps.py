from django.apps import AppConfig


class PersonaldocConfig(AppConfig):
    name = 'personaldoc'

    def ready(self):
        import personaldoc.signals

