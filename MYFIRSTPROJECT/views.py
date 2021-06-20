from django.http import HttpResponse


def view1(request):
    return HttpResponse("Good Morning!")
def view2(request):
    return HttpResponse("Good Evening!")
def view3(request):
    return HttpResponse("Good Night!")
def view4(request):
    return HttpResponse("Vatashiva Sarika this")
def view5(request):
    return HttpResponse("O hiye Gojayemass!")