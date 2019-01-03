from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import NameForm
from django.utils.crypto import get_random_string
from django.urls import reverse, reverse_lazy



def index(request):
	if request.GET:
		dC = request.GET.get('dayChosen')
		dayChosen = dC.split(",",dC.count(","))
		#k = dayChosen.length()
		#render(request, 'user.html')
		return HttpResponse(dayChosen)
	return render(request, 'week.html')


def get_name(request):
	if request.method == 'POST':
		#random_url = get_random_string(length=10)
		form = NameForm(request.POST)
		if form.is_valid():
			#return redirect('result.html', random_url)
			#return reverse('randomURL', args=[random_url])  
			#return redirect('randomURL', random_url)
			#return reverse_lazy('randomURL')
			#redirect(reverse('randomURL',kwargs={'random_url': random_url}))
			#return render(request, 'resultpage', {'form':form})
			#return redirect('result.html')
			return render(request, 'result.html', {'form':form})
	else:
		form = NameForm()

	return render(request, 'user.html', {'form':form})

def resultpage(request):

	return render(request, 'result.html', {'form':form})