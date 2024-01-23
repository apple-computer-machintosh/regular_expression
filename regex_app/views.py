from django.shortcuts import redirect, render
from .forms import RegexForm

def index(request):
    regexForm = RegexForm()
    context = {
        'regexForm': regexForm
    }
    return render(request, 'regex/index.html', context)

def confirm(request):
    if request.method == 'POST':
        form = RegexForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render(request, 'regex/confirm.html', {'data': data})
    else:
        form = RegexForm()

    return render(request, 'regex/index.html', {'form': form})