from django.shortcuts import render, redirect
from .models import Widget
from django.views.generic.edit import DeleteView
from .forms import WidgetForm



# Create your views here.
def home(request):
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    total = sum([x.quantity for x in widgets])
    return render(request, 'home.html', {'widgets': widgets, 'widget_form': widget_form, 'total': total})

def WidgetCreate(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.save()

    return redirect('home')

def WidgetDelete(request, widget_id):
    Widget.objects.filter(id=widget_id)[0].delete()
    return redirect('home')
