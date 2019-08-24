import re
import urllib.parse
from django.shortcuts import render
from django.conf import settings

from .models import Document

def index(request):
    ctx = {}

    try:
        if 'input' in request.POST:
            document_search = urllib.parse.unquote(request.POST['input'])

            url_match = re.search(r'https://.*/doc/(([A-Za-z0-9]+/[A-Fa-f0-9]{64})|(\?path=.*))', document_search)
            new_url = None
            if url_match is not None:
                new_url = urllib.parse.urljoin(settings.REUP_DOCUMENT_URL_PREFIX, url_match[1])

            ctx['urls'] = {
                'new_url': new_url
            }

            id_match = re.search(r'\d+', document_search)
            if id_match is None:
                raise ValueError('Could not find an ID in the input.')

            ctx['document'] = Document.objects.get(old_id=id_match[0])

    except Document.DoesNotExist:
        ctx['document'] = {
            'md5': 'Not found',
            'sha1': 'Not found',
        }
    except ValueError as e:
        ctx['message'] = e

    return render(request, 'revive/index.html', ctx)
