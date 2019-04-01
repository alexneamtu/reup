from django.core.management import CommandError
from django.test import TestCase
from django.urls import reverse
from django.core import management

from .models import Document


class CommandsTestCase(TestCase):
    def test_import_documents_missing_file_param(self):
        """
        Should throw error for missing input file
        """
        try:
            management.call_command('import_documents')
        except CommandError as e:
            self.assertEqual(str(e), 'Error: the following arguments are required: csv_path');


class ReviveIndexViewTests(TestCase):

    def test_search_successful(self):
        """
        Should search and find a document.
        """
        Document.objects.get_or_create(
            old_id=1,
            md5='test',
            sha1='test',
        )
        response = self.client.post(reverse('index'), {'id': '1'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<li id="md5">MD5: test</li>')
        self.assertContains(response, '<li id="sha1">SHA1: test</li>')

    def test_search_invalid(self):
        """
        Should return invalid message for non numeric input.
        """
        response = self.client.post(reverse('index'), {'id': 'a'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid.')

    def test_search_not_found(self):
        """
        Should return not found message.
        """
        response = self.client.post(reverse('index'), {'id': '1'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Not found.')
