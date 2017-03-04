from django.conf.urls import url, include
from django.contrib import admin
from API.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'app_user', AppUserViewSet)
router.register(r'equipment', EquipmentViewSet)
router.register(r'exercises', ExercisesViewSet)
router.register(r'workout_type', WorkoutTypeViewSet)
router.register(r'workout', WorkoutViewSet)
router.register(r'muscle_group', BodyPartViewSet)
router.register(r'exercises_on_workout', ExercisesOnWorkoutViewSet)


urlpatterns = [

    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
