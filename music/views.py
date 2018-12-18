# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView

from music.models import Performer


# def index(request):
#     return HttpResponse('<h1>Hi there :)<h1>')

# def index(request):
#     n_performers = Performer.objects.all().count()
#     rng = range(0, 3)
#     context = {
#         'n_performers': n_performers,
#         'range': rng
#     }
#     # return render(request, 'index_0.html', context=context)
#     # return render(request, 'index_1.html', context=context)
#     return render(request, 'index_2.html', context=context)

def index(request):
    n_performers = Performer.objects.all().count()
    context = {
        'n_performers': n_performers,
    }
    # return render(request, 'index_0.html', context=context)
    # return render(request, 'index_1.html', context=context)
    # return render(request, 'index_2.html', context=context)
    return render(request, 'index.html', context=context)


# def performer_detail(request, pk):
#     # return HttpResponse(str(Performer.objects.get(id=pk)))
#     return HttpResponse(str(Performer.objects.get(id=pk).get_absolute_url()))

class PerformerDetailView(DetailView):
    model = Performer


class PerformerListView(ListView):
    model = Performer
    template = 'music/performer_list.html'
    paginate_by = 2

    def get_queryset(self):
        return Performer.objects.all()


