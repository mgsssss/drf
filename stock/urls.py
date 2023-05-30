from django.urls import path
from .views import KospiList, KospiDetail
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('kospi', KospiList.as_view()),
    path('kospi/<int:pk>', KospiDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)