from django.shortcuts import render,redirect
from .models import FeedbackData
from .forms import FeedbackForm
import datetime as dt

time1=dt.datetime.now()
def feedback(request):
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            name=request.POST.get('name','')
            rating=request.POST.get('rating','')
            feedback=request.POST.get('feedback','')

            name=name.title()


            data=FeedbackData(name=name,
                              rating=rating,
                              time=time1,
                              feedback=feedback)
            data.save()
            return redirect('feedback/')
    else:
        fbs=FeedbackData.objects.all()
        form=FeedbackForm()
        return render(request,'feedback.html',{'form':form,'fbs':fbs})

# Create your views here.
