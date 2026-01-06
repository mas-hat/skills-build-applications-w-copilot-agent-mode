from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Marvel", description="Marvel team")
        self.assertEqual(str(team), "Marvel")

    def test_create_user(self):
        team = Team.objects.create(name="DC", description="DC team")
        user = User.objects.create(email="batman@dc.com", username="batman", team=team, is_superhero=True)
        self.assertEqual(str(user), "batman")

    def test_create_workout(self):
        workout = Workout.objects.create(name="Pushups", description="Upper body", difficulty="Easy")
        self.assertEqual(str(workout), "Pushups")

    def test_create_activity(self):
        team = Team.objects.create(name="Marvel2", description="Marvel2 team")
        user = User.objects.create(email="spiderman@marvel.com", username="spiderman", team=team, is_superhero=True)
        workout = Workout.objects.create(name="Situps", description="Core", difficulty="Medium")
        activity = Activity.objects.create(user=user, workout=workout, duration=30, calories_burned=200)
        self.assertIn("spiderman", str(activity))

    def test_create_leaderboard(self):
        team = Team.objects.create(name="DC2", description="DC2 team")
        leaderboard = Leaderboard.objects.create(team=team, total_points=100)
        self.assertIn("DC2", str(leaderboard))
