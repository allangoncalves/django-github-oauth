from django.shortcuts import redirect


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        return redirect('/login/')


def github_callback(request):
    code = request.GET['code']
