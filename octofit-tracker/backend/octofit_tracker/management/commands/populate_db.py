from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data safely
        User.objects.filter(pk__isnull=False).delete()
        Team.objects.filter(pk__isnull=False).delete()
        Activity.objects.filter(pk__isnull=False).delete()
        Leaderboard.objects.filter(pk__isnull=False).delete()
        Workout.objects.filter(pk__isnull=False).delete()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thor', password='thundergodpassword'),
            User(email='metalgeek@mhigh.edu', name='Tony Stark', password='metalgeekpassword'),
            User(email='zerocool@mhigh.edu', name='Zero Cool', password='zerocoolpassword'),
            User(email='crashoverride@hmhigh.edu', name='Crash Override', password='crashoverridepassword'),
            User(email='sleeptoken@mhigh.edu', name='Sleep Token', password='sleeptokenpassword'),
        ]
        # Save users individually to ensure they are persisted in the database
        for user in users:
            user.save()

        # Create teams
        team1 = Team(name='Blue Team')
        team2 = Team(name='Gold Team')
        team1.save()
        team2.save()

        # Create activities
        activities = [
            Activity(user=users[0], type='Cycling', duration=60, date='2025-04-09'),
            Activity(user=users[1], type='Crossfit', duration=120, date='2025-04-08'),
            Activity(user=users[2], type='Running', duration=90, date='2025-04-07'),
            Activity(user=users[3], type='Strength', duration=30, date='2025-04-06'),
            Activity(user=users[4], type='Swimming', duration=75, date='2025-04-05'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=team1, points=100),
            Leaderboard(team=team2, points=90),
        ]
        for entry in leaderboard_entries:
            entry.save()

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
