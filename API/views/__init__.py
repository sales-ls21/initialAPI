# __all__ = [
# 	'app_user_view',
# 	'equipment_view',
# 	'exercises_view',
# 	'muscle_group_view',
# 	'workouts_view',
# 	'workout_type_view',
# 	'exercises_on_workout_view',
# ]

from .app_user_view import AppUserViewSet
from .equipment_view import EquipmentViewSet
from .exercises_view import ExercisesViewSet
from .exercises_on_workout_view import ExercisesOnWorkoutViewSet
from .muscle_group_view import BodyPartViewSet
from .workout_type_view import WorkoutTypeViewSet
from .workouts_view import WorkoutViewSet
