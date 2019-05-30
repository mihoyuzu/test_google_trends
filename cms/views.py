from django.shortcuts import render
from pytrends.request import TrendReq


def keyword_list(request):
    """キーワード一覧"""

    pytrends = TrendReq(hl='ja-JP', tz=360)
    response = pytrends.trending_searches(pn='japan')

    object_list = response.values.tolist()
    return render(request, 'cms/keyword_list.html', {'object_list': object_list})


