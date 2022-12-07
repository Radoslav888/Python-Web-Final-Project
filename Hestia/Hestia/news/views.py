from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views import generic as views

from Hestia.news.models import News


class ListNewsView(views.ListView):
    model = News
    template_name = 'news/list-news.html'
    paginate_by = 1


def news_listings(request):
    news = News.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(news, 2)

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    context = {
        'news': news,
    }
    return render(request, 'news/list-news.html', context)


class DetailsNewsView(views.DetailView):
    model = News
    template_name = 'news/details-news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_news'] = News.objects.filter().order_by('-id')[:3][::-1]
        return context