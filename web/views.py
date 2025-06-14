from django.shortcuts import render

# Create your views here.
def register(request):
	return render(request, 'other/register.html')

def accounts(request):
	return render(request, 'other/accounts.html')

def operations(request):
	return render(request, 'other/operations.html')

def plans(request):
	return render(request, 'other/plans.html')

def more(request):
	return render(request, 'other/more.html')

