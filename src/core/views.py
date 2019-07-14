from django.shortcuts import render
from .models import Jobs, Category

# Create your views here.

def is_valid_queryparam(param):
	return param !='' and param is not None

def BootstrapFilterView(request):
	qs = Jobs.objects.all()
	categories = Category.objects.all()
	title_contains_query = request.GET.get('title_contains')
	id_exact_query = request.GET.get('id_exact')
	#id_exact_query = request.GET.get('id_exact')
	category = request.GET.get('category')
	if title_contains_query !='' and title_contains_query is not None:
		qs = qs.filter(Job__icontains = title_contains_query)
	
	if is_valid_queryparam(category) and category !='Choose...':
		qs = qs.filter(category__name =category)
	context = {
		'queryset':qs,
		'categories':categories
	}
	
	return render(request, "bootstrap_form.html", context)
	
