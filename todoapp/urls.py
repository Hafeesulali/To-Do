from django.urls import path
from todoapp import views

urlpatterns = [
    path("accounts/register", views.SignUpView.as_view(), name="register"),
    path("accounts/login", views.SignInView.as_view(), name="signin"),
    path("add", views.TodoCreateView.as_view(), name="createtodo"),
    path("home", views.UserHome.as_view(), name="home"),
    path("all", views.TodoListView.as_view(), name="alltodos"),
    path("detail/<int:id>", views.TodoDetail.as_view(), name="tododetail"),
    path("todo/change/<int:id>", views.EditTodo.as_view(), name="changetodo"),
    path("todo/delete/<int:id>", views.remove_todo, name="deletetodo")

]
