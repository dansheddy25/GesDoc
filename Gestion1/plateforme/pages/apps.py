from django.apps import AppConfig


class PagesConfig(AppConfig):
    name = 'pages'


    def ready(self):
        import pages.signals
