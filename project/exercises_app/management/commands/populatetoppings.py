from django.core.management.base import BaseCommand

from exercises_app.models import Toppings


class Command(BaseCommand):
    help = 'Populates toppings model'
    def handle(self, *args, **options):
        Toppings.objects.create(name='oliwki', price=0.3)
        Toppings.objects.create(name='pomidory', price=1)
        Toppings.objects.create(name='dodatkowy ser', price=0.3)
        Toppings.objects.create(name='anchovies', price=12.3)
        Toppings.objects.create(name='cebula', price=3.3)