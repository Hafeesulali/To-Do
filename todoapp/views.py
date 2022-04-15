from django.shortcuts import render, redirect
from todoapp.forms import UserRegistrationForm, LoginFrom, TodoForm, TodoChangeForm
from django.views.generic import CreateView, View, TemplateView, ListView, DetailView, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from todoapp.models import Todos
from todoapp.decorators import sign_in_required
from django.utils.decorators import method_decorator


# Create your views here.

class SignUpView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "registration.html"
    success_url = reverse_lazy("signin")


class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = LoginFrom()
        return render(request, "login.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = LoginFrom(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")
            else:
                return render(request, "login.html", {"form": form})
        else:
            return render(request, "login.html", {"form": form})


@method_decorator(sign_in_required, name="dispatch")
class UserHome(TemplateView):
    template_name = "userhome.html"

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return render(request, self.template_name)
    #     else:
    #         return redirect("signin")


@method_decorator(sign_in_required, name="dispatch")
class TodoCreateView(CreateView):
    model = Todos
    form_class = TodoForm
    template_name = "add_todo.html"
    success_url = reverse_lazy("home")

    def post(self, request, *args, **kwargs):
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect("home")
        else:
            return render(request, self.template_name, {"form": form})


@method_decorator(sign_in_required, name="dispatch")
class TodoListView(ListView):
    model = Todos
    template_name = "list_todos.html"
    context_object_name = "todos"

    def get_queryset(self):
        qs = Todos.objects.filter(user=self.request.user)
        return qs
    # def get(self, request, *args, **kwargs):
    #     qs = Todos.objects.filter(user=request.user)
    #     return render(request, self.template_name, {"todos": qs})

@method_decorator(sign_in_required,name="dispatch")
class TodoDetail(DetailView):
    model = Todos
    template_name = "todo_detail.html"
    context_object_name = "todo"
    pk_url_kwarg = "id"

@method_decorator(sign_in_required,name="dispatch")
class EditTodo(UpdateView):
    model = Todos
    form_class = TodoChangeForm
    template_name = "edit_todo.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("alltodos")

@sign_in_required
def remove_todo(request, *args,**kwargs):
    todos = Todos.objects.get(id=kwargs["id"])
    todos.delete()
    return redirect("alltodos")

@sign_in_required
def sign_out(request,*args,**kwargs):
    logout(request)
    return redirect("signin")
