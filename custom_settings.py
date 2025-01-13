from weblate.settings_docker import *

WEBLATE_ADDONS += ("test_addons.example.ExampleAddon",)

CHECK_LIST += ("test_check.example.ExampleCheck",
               "test_check.example.RandomFailTargetCheck",
               "test_check.example.RandomFailSourceCheck")