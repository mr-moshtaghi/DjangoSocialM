from django.shortcuts import render
from base.forms import AddCVacationForm
from base.models import Person
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.


def create_vacation(request, pk):
    if request.method == 'POST':
        form = AddCVacationForm(request.POST)
        if form.is_valid():
            person = Person.objects.filter(pk=pk).first()
            new_post = form.save(commit=False)
            new_post.person = person
            new_post.save()
            messages.success(request, 'your post submitted', 'success')
            return redirect('posts:all_posts')
    else:
        form = AddCVacationForm()
    return render(request, 'base/add_vacation.html', {'form': form})
