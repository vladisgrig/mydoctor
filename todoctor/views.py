from django.shortcuts import render

# Create your views here.
def main_page(request):
	return render(request, 'todoctor/index.html', {})

def results(request):
	return render(request, 'todoctor/results.html', {})

def coupon(request):
	return render(request, 'todoctor/coupon.html', {})
