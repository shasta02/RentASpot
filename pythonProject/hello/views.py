from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import RenterModel
from django.db import connections

querySearch = ''


def index(request):
    return render(request, 'hello/index.html')


def index2(request):
    querySearch = request.GET.get('q')
    #print (querySearch)
    optionList = []

    for p in RenterModel.objects.raw('SELECT renter_location FROM hello_rentermodel'):
        if str(p) == querySearch:
            optionList.append(p)
    return render(request, 'hello/index2.html')
    # return render_to_response("index2.html", {'optionsList:' optionsList})


class SearchResultsViews(ListView):
    model = RenterModel
    template_name = 'hello/index2.html'

    def get_queryset(self):
        return RenterModel.objects.filter(renter_price__icontains='$10')
