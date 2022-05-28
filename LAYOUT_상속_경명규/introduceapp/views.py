from django.shortcuts import render

# Create your views here.
def department(request):
    return render(request, 'department.html')

def KMGs_Gallery(request):
    return render(request, 'KMGs_Gallery.html')

def Schedule_202214080_KMG(request):
    return render(request, 'Schedule_202214080_KMG.html')

def test(request):
    return render(request, 'test.html')