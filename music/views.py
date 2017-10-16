from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album, Song, login
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth import logout
from .forms import AlbumForm, SongForm, UserForm

from django.shortcuts import render, get_object_or_404

from django.views.generic import View



def home(request):
    return render(request, 'music/homepage.html', None)


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums, }
    return render(request, 'music/index.html', context)


def details(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/details.html', {"album": album})
    # return HttpResponse("<h1>hello</h1>")


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['Song'])

    except(KeyError, Song.DoesNotExist):
        return render(request, 'music/details', {'album': album, 'error message': "you did not select a valid song"})
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})


# user authentications
class Userform(View):
    template_name = 'music/UserLogin.html'

    # for new user who doesnt have  account

    def get(self, request):
        form = UserForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserForm(request.POST)

        if form.is_valid():
            # data saving by post method
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            p, created = login.objects.get_or_create(username=username, password=password)

            # obj.username=username
            # obj.password=password
            # obj.save()
            # user = authenticate(username=username, password=password)
            #
            # if user is not None:
            #
            #     if user.is_active:
            #         login(request="", user=user)
            #         return redirect('music :index.html')
        form = UserForm()
        return render(request, self.template_name, {'form': form})


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


def contact(request):
    return render(request, 'music/contact.html', context=None)


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None )
    context = {"forms" : form, }
    return render(request, 'music/UserLogin.html', context)
