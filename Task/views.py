import Task
from django.shortcuts import redirect, render
from .models import Add

# Create your views here.
def index(request):
    ans = Add.objects.all()
    return render(request, "index.html", {"ans": ans})


def solve(request):
    # print(request.POST.get("task"))
    if request.POST.get("task"):

        val = request.POST.get("task")
        add = Add(mytask=val)

        add.save()

    return redirect("/")


def delete(request, a: int):
    # request.GET.get(a)
    # print(a)
    Add.objects.get(id=a).delete()

    return redirect("index")


def save(request):

    d = request.POST.get("id")
    val = Add.objects.get(id=d)
    val.mytask = request.POST.get("task")

    val.save()
    return redirect("index")


def update(request, a: int):
    temp = Add.objects.get(id=a)
    print(temp)
    content = {"name": temp}
    return render(request, "update.html", content)
