from django.shortcuts import render
from django.views import View

from main.models import News


def top_news_4():
    top_news_per_category = News.objects.order_by('-views')
    top_categories = []
    result = []
    for news in top_news_per_category:
        if news.category not in top_categories:
            top_categories.append(news.category)
            result.append(news)
        if len(top_categories) == 4:
            return result
    return top_news_per_category[:4]


class IndexView(View):

    def get(self, request):
        context = {
            'top_news_4': top_news_4(),
            'top_news': News.objects.order_by('-views').first(),
        }
        return render(request, 'index.html', context)
