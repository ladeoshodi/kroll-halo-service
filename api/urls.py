from django.urls import path
from .views import KrollHaloMappingList, KrollHaloMappingDetail

urlpatterns = [
    path("", KrollHaloMappingList.as_view()),
    path("kroll_ticket/<str:kroll_ticket_id>/", KrollHaloMappingDetail.as_view()),
]
