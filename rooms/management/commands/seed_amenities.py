from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    help = "This command is to create new amenities"

    # def add_arguments(self, parser):
    #     parser.add_argument("--times", help="This for multiplation")

    def handle(self, *args, **options):
        amenities = [
            "Toilet paper",
            "Soap for hands and body",
            "One towel per guest",
            "Linens for each bed",
            "One pillow per guest",
            "Cleaning supplies",
            "Free parking",
            "Wifi",
            "TV",
            "Heater, air conditioning",
            "Hair dryer",
            "Breakfast",
            "Carbon monoxide alarm",
            "Smoke alarm",
            "Fire extinguisher",
            "First-aid kit",
            "Emergency plan and local numbers",
            "A crib and high chair",
            "A bathtub",
            "Air conditioning",
            "A washer and/or dryer",
            "Extra cleaning supplies",
            "Furniture covers",
            "Bowls for pet food and water",
            "Towels to wipe off paws at the door",
            "Step-free entryway",
            "Wide entrances (at least 32”)",
            "Wide hallways (at least 36”)",
            "Accessible bathroom",
            "Extra toilet paper, linens, and towels",
            "Basic toiletries like shampoo and conditioner",
            "Dish soap and cleaning supplies",
            "Dining basics like a coffee maker, cooking utensils, dishes",
            "Wine glasses",
            "Basic cooking supplies like salt, pepper, and oil",
            "Coffee, tea",
            "Light breakfast or snacks",
            "Hangers",
            "Adapters and chargers",
            "Fast and reliable wifi",
            "Laptop-friendly workspace",
            "Good lighting",
            "Fully equipped kitchens",
            "Office supplies",
        ]
        for amenity in amenities:
            Amenity.objects.create(name=amenity)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))
