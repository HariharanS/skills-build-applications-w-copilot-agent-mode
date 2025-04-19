from django.contrib import admin
from octofit_tracker_app.models import User, Team, Activity, Leaderboard, Workout

admin.site.register(User)
admin.site.register(Team)
admin.site.register(Activity)
admin.site.register(Leaderboard)
admin.site.register(Workout)