from django.shortcuts import render, redirect
from .forms import ScriptForm
from django.contrib.auth.decorators import login_required
from .models import Script, Character
from .forms import CharacterForm
from django.shortcuts import get_object_or_404
from .models import Scene
from .forms import SceneForm, DialogueForm
from .models import Dialogue

@login_required
def write_scene(request, script_id, scene_id):
    script = get_object_or_404(Script, id=script_id, created_by=request.user)
    scene = get_object_or_404(Scene, id=scene_id, script=script)
    characters = Character.objects.filter(script=script)
    dialogues = Dialogue.objects.filter(scene=scene).order_by('order')

    if request.method == 'POST':
        form = DialogueForm(request.POST, script=script)  # script 넘김
        if form.is_valid():
            dialogue = form.save(commit=False)
            dialogue.scene = scene
            dialogue.order = dialogues.count() + 1
            dialogue.save()
            return redirect('scripter:write_scene', script_id=script.id, scene_id=scene.id)
    else:
        form = DialogueForm(script=script)

    return render(request, 'scripter/write_scene.html', {
        'script': script,
        'scene': scene,
        'form': form,
        'dialogues': dialogues
    })

@login_required
def add_scene(request, script_id):
    script = get_object_or_404(Script, id=script_id, created_by=request.user)
    scenes = Scene.objects.filter(script=script).order_by('order')

    if request.method == 'POST':
        form = SceneForm(request.POST)
        if form.is_valid():
            scene = form.save(commit=False)
            scene.script = script
            scene.save()
            return redirect('scripter:add_scene', script_id=script.id)
    else:
        form = SceneForm()



    return render(request, 'scripter/add_scene.html', {
        'script': script,
        'form': form,
        'scenes': scenes
    })

@login_required
def setup_script(request, script_id):
    script = get_object_or_404(Script, id=script_id, created_by=request.user)
    characters = Character.objects.filter(script=script)

    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.script = script
            character.save()
            return redirect('scripter:setup_script', script_id=script.id)
    else:
        form = CharacterForm()


    return render(request, 'scripter/setup_script.html', {
        'script': script,
        'form': form,
        'characters': characters
    })


def index(request):
    return render(request, 'scripter/index.html')


@login_required
def create_script(request):
    if request.method == 'POST':
        form = ScriptForm(request.POST)
        if form.is_valid():
            script = form.save(commit=False)
            script.created_by = request.user
            script.save()
            return redirect('scripter:setup_script', script_id=script.id)  # ← 여기 OK
    else:
        form = ScriptForm()

    return render(request, 'scripter/create_script.html', {'form': form})
