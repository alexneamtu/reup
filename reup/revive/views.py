from django.shortcuts import render, get_object_or_404

from .models import Document

def index(request):
    ctx = {}
    if 'id' in request.POST:
        ctx['document'] = get_object_or_404(Document, pk=request.POST['id'])

    return render(request, 'revive/index.html', ctx)
