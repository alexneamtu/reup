from django.shortcuts import render

from .models import Document


def index(request):
    ctx = {}

    try:
        if 'id' in request.POST:
            ctx['document'] = Document.objects.get(old_id=request.POST['id'])
    except Document.DoesNotExist:
        ctx['message'] = 'Not found.'
    except ValueError:
        ctx['message'] = 'Invalid.'

    return render(request, 'revive/index.html', ctx)
