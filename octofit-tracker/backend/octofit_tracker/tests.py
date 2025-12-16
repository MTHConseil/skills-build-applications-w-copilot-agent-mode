from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.assertEqual(str(team), 'Marvel')

    def test_user_creation(self):
        team = Team.objects.create(name='DC', description='DC Team')
        user = User.objects.create(email='batman@dc.com', username='batman', team=team)
        self.assertEqual(str(user), 'batman')

    def test_activity_creation(self):
        team = Team.objects.create(name='X-Men', description='X-Men Team')
        user = User.objects.create(email='logan@xmen.com', username='wolverine', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=30)
        self.assertEqual(str(activity), 'wolverine - run')

    def test_workout_creation(self):
        team = Team.objects.create(name='Avengers', description='Avengers Team')
        workout = Workout.objects.create(name='Cardio', description='Cardio workout')
        workout.suggested_for.add(team)
        self.assertEqual(str(workout), 'Cardio')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Justice League', description='Justice League Team')
        user = User.objects.create(email='clark@dc.com', username='superman', team=team)
        leaderboard = Leaderboard.objects.create(user=user, score=100, rank=1)
        self.assertEqual(str(leaderboard), 'superman - 100')
