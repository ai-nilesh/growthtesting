
from django.views.generic import ListView,DetailView

from . models import BlogModal

# Create your views here.

class HomePageView(ListView):
    template_name = 'home.html'
    model = BlogModal
    
class ArticalPageView(DetailView):
    template_name = 'detail.html'
    model = BlogModal
    context_object_name = 'nilesh'
    
    
    

