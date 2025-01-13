import random
from django.utils.translation import gettext_lazy
from weblate.checks.base import TargetCheck, SourceCheck


class ExampleCheck(TargetCheck):
    """Check whether "foo" string is not present in the target."""

    # Used as identifier for check, should be unique
    # Has to be shorter than 50 chars
    check_id = "foo"

    # Short name used to display failing check
    name = gettext_lazy("Foo check")

    # Description for failing check
    description = gettext_lazy("Your translation is foo")

    def check_single(self, source, target, unit):
        """Real check code."""
        return "foo" in target

class RandomFailTargetCheck(TargetCheck):
    # Eindeutige Check-ID, die kürzer als 50 Zeichen sein sollte
    check_id = "random_fail_target"

    # Name für diesen Check, wird in Fehlermeldungen verwendet
    name = gettext_lazy("Zufälliger Fehler-Check für Zieltexte")

    # Ausführlichere Erklärung zum Check
    description = gettext_lazy("Wirft gelegentlich zufällig einen Fehler")

    def check_single(self, source, target, unit):
        """
        Diese Methode entscheidet, ob ein Fehler gemeldet wird oder nicht.
        Sie zieht einen Zufallswert, und wenn dieser unter 0.5 liegt,
        wird 'random_fail' als Fehler gemeldet.
        """
        # Ziehe eine Zufallszahl zwischen 0 und 1
        zufallswert = random.random()

        # Falls der Wert < 0.5, wird ein Fehler gemeldet
        if zufallswert < 0.5:
            # Dieser Wert wird als String in der Fehlermeldung angezeigt
            return True

        # Ansonsten wird kein Fehler gemeldet
        return False

class RandomFailSourceCheck(SourceCheck):
    # Eindeutige Check-ID, die kürzer als 50 Zeichen sein sollte
    check_id = "random_fail_source"

    # Name für diesen Check, wird in Fehlermeldungen verwendet
    name = gettext_lazy("Zufälliger Fehler-Check für Quelltexte")

    # Ausführlichere Erklärung zum Check
    description = gettext_lazy("Wirft gelegentlich zufällig einen Fehler im Quelltext")

    def check_single(self, source, target, unit):
        """
        Diese Methode entscheidet, ob ein Fehler gemeldet wird oder nicht.
        Sie zieht einen Zufallswert, und wenn dieser unter 0.5 liegt,
        wird 'random_fail_source' als Fehler gemeldet.
        """
        # Ziehe eine Zufallszahl zwischen 0 und 1
        zufallswert = random.random()

        # Falls der Wert < 0.5, wird ein Fehler gemeldet
        if zufallswert < 0.5:
            # Dieser Wert wird als String in der Fehlermeldung angezeigt
            return True

        # Ansonsten wird kein Fehler gemeldet
        return False
    
    def check_source_unit(self, sources, unit):
        """
        Diese Methode entscheidet, ob ein Fehler gemeldet wird oder nicht.
        Sie zieht einen Zufallswert, und wenn dieser unter 0.5 liegt,
        wird 'random_fail_source' als Fehler gemeldet.
        """
        # Ziehe eine Zufallszahl zwischen 0 und 1
        zufallswert = random.random()

        # Falls der Wert < 0.5, wird ein Fehler gemeldet
        if zufallswert < 0.5:
            # Dieser Wert wird als String in der Fehlermeldung angezeigt
            return True

        # Ansonsten wird kein Fehler gemeldet
        return False