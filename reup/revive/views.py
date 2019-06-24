import re
from django.shortcuts import render

from .models import Document


def index(request):
    ctx = {}

    try:
        if 'input' in request.POST:
            id_match = re.search(r'\d+', request.POST['input'])
            if id_match is None:
                raise ValueError('Could not find an ID in the input.')
            ctx['document'] = Document.objects.get(old_id=id_match[0])
    except Document.DoesNotExist:
        ctx['message'] = 'ID not found.'
    except ValueError as e:
        ctx['message'] = e

    return render(request, 'revive/index.html', ctx)
