from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
            User.objects.create(name='Thor', email='thor@marvel.com', team=marvel),
            User.objects.create(name='Superman', email='superman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30)
        Activity.objects.create(user=users[1], type='Cycling', duration=45)
        Activity.objects.create(user=users[2], type='Swimming', duration=60)
        Activity.objects.create(user=users[3], type='Running', duration=25)
        Activity.objects.create(user=users[4], type='Cycling', duration=40)
        Activity.objects.create(user=users[5], type='Swimming', duration=55)

        # Create workouts
        workout1 = Workout.objects.create(name='Pushups', description='Upper body strength')
        workout2 = Workout.objects.create(name='Squats', description='Lower body strength')
        workout1.suggested_for.add(marvel, dc)
        workout2.suggested_for.add(marvel, dc)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=140)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
