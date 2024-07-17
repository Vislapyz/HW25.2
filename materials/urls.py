from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import (
    CourseView,
    LessonCreateAPIView,
    LessonDestroyAPIView,
    LessonListAPIView,
    LessonRetrieveAPIView,
    LessonUpdateAPIView,
    SubscriptionCourseAPIView,
)

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register(r"courses", CourseView, basename="courses")


urlpatterns = [
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson-create"),
    path("lesson/", LessonListAPIView.as_view(), name="lesson-list"),
    path("lesson/<int:pk>", LessonRetrieveAPIView.as_view(), name="lesson-get"),
    path("lesson/update/<int:pk>", LessonUpdateAPIView.as_view(), name="lesson-update"),
    path(
        "lesson/delete/<int:pk>", LessonDestroyAPIView.as_view(), name="lesson-delete"
    ),
    path("subscription/", SubscriptionCourseAPIView.as_view(), name="subscription"),
] + router.urls
