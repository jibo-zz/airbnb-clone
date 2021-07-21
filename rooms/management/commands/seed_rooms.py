import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command is to create new rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many rooms do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_user = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_user),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 500),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        create_photos = seeder.execute()
        created_flatten = flatten(list(create_photos.values()))
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()
        for id in created_flatten:
            room = room_models.Room.objects.get(id=id)
            for n in range(3, random.randint(10, 30)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"/room_photos/{random.randint(1, 31)}.webp",
                )
            for amenity in amenities:
                sweet_number = random.randint(0, 12)
                if sweet_number % 2 == 0:
                    room.amenities.add(amenity)
            for facility in facilities:
                sweet_number = random.randint(0, 6)
                if sweet_number % 2 == 0:
                    room.facilities.add(facility)
            for rule in rules:
                sweet_number = random.randint(0, 3)
                if sweet_number % 2 == 0:
                    room.house_rules.add(rule)
        self.stdout.write(self.style.SUCCESS(f"{number} Rooms created!"))
