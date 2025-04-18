from django.shortcuts import render, get_object_or_404
from .models import Advertisement

def ad_list(request):
    ads = Advertisement.objects.all()
    return render(request, 'ads/list.html', {'ads': ads})

def ad_detail(request, pk):
    ad = get_object_or_404(Advertisement, pk=pk)
    return render(request, 'ads/detail.html', {'ad': ad})