from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def index(request):
    data = DataScript.objects.all().exclude(count=3).order_by("?").first()

    if request.method == 'POST':
        text = request.POST['text']
        id = request.POST['id']
        datascript = DataScript.objects.get(id=id)
        datascript.count += 1
        datascript.save()
        textinput = ScriptInput(inputText=text, user_that_input=datascript)
        textinput.save()
        return redirect('/')

    context = {'data': data}
    return render(request, 'index.html', context)
