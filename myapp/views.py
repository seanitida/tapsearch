
from django.shortcuts import render
from .models import Flower
from django.http import HttpResponseRedirect # < here
from .forms import MyForm
# Create your views here.


def index(request):
	flowers = Flower.objects.all()
	return render(request,'myapp/index.html',{'flowers': flowers,})
def detail(request, id=None): # < here
	flower = get_object_or_404(Flower, id=id)
	return render(request, 'myapp/detail.html', {'flower': flower})
# Create your views here.
def index(request):
	q = request.GET.get('q', None)
	items = ''
	if q is None or q is "":
		flowers = Flower.objects.all()
	elif q is not None:
		flowers = Flower.objects.filter(description__contains=q)
	return render(request, 'myapp/index.html', {'flowers': flowers })

def create(request): # < here
	if request.method == 'POST':
		form = MyForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = MyForm()
		return render(request, 'myapp/edit.html', {'form': form})
