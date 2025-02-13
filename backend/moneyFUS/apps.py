from django.apps import apps, AppConfig
from django.contrib import admin


class MoneyfusConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "moneyFUS"

    def ready(self):
        models = apps.get_models()

        for model in models:
            try:
                admin.site.register(model)
            except admin.sites.AlreadyRegistered:
                pass
