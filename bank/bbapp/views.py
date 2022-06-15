from django.shortcuts import render, redirect
from .models import Branches,District
from .forms import AccountForm
from django.http import JsonResponse

# Create your views here.
def index(request):
    district=District.objects.all()
    return render(request,'index.html',{'districts':district})
def account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bbapp:success')
    else:
        form = AccountForm()
    return render(request, 'account.html', {'form': form})
def load_branches(request):
    district_id = request.GET.get('district_id')  #district id is from ajax requsest for data
    branches = Branches.objects.filter(district_id=district_id).order_by('name')
    return render(request,'branch_dropdown_list_options.html',{'branches':branches})
def success(request):
    return render(request, 'success.html')