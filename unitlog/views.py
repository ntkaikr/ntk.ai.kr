from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from collections import defaultdict
from .models import Residence
from .forms import ResidenceForm

@login_required
def residence_list(request):
    # 나만의 기록만 보여줌
    residences = Residence.objects.filter(author=request.user)
    floors = defaultdict(list)
    for r in residences:
        floors[r.floor].append(r)
    floors = dict(sorted(floors.items(), key=lambda x: -x[0]))  # 높은 층부터 정렬
    return render(request, "unitlog/residence_list.html", {"floors": floors})

@login_required
def residence_add(request):
    if request.method == "POST":
        form = ResidenceForm(request.POST)
        if form.is_valid():
            res = form.save(commit=False)
            res.author = request.user
            res.save()
            return redirect("unitlog:residence_list")
    else:
        form = ResidenceForm()
    return render(request, "unitlog/residence_form.html", {"form": form})
