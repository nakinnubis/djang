from django.http import HttpResponse
from django.template import loader
from .models import Albums

#this is define based on the url that i want for my default url. it is the same as the name=index
def index(request):
    all_albums = Albums.objects.all()
    template = loader.get_template(music/index.html)    
    return HttpResponse(html)

def detail(request, albums_id):
    return HttpResponse("<h1> Welcome retrieving album details" + str(albums_id) + "</h1>" )
