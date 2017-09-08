from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Album,Song
from django.shortcuts import redirect


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_album'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:home')


class SongDelete(DeleteView):
    model = Song
    context_object_name = 'song'
    success_url = reverse_lazy('music:home')










'''from django.shortcuts import render,get_object_or_404
from .models import Song,Album
from django.http import HttpResponse

def index(request):
    all_albums = Album.objects.all()
    context = {'all_album':all_albums }
    return render(request,'index.html',context)

def detail(request,id):
    ad = get_object_or_404(Album, id=id)
    context = {'ad':ad}
    template = 'detail.html'
    return render(request,template,context)

def favorite(request,id):
    ad = get_object_or_404(Album, id=id)
    try:
        selected_song = ad.song_set.get(pk = request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request,'detail.html',{'album':ad,
                                             'error_msg':'You dont not chose write song'})
    else:
        selected_song.is_favorite = True

        selected_song.save()

        return render(request, 'detail.html', {'album':ad})
'''