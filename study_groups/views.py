from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import StudyGroup
from django.views.generic import ListView

@login_required
def join_group(request, group_id):
    group = get_object_or_404(StudyGroup, id=group_id)
    group.members.add(request.user)
    return redirect('group-detail', group_id=group.id)

def group_detail(request, group_id):
    group = get_object_or_404(StudyGroup, id=group_id)
    return render(request, "study_groups/group_detail.html", {'group':group})

class GroupList(ListView):
    model = StudyGroup
    context_object_name = 'groups'