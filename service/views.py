from django.shortcuts import render
from .forms import EpresForm
from .models import eprescriptions,Hospital
from django.http import HttpResponse
from django.views.generic import View,ListView
from django.template.loader  import get_template
from .utils import render_to_pdf
# Create your views here.
def eprescription(request):
    form = EpresForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=EpresForm()
    context={
        'form':form
    }
    return render(request,"eprescription/eprescription.html",context)

class hospitallist(ListView):
    context_object_name = Hospital
    template_name = 'hospital.html'
    context_object_name = 'hospital'
    


class GeneratePDF(View):
    def get(self,request,*args,**kwargs):
        template = get_template("eprescription/prescription.html")
        context = {
            'invoice_id':123,
            "customer_name":'nirob',
            "Amount": 52.5,
            "today" : "Today"
            }
        html = template.render(context)
        pdf = render_to_pdf('eprescription/prescription.html',context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("123456")
            content = "inline; filename='%s'" %(filename)
            response['content-Disposition'] = content
            return response
        return HttpResponse("Not Found")
