from django.conf.urls import url, include
from rest_framework import routers
from core.views import StudentViewSet, UniversityViewSet
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'universities', UniversityViewSet)

schema_view = get_swagger_view(title='API Docs')

urlpatterns = [
url(r'^docs/', schema_view)
]
urlpatterns += router.urls
