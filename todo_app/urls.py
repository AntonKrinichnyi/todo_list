from django.urls import path
from todo_app.views import (
    TagDeleteView,
    TagUpdateView,
    TaskDeleteView,
    TaskListView,
    TaskCreateView,
    TagListView,
    TagCreateView,
    TaskUpdateView,
    ToggleAssignToTaskView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path(
        "task/<int:pk>/toggle-assign/",
        ToggleAssignToTaskView.as_view(),
        name="toggle-task-assign",
    ),
    path("tag/", TagListView.as_view(), name="tag-list"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo_app"
