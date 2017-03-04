from django.contrib import admin
from API.models import *

# Register your models here.
admin.site.register(app_user.AppUser)
admin.site.register(exercises.Exercises)
admin.site.register(equipment.Equipment)
admin.site.register(muscle_group.BodyPart)
admin.site.register(workouts.Workout)
admin.site.register(exercises_on_workout.ExercisesOnWorkout)
admin.site.register(workout_type.WorkoutType)


