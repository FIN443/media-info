from random import choice, randint,choices
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from movies.models import Movie
from categories.models import Category
from people.models import Person


class Command(BaseCommand):

    help = "This command seeds movies"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            help="How many movies do you want to create?",
            default=10)

    def handle(self, *args, **options):
        total = int(options.get('total'))
        categories = Category.objects.all()
        directors = Person.objects.filter(kind=Person.KIND_DIRECTOR)
        cast = Person.objects.filter(kind='actor')
        seeder = Seed.seeder()
        seeder.add_entity(
            Movie, total, {
                "title":lambda x: seeder.faker.text(max_nb_chars=randint(7,25)),
                "year": lambda x: seeder.faker.year(),
                "rating": lambda x: randint(1, 5),
                "cover_image":lambda x: f"movie/{randint(1,25)}.jpg",
                "category": lambda x: choice(categories),
                "director": lambda x: choice(directors),
            })
        created = seeder.execute()
        cleaned = flatten(list(created.values()))
        for pk in cleaned:
          movie = Movie.objects.get(pk=pk)
          cast = choices(cast,k=randint(13,43))
          for c in cast:
            magic_number = randint(1,31)
            if magic_number % 2 == 0:
              movie.cast.add(c)
        self.stdout.write(self.style.SUCCESS(f'{total} movies created!'))

