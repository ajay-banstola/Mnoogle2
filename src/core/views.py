from django.shortcuts import render
from .models import Jobs

# Create your views here.


def BootstrapFilterView(request):
	qs = Jobs.objects.all()
	title_contains_query = request.GET.get('title_contains')
	id_exact_query = request.GET.get('id_exact')
	#id_exact_query = request.GET.get('id_exact')
	if title_contains_query !='' and title_contains_query is not None:
		qs = qs.filter(Job__icontains = title_contains_query)
	
	
	context = {
		'queryset':qs
	}
	
	return render(request, "bootstrap_form.html", context)
	
