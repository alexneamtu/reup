from django.test import TestCase, override_settings

from .models import Document


class ReupTestCase(TestCase):
    def setUp(self):
        Document.objects.create(old_id=1, md5='test1', sha1='test1')
        Document.objects.create(old_id=12345, md5='test2', sha1='test2')
        Document.objects.create(
            old_id='46',
            md5='test3',
            sha1='test3',
        )

    def test_search_by_id_success(self):
        response = self.client.post('/', {'input': 1})
        self.assertContains(response, r'<li id="md5">MD5: <code>test1</code></li>')
        self.assertContains(response, r'<li id="sha1">SHA1: <code>test1</code></li>')
        self.assertNotContains(response, r'<li id="new_url">')

    def test_search_by_id_fail(self):
        response = self.client.post('/', {'input': 4})
        self.assertContains(response, r'<li id="md5">MD5: <code>Not found</code></li>')
        self.assertContains(response, r'<li id="sha1">SHA1: <code>Not found</code></li>')
        self.assertNotContains(response, r'<li id="new_url">')

    def test_search_by_url_success(self):
        response = self.client.post('/', {'input': r'https://hoover.liquiddemo.org/doc/12345/'})
        self.assertContains(response, r'<li id="md5">MD5: <code>test2</code></li>')
        self.assertContains(response, r'<li id="sha1">SHA1: <code>test2</code></li>')
        self.assertNotContains(response, r'<li id="new_url">')

    def test_search_by_url_fail(self):
        response = self.client.post('/', {'input': r'https://hoover.liquiddemo.org/doc/123456/'})
        self.assertContains(response, r'<li id="md5">MD5: <code>Not found</code></li>')
        self.assertContains(response, r'<li id="sha1">SHA1: <code>Not found</code></li>')
        self.assertNotContains(response, r'<li id="new_url">')

    @override_settings(REUP_DOCUMENT_URL_PREFIX=r'https://somethingelse.example.org/doc/')
    def test_replace_url_doc(self):
        response = self.client.post(
            '/',
            {'input': r'https://hoover.liquiddemo.org/doc/?path=%2Fdoc%2Ftestdata%2F_directory_46'},
        )
        self.assertContains(response, r'<li id="md5">MD5: <code>test3</code></li>')
        self.assertContains(response, r'<li id="sha1">SHA1: <code>test3</code></li>')
        self.assertContains(response, r'<li id="new_url">New URL: <code>https://somethingelse.example.org/doc/?path'
                                      r'=/doc/testdata/_directory_46</code></li>',
        )

    @override_settings(REUP_DOCUMENT_URL_PREFIX=r'https://somethingelse.example.org/doc/')
    def test_replace_url_sha256(self):
        response = self.client.post(
            '/',
            {'input': r'https://hoover.liquiddemo.org/doc/testdata'
                      r'/41567bf099e390d94f99f5c6fce3786ee57b6891a5c28f2785f4888aadfed464'},
        )
        self.assertContains(response, r'<li id="md5">MD5: <code>Not found</code></li>')
        self.assertContains(response, r'<li id="sha1">SHA1: <code>Not found</code></li>')
        self.assertContains(response, r'<li id="new_url">New URL: <code>https://somethingelse.example.org/doc'
                                      r'/testdata/41567bf099e390d94f99f5c6fce3786ee57b6891a5c28f2785f4888aadfed464',
        )
