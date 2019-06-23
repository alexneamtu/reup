import re
from django.shortcuts import render

from .models import Document


def index(request):
    ctx = {}

    try:
        if 'input' in request.POST:
            idMatch = re.search('\d+', request.POST['input'])
            if idMatch is None:
                raise ValueError('Could not find an ID in the input.')
            print(idMatch[0])
            ctx['document'] = Document.objects.get(old_id=idMatch[0])
    except Document.DoesNotExist:
        ctx['message'] = 'ID not found.'
    except ValueError as e:
        ctx['message'] = e

    return render(request, 'revive/index.html', ctx)
