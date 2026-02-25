from core.services import mon_traitement
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Exécute le traitement toutes les 10 minutes"

    def handle(self, *args, **kwargs):
        data = mon_traitement()
        print("Data :", data)