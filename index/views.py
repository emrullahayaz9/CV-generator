from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ProfileModelForm
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
def index(request):
    if request.method=="GET":
        form = ProfileModelForm()
        return render(request, "pdf/accept.html", {"form":form})
    
    if request.method=="POST":
        form = ProfileModelForm(request.POST)
        form.save()
        return HttpResponseRedirect("http://127.0.0.1:8000/allforms")
    
def all_forms(request):
    all_forms = Profile.objects.all()
    return render(request, "pdf/all-forms.html", {"all_forms":all_forms})
def resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template("pdf/resume.html")
    html = template.render({'user_profile':user_profile})
    options = {
        'page-size':'Letter',
        'encoding':'UTF-8',
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename='resume.pdf'

    return response

def list(request):
    profiles = Profile.objects.all()
    return render(request,'pdf/list.html',{'profiles':profiles})