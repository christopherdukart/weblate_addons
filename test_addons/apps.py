# from django.apps import AppConfig
# from django.utils.translation import gettext_lazy as _
#
# class TestingPluginConfig(AppConfig):
#     name = 'testing_plugin'
#     label = "test_addons"
#     verbose_name = _('Testing Plugin')
#
#     # def ready(self):
#     #     from weblate.test_addons.registry import ADDONS
#     #     from .testing_plugin import TestingPlugin
#     #     ADDONS.register(TestingPlugin)

from django.apps import AppConfig


class AddonsConfig(AppConfig):
    name = "test_addons"
    label = "test_addons"
    verbose_name = "Add-ons"