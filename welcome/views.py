from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import loader
from .models import *
from django.contrib import messages


# Create your views here.
def index(request):
    template = loader.get_template('welcome/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def detail(request):
        template = loader.get_template('welcome/index1.html')
        context = {

        }
        return HttpResponse(template.render(context, request))

def fr1(request):
    template = loader.get_template('welcome/r1.html')
    context = {

        }
    return HttpResponse(template.render(context, request))


def fr2(request):
    template = loader.get_template('welcome/r2.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def fr3(request):
    template = loader.get_template('welcome/r3.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def fr4(request):
    template = loader.get_template('welcome/r4.html')
    context = {

        }
    return HttpResponse(template.render(context, request))

def frr2(request):
    template = loader.get_template('welcome/rr2.html')
    context = {

        }
    return HttpResponse(template.render(context, request))

def frr3(request):
    template = loader.get_template('welcome/rr3.html')
    context = {

        }
    return HttpResponse(template.render(context, request))

def frr4(request):
    template = loader.get_template('welcome/rr4.html')
    context = {

        }
    return HttpResponse(template.render(context, request))

def  frshow(request):

     some_var = request.POST.getlist('ing')
     lengthh=len(some_var)
     if (lengthh == 0):

        template = loader.get_template('welcome/rshow.html')
        messages.info(request,'Choose atleast one ingredient!')
        context={

        }
        return HttpResponse(template.render(context, request))
     if(lengthh==1):
        p=beverage_1.objects.filter(ingredient1=some_var[0])
        template = loader.get_template('welcome/rshow.html')
        context1 = {
        'some_var':some_var,
        #'lengthh':lengthh
        'p':p
        }
        return HttpResponse(template.render(context1, request))
     if(lengthh==2):
         p = beverage_2.objects.filter(ingredient1=some_var[0],ingredient2=some_var[1])
         template = loader.get_template('welcome/rshow.html')
         context2 = {
             'some_var': some_var,
             # 'lengthh':lengthh
             'p': p
         }
         return HttpResponse(template.render(context2, request))
     if (lengthh == 3):
         p = beverage_3.objects.filter(ingredient1=some_var[0], ingredient2=some_var[1], ingredient3=some_var[2])
         template = loader.get_template('welcome/rshow.html')
         context3 = {
             'some_var': some_var,
             # 'lengthh':lengthh
             'p': p
         }
         return HttpResponse(template.render(context3, request))
     if (lengthh == 4):
         p = beverage_4.objects.filter(ingredient1=some_var[0], ingredient2=some_var[1], ingredient3=some_var[2], ingredient4=some_var[3])
         template = loader.get_template('welcome/rshow.html')
         context4 = {
             'some_var': some_var,
             # 'lengthh':lengthh
             'p': p
         }
         return HttpResponse(template.render(context4, request))
     if (lengthh == 5):
         p = beverage_5.objects.filter(ingredient1=some_var[0], ingredient2=some_var[1], ingredient3=some_var[2], ingredient4=some_var[3],ingredient5=some_var[4])
         template = loader.get_template('welcome/rshow.html')
         context5 = {
             'some_var': some_var,
             # 'lengthh':lengthh
             'p': p
         }
         return HttpResponse(template.render(context5, request))

def  frshow2(request):

     some_var = request.POST.getlist('ing')
     lengthh=len(some_var)
     if(lengthh==1):
        p=main_course_1.objects.filter(ingredient=some_var[0])
        template = loader.get_template('welcome/rshow2.html')
        context1 = {
        'some_var':some_var,
        #'lengthh':lengthh
        'p':p
        }
        return HttpResponse(template.render(context1, request))
     if(lengthh==2):
         p = main_course_2.objects.filter(ingredient1=some_var[0],ingredient2=some_var[1])
         template = loader.get_template('welcome/rshow2.html')
         context2 = {
             'some_var': some_var,
             # 'lengthh':lengthh
             'p': p
         }
         return HttpResponse(template.render(context2, request))
     if (lengthh == 3):
         p = main_course_3.objects.filter(ingredient1=some_var[0], ingredient2=some_var[1], ingredient3=some_var[2])
         template = loader.get_template('welcome/rshow2.html')
         context3 = {
             'some_var': some_var,
             # 'lengthh':lengthh
             'p': p
         }
         return HttpResponse(template.render(context3, request))
     if (lengthh == 4):
         p = main_course_4.objects.filter(ingredient1=some_var[0], ingredient2=some_var[1], ingredient3=some_var[2], ingredient4=some_var[3])
         template = loader.get_template('welcome/rshow2.html')
         context4 = {
             'some_var': some_var,
             # 'lengthh':lengthh
             'p': p
         }
         return HttpResponse(template.render(context4, request))
     if (lengthh == 5):
         p = main_course_5.objects.filter(ingredient1=some_var[0], ingredient2=some_var[1], ingredient3=some_var[2], ingredient4=some_var[3],ingredient5=some_var[4])
         template = loader.get_template('welcome/rshow2.html')
         context5 = {
             'some_var': some_var,
             # 'lengthh':lengthh
             'p': p
         }
         return HttpResponse(template.render(context5, request))

def  frshow3(request):

     some_var = request.POST.getlist('ing')
     lengthh=len(some_var)
     if(lengthh==1):
        p=Desserts_1.objects.filter(ingredient1=some_var[0])
        template = loader.get_template('welcome/rshow3.html')
        context1 = {
        'some_var':some_var,
        #'lengthh':lengthh
        'p':p
        }
        return HttpResponse(template.render(context1, request))
     if(lengthh==2):
         p = Desserts_2.objects.filter(ingredient1=some_var[0],ingredient2=some_var[1])
         template = loader.get_template('welcome/rshow3.html')
         context2 = {
             'some_var': some_var,
             # 'lengthh':lengthh
             'p': p
         }
         return HttpResponse(template.render(context2, request))
     if (lengthh == 3):
         p = Desserts_3.objects.filter(ingredient1=some_var[0], ingredient2=some_var[1], ingredient3=some_var[2])
         template = loader.get_template('welcome/rshow3.html')
         context3 = {
             'some_var': some_var,
             # 'lengthh':lengthh
             'p': p
         }
         return HttpResponse(template.render(context3, request))
     if (lengthh == 4):
         p = Desserts_4.objects.filter(ingredient1=some_var[0], ingredient2=some_var[1], ingredient3=some_var[2], ingredient4=some_var[3])
         template = loader.get_template('welcome/rshow3.html')
         context4 = {
             'some_var': some_var,
             # 'lengthh':lengthh
             'p': p
         }
         return HttpResponse(template.render(context4, request))
     if (lengthh == 5):
         p = Desserts_5.objects.filter(ingredient1=some_var[0], ingredient2=some_var[1], ingredient3=some_var[2], ingredient4=some_var[3],ingredient5=some_var[4])
         template = loader.get_template('welcome/rshow3.html')
         context5 = {
             'some_var': some_var,
             # 'lengthh':lengthh
             'p': p
         }
         return HttpResponse(template.render(context5, request))
