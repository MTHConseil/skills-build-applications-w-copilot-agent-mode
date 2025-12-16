from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data (delete one by one for Djongo compatibility)
        for obj in Leaderboard.objects.all():
            obj.delete()
        for obj in Activity.objects.all():
            obj.delete()
        for obj in User.objects.all():
            obj.delete()
        for obj in Team.objects.all():
            obj.delete()
        for obj in Workout.objects.all():
            obj.delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Team')
        dc = Team.objects.create(name='DC', description='DC Team')

        # Users
        ironman = User.objects.create(email='ironman@marvel.com', username='Iron Man', team=marvel)
        spiderman = User.objects.create(email='spiderman@marvel.com', username='Spider-Man', team=marvel)
        batman = User.objects.create(email='batman@dc.com', username='Batman', team=dc)
        superman = User.objects.create(email='superman@dc.com', username='Superman', team=dc)

        # Activities
        Activity.objects.create(user=ironman, type='run', duration=30)
        Activity.objects.create(user=spiderman, type='cycle', duration=45)
        Activity.objects.create(user=batman, type='swim', duration=25)
        Activity.objects.create(user=superman, type='run', duration=60)

        # Workouts
        w1 = Workout.objects.create(name='Cardio Blast', description='High intensity cardio')
        w2 = Workout.objects.create(name='Strength Training', description='Build muscle')
        w1.suggested_for.add(marvel, dc)
        w2.suggested_for.add(dc)

        # Leaderboard
        Leaderboard.objects.create(user=ironman, score=100, rank=1)
        Leaderboard.objects.create(user=spiderman, score=80, rank=2)
        Leaderboard.objects.create(user=batman, score=90, rank=1)
        Leaderboard.objects.create(user=superman, score=70, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db has been populated with test data.'))
