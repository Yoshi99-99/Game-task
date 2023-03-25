from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from todo.models import Daily_mission, Weekly_mission, Nomal_mission

# デイリータスクの挙動
class DailyMissionListView(ListView):
    model = Daily_mission
    template_name = 'todo/daily_mission_list.html'

class DailyMissionDetailView(DetailView):
    model = Daily_mission
    template_name = 'todo/mission_detail.html'

class DailyMissionDeleteView(DeleteView):
    model = Daily_mission
    success_url = reverse_lazy('daily-mission-list')
    template_name = 'todo/mission_delete.html'

class DailyMissionCreateView(CreateView):
    model = Daily_mission
    fields = ['title', 'description', 'deadline']
    template_name = 'todo/mission_form.html'
    success_url = reverse_lazy('daily-mission-list')

class DailyMissionUpdateView(UpdateView):
    model = Daily_mission
    fields = ['title', 'description', 'deadline']
    template_name = 'todo/mission_form.html'
    success_url = reverse_lazy('daily-mission-list')

def daily_mission_update_object(request, pk):
    my_object = get_object_or_404(Daily_mission, pk=pk)

    if request.method == 'POST' and 'update' in request.POST:
        my_object.completed = True
        my_object.save()
        return redirect('daily-mission-list')

    return render(request, 'todo/daily_mission_list.html', {'object': my_object})

# ウィークリータスクの挙動
class WeeklyMissionListView(ListView):
    model = Weekly_mission
    template_name = 'todo/weekly_mission_list.html'

class WeeklyMissionDetailView(DetailView):
    model = Weekly_mission
    template_name = 'todo/mission_detail.html'
    
class WeeklyMissionDeleteView(DeleteView):
    model = Weekly_mission
    success_url = reverse_lazy('weekly-mission-list')
    template_name = 'todo/mission_delete.html'

class WeeklyMissionCreateView(CreateView):
    model = Weekly_mission
    fields = ['title', 'description', 'deadline']
    template_name = 'todo/mission_form.html'
    success_url = reverse_lazy('weekly-mission-list')

class WeeklyMissionUpdateView(UpdateView):
    model = Weekly_mission
    fields = ['title', 'description', 'deadline']
    template_name = 'todo/mission_form.html'
    success_url = reverse_lazy('weekly-mission-list')
    
def weekly_mission_update_object(request, pk):
    my_object = get_object_or_404(Weekly_mission, pk=pk)

    if request.method == 'POST' and 'update' in request.POST:
        my_object.completed = True
        my_object.save()
        return redirect('weekly-mission-list')

    return render(request, 'todo/weekly_mission_list.html', {'object': my_object})
# ショップの挙動
class NomalMissionListView(ListView):
    model = Nomal_mission
    template_name = 'todo/nomal_mission_list.html'
    
class NomalMissionDetailView(DetailView):
    model = Nomal_mission
    template_name = 'todo/mission_detail.html'
    
class NomalMissionDeleteView(DeleteView):
    model = Nomal_mission
    success_url = reverse_lazy('nomal-mission-list')
    template_name = 'todo/mission_delete.html'

class NomalMissionCreateView(CreateView):
    model = Nomal_mission
    fields = ['title', 'description']
    template_name = 'todo/mission_form.html'
    success_url = reverse_lazy('nomal-mission-list')

class NomalMissionUpdateView(UpdateView):
    model = Nomal_mission
    fields = ['title', 'description']
    template_name = 'todo/mission_form.html'
    success_url = reverse_lazy('nomal-mission-list')
    
def nomal_mission_update_object(request, pk):
    my_object = get_object_or_404(Nomal_mission, pk=pk)

    if request.method == 'POST' and 'update' in request.POST:
        my_object.completed = True
        my_object.save()
        return redirect('nomai-mission-list')

    return render(request, 'todo/nomal_mission_list.html', {'object': my_object})