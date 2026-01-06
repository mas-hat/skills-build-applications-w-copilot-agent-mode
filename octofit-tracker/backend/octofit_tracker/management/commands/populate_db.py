from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        users = [
            User(email='ironman@marvel.com', username='Iron Man', team=marvel, is_superhero=True),
            User(email='captain@marvel.com', username='Captain America', team=marvel, is_superhero=True),
            User(email='batman@dc.com', username='Batman', team=dc, is_superhero=True),
            User(email='superman@dc.com', username='Superman', team=dc, is_superhero=True),
        ]
        User.objects.bulk_create(users)

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        workouts = [
            Workout(name='Pushups', description='Upper body', difficulty='Easy'),
            Workout(name='Situps', description='Core', difficulty='Medium'),
            Workout(name='Running', description='Cardio', difficulty='Hard'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        user_objs = list(User.objects.all())
        workout_objs = list(Workout.objects.all())
        activities = [
            Activity(user=user_objs[0], workout=workout_objs[0], duration=30, calories_burned=200),
            Activity(user=user_objs[1], workout=workout_objs[1], duration=20, calories_burned=150),
            Activity(user=user_objs[2], workout=workout_objs[2], duration=40, calories_burned=300),
            Activity(user=user_objs[3], workout=workout_objs[0], duration=25, calories_burned=180),
        ]
        Activity.objects.bulk_create(activities)

        self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
        Leaderboard.objects.create(team=marvel, total_points=350)
        Leaderboard.objects.create(team=dc, total_points=480)

        self.stdout.write(self.style.SUCCESS('Ensuring unique index on email field for users...'))
        with connection.cursor() as cursor:
            cursor.execute('''
                db = connection.db.client.get_database('octofit_db')
                db.users.create_index([('email', 1)], unique=True)
            ''')

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
