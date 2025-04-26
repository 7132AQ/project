from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ad
from .forms import AdForm
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.db.models import Q



class AdListView(ListView):
    model = Ad
    template_name = 'ads/ad_list.html'
    context_object_name = 'ads'
    ordering = ['-created_at']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        params = self.request.GET

        if search_query := params.get('q'):
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query)
            )

        if category := params.get('category'):
            queryset = queryset.filter(category=category)

        if min_price := params.get('min_price'):
            queryset = queryset.filter(price__gte=min_price)
        if max_price := params.get('max_price'):
            queryset = queryset.filter(price__lte=max_price)

        if sort_by := params.get('sort'):
            sort_options = {
                'newest': '-created_at',
                'oldest': 'created_at',
                'price_asc': 'price',
                'price_desc': '-price'
            }
            queryset = queryset.order_by(sort_options.get(sort_by, '-created_at'))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Ad.CATEGORY_CHOICES
        context['current_params'] = self.request.GET
        return context


class AdDetailView(DetailView):
    model = Ad
    template_name = 'ads/ad_detail.html'

@login_required
def ad_create(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            ad.save()
            messages.success(request, 'Объявление успешно создано!')
            return redirect('ads:ad_detail', pk=ad.pk)
    else:
        form = AdForm()
    return render(request, 'ads/ad_create.html', {'form': form})

@login_required
def my_ads(request):
    ads = Ad.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'ads/my_ads.html', {'ads': ads})

@login_required
def ad_delete(request, pk):
    ad = get_object_or_404(Ad, pk=pk, author=request.user)
    if request.method == 'POST':
        ad.delete()
        messages.success(request, 'Объявление успешно удалено!')
        return redirect('ads:my_ads')
    return render(request, 'ads/ad_confirm_delete.html', {'ad': ad})

def home(request):
    return render(request, 'ads/home.html')