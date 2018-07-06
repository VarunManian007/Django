from django.http import HttpResponse,HttpResponseRedirect
from .models import Album,Song
from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.views.generic.edit import CreateView,UpdateView
from django.views import generic
from django.template import Context, loader
# from website.music.forms import LoginForm
# from website.music.models import Login
def index(request):
    return render(request, 'music/index.html')
    #all_albums=Album.objects.all()
    #template=loader.get_template('music/index.html')
    #context={'all_albums':all_albums,}

    #return render(request,'music/index.html',{'all_albums':all_albums})

# def login(request):
#     return render(request, 'music/login.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request, 'music/signup.html')

def shirt(request):
    return render(request, 'music/shirts.html')

def watch(request):
    return render(request, 'music/watch.html')

def camera(request):
    return render(request, 'music/camera.html')

        # def detail(request,album_id):
#     try:
#         album=Album.objects.get(pk=album_id)
#     except Album.DoesNotExist:
#         raise Http404("Album does not exist")
#     return render(request,'music/detail.html',{'album':album})
#
#     #return HttpResponse("<h2>Details about the song:"+str(album_id)+"</h2>")
#
# def favorite(request, album_id):
#     album=get_object_or_404(Album,pk=album_id)
#     try:
#         selected_song=album.song_set.get(pk=request.POST['song'])
#     except(KeyError, Song.DoesNotExist):
#         return render(request, 'music/detail.html', {'album': album,'error_message':'Select Valid Song',})
#     else:
#         selected_song.is_favorite=True
#         selected_song.save()
#         return render(request,'music/detail.html', {'album': album})
#
# # from django.views import generic
# # from .models import Album
# #
# # class IndexView(generic.ListView):
# #     template_name = 'music/index.html'
# #
# #     def get_queryset(self):
# #         return Album.objects.all()
# #
# # class Detail(generic.DetailView):
# #     model = Album
# #     template_name = 'music/detail.html'
#
# def AlbumCreate(CreateView):
#     model=Album
#     fields=['artist','album_title','genre','album_logo']


# def loginview(request):
#     if request.method=='POST':
#         form=LoginForm(request.POST)
#         if form.is_valid():
#             email=request.POST.get('email','')
#             pss=request.POST.get('pss','')
#             log=Login(email=email,pss=pss)
#             return render(request,'music/index.html')
#         else:
#             form=LoginForm()
#         return render(request,'music/login.html',{'form':form})

def submit(request, login_id):
    login=get_object_or_404(Album,pk=login_id)
    try:
        selected_msg=login.email_set.get(pk=request.POST['email'])
    except(KeyError, Login.DoesNotExist):
        return render(request, 'music/login.html', {'login': login,'error_message':'Select Valid Song',})
    else:
        selected_msg.is_submit=True
        selected_msg.save()
        return render(request,'music/login.html', {'login': login})