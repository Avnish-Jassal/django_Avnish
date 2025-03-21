from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from .models import alumne, professor

from .forms import alumne_form  # Importar el formulario

def alumne_form_view(request):
    if request.method == 'POST':
        form = alumne_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumne')  # Asegúrate de que 'alumne' es una ruta válida en urls.py
    else:
        form = alumne_form()

    return render(request, 'alumne_form.html', {'alumne_form': form})


from django.shortcuts import render, redirect
from .forms import professor_form  # Importa el formulario

def professor_form_view(request):
    if request.method == 'POST':
        form = professor_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('professor')  # Asegúrate de que 'professor' sea una ruta válida en urls.py
    else:
        form = professor_form()

    return render(request, 'professor_form.html', {'professor_form': form})

# Create your views here.

def index(request):
    template = loader.get_template('index_centre.html')
    return HttpResponse(template.render())


def index1(request):
    alumnoss = alumne.objects.all()
    return render(request, 'alumne.html', {'alumnos': alumnoss})


def index2(request):
    professors = professor.objects.all()
    return render(request, 'professor.html', {'professors': professors})


def alumne_detall(request, alumno_id):
    alumno = alumne.objects.get(id=alumno_id)
    return render(request, 'alumne_detall.html', {'alumn': alumno})

def professor_detall(request, profe_id):
    profe = professor.objects.get(id=profe_id)
    return render(request, 'professor_detall.html', {'proff': profe})
#from django.shortcuts import render, get_object_or_404

#def alumne_detall(request, alumno_id):
#    alumn = (alumne, id=alumno_id)  # Aquí usamos 'alumno_id', no 'alumn_id'
#    return render(request, 'alumne_detall.html', {'alumn': alumn})  # Se pasa 'alumn' al template
