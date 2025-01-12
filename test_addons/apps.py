from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class TestAddonsConfig(AppConfig):
    name = "test_addons"
    label = "test_addons"
    verbose_name = _("Testing Add-ons")

    def ready(self):
        from weblate.addons.models import ADDONS
        from .example import ExampleAddon
        #ADDONS.settings.WEBLATE_ADDONS += ('test_addons.example.ExampleAddon',)
        ADDONS.register(ExampleAddon)