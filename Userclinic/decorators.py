from django.shortcuts import redirect


def admin_required(view_func):

    def wrapper(request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('login')

        try:
            role = request.user.profile.role
        except Exception:
            role = None

        if role != 'ADMIN':
            return redirect('login')

        return view_func(
            request,
            *args,
            **kwargs
        )

    return wrapper