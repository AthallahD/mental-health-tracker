from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '230624024',
        'name': 'Athallah Damar Jiwanto',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)