from django.http import Http404
from django.shortcuts import render

from .models import Document

def index(request):
    ctx = {}

    try:
        if 'id' in request.POST:
            ctx['document'] = Document.objects.get(pk=request.POST['id'])
    except Document.DoesNotExist:
        ctx['message'] = 'Not found.'

    return render(request, 'revive/index.html', ctx)
