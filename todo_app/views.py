from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from todo_app.models import Task, Tag
from django.views import generic


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "todo_app/task_list.html"
    paginate_by = 10
    queryset = Task.objects.select_related("tag")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ["content", "deadline", "tag"]
    success_url = "todo_app:task_list"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ["content", "deadline", "tag"]
    success_url = "todo_app:task_list"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = "todo_app:task_list"


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "todo_app/tag_list.html"
    paginate_by = 10


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ["name"]
    success_url = "todo_app:tag_list"


class ToggleAssignToTaskView(generic.View):
    @staticmethod
    def post(request, pk):
        if (Task.objects.get(id=pk).done):
            Task.objects.get(id=pk).done = False
        else:
            Task.objects.get(id=pk).done = False
        return HttpResponseRedirect(reverse_lazy("todo_app:task-list",))



class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    success_url = "todo_app:tag_list"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = "todo_app:tag_list"
    