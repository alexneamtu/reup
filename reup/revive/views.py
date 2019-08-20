import re
from django.shortcuts import render
from django.conf import settings

from .models import Document


def index(request):
    ctx = {}

    try:
        if 'input' in request.POST:
            id_match = re.search(r'\d+', request.POST['input'])
            if id_match is None:
                raise ValueError('Could not find an ID in the input.')
            document = Document.objects.get(old_id=id_match[0])
            ctx['document'] = document
            ctx['urls'] = {
                'md5': re.sub(r'{md5}', document.md5, settings.REUP_MD5_URL),
                'sha1': re.sub(r'{sha1}', document.sha1, settings.REUP_SHA1_URL),
            }
    except Document.DoesNotExist:
        ctx['message'] = 'ID not found.'
    except ValueError as e:
        ctx['message'] = e

    return render(request, 'revive/index.html', ctx)
