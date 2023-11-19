# members/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Member, Flow, Oops, Function
from .forms import MemberForm

def members(request):
    mymembers = Member.objects.all()
    cmembers = Flow.objects.all()
    coops = Oops.objects.all()
    cfunction = Function.objects.all()
    return render(request, 'all_members.html', {'mymembers': mymembers, 'cmembers': cmembers, 'coops': coops, 'cfunction': cfunction})

def main(request):
    return render(request, 'main.html')

def details(request, id):
    template_mapping = {
        1: 'intro.html',
        7: 'datatype.html',
        6: 'type.html',
        2: 'variable.html',
        3: 'constant.html',
        4: 'comments.html',
        5: 'datatype.html',
        8: 'inputoutput.html',
    }

    template_name = template_mapping.get(id, 'details.html')
    mymember = get_object_or_404(Member, id=id)
    return render(request, template_name, {'mymember': mymember})

def control(request, id):
    template_mapping = {
        4: 'ifelse.html',
        5: 'while.html',
        6: 'dowhile.html',
        7: 'for.html',
        8: 'break.html',
        9: 'pass.html',
    }

    control = template_mapping.get(id, 'control.html')
    cmembers = get_object_or_404(Flow, id=id)
    return render(request, control, {'cmembers': cmembers})

def add_topic(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('members')
    else:
        form = MemberForm()
    return render(request, 'add_topic.html', {'form': form})

def object(request, id):
    template_mapping = {
        1: 'class.html',
        2:'inheritance.html',
        3:"exception.html",
        6:"encap.html"
    }

    template_name = template_mapping.get(id, 'object.html')
    coops = get_object_or_404(Oops, id=id)
    return render(request, template_name, {'coops': coops})

def fun(request, id):
    template_mapping = {
        2: 'fun.html',
    }

    template_name = template_mapping.get(id, 'function.html')
    cfunction = get_object_or_404(Function, id=id)
    return render(request, template_name, {'cfunction': cfunction})
