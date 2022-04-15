from django.shortcuts import redirect


def sign_in_required(view):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view(request, *args, **kwargs)
        else:
            return redirect("signin")

    return wrapper
