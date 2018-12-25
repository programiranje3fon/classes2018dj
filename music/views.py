# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView

from music.models import Performer, Song


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
    template_name = 'music/performer_list.html'
    paginate_by = 2

    def get_queryset(self):
        return Performer.objects.all()


class SongDetailView(DetailView):
    model = Song


class SongListView(ListView):
    model = Song
    template_name = 'music/song_list.html'
    paginate_by = 2

    def get_queryset(self):
        return Song.objects.all()


class PerformerCreate(CreateView):
    model = Performer
    fields = '__all__'


class PerformerUpdate(UpdateView):
    model = Performer
    fields = ['name', 'is_band']


class PerformerDelete(DeleteView):
    model = Performer
    success_url = reverse_lazy('performer-list')


class SongCreate(CreateView):
    model = Song
    fields = '__all__'


class SongUpdate(UpdateView):
    model = Song
    fields = ['title', 'performer', 'time', 'release_date']


class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('song-list')

