import re
import urllib.parse
from django.shortcuts import render
from django.conf import settings

from .models import Document


def match_url(document_search):
    url_match = re.search(
        r'https://.*/doc/(([A-Za-z0-9]+/[A-Fa-f0-9]{64})|(\?path=.*))',
        document_search,
    )

    if url_match:
        url = urllib.parse.urljoin(settings.REUP_DOCUMENT_URL_PREFIX,
                                   url_match[1])
        return {'urls': [(url, url)]}

    id_match = re.search(r'\d+', document_search)
    if id_match:
        document = Document.objects.filter(old_id=id_match[0]).first()

        if document:
            return {
                'document': document,
                'urls': [
                    (document.md5, settings.REUP_MD5_URL.format(md5=document.md5)),
                    (document.sha1, settings.REUP_SHA1_URL.format(sha1=document.sha1)),
                ],
            }

    return {'error_message': 'Not Found'}


def index(request):
    if request.POST:
        ctx = match_url(request.POST['input'])

    else:
        ctx = {}

    return render(request, 'revive/index.html', ctx)
