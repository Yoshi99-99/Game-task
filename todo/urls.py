from django.urls import path
from todo.views import DailyMissionListView, DailyMissionDetailView, DailyMissionCreateView, DailyMissionDeleteView, DailyMissionUpdateView, daily_mission_update_object, \
WeeklyMissionListView, WeeklyMissionDetailView, WeeklyMissionCreateView, WeeklyMissionDeleteView, WeeklyMissionUpdateView, weekly_mission_update_object, \
NomalMissionListView, NomalMissionDetailView, NomalMissionCreateView, NomalMissionDeleteView, NomalMissionUpdateView, nomal_mission_update_object

urlpatterns = [
    path('', DailyMissionListView.as_view(), name='daily-mission-list'),
    path('dmission/<int:pk>', DailyMissionDetailView.as_view(), name='daily-mission-detail'),
    path('dmission/new', DailyMissionCreateView.as_view(), name='daily-mission-new'),
    path('dmission/<int:pk>/delete', DailyMissionDeleteView.as_view(), name='daily-mission-delete'),
    path('dmission/<int:pk>/edit', DailyMissionUpdateView.as_view(), name='daily-mission-edit'),
    path('dmission/<int:pk>/update', daily_mission_update_object, name='daily-mission-update-object'),
    path('wmission/', WeeklyMissionListView.as_view(), name='weekly-mission-list'),
    path('wmission/<int:pk>', WeeklyMissionDetailView.as_view(), name='weekly-mission-detail'),
    path('wmission/new', WeeklyMissionCreateView.as_view(), name='weekly-mission-new'),
    path('wmission/<int:pk>/delete', WeeklyMissionDeleteView.as_view(), name='weekly-mission-delete'),
    path('wmission/<int:pk>/edit', WeeklyMissionUpdateView.as_view(), name='weekly-mission-edit'),
    path('wmission/<int:pk>/update', weekly_mission_update_object, name='weekly-mission-update-object'),
    path('nmission/', NomalMissionListView.as_view(), name='nomal-mission-list'),
    path('nmission/<int:pk>', NomalMissionDetailView.as_view(), name='nomal-mission-detail'),
    path('nmission/new', NomalMissionCreateView.as_view(), name='nomal-mission-new'),
    path('nmission/<int:pk>/delete', NomalMissionDeleteView.as_view(), name='nomal-mission-delete'),
    path('nmission/<int:pk>/edit', NomalMissionUpdateView.as_view(), name='nomal-mission-edit'),
    path('nmission/<int:pk>/update', nomal_mission_update_object, name='nomal-mission-update-object'),
]