from random import choice, randint
from django.core.management.base import BaseCommand
from django_seed import Seed
from books.models import Book
from categories.models import Category
from people.models import Person


class Command(BaseCommand):

    help = "This command seeds books"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            help="How many books do you want to create?",
            default=10)

    def handle(self, *args, **options):
        total = int(options.get('total'))
        categories = Category.objects.all()
        writers = Person.objects.filter(kind=Person.KIND_WRITER)
        seeder = Seed.seeder()
        seeder.add_entity(
            Book, total, {
                "title":lambda x: seeder.faker.text(max_nb_chars=randint(7,25)),
                "year": lambda x: seeder.faker.year(),
                "rating": lambda x: randint(1, 5),
                "category": lambda x: choice(categories),
                "cover_image":lambda x: f"book/{randint(1,17)}.webp",
                "writer": lambda x: choice(writers),
            })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{total} books created!'))
