from django.shortcuts import render
from wcp_app import models

# Create your views here. 
# test git push this is banch
def v_orm(request):
	name = request.POST.get('name')
	age = request.POST.get('age')
	corsor = models.wcp.objects.create(name=name,age=age)
	corsor.save()
	all_info = models.wcp.objects.order_by('age')
	return render(request, "wyn.html",{'all_list':all_info})