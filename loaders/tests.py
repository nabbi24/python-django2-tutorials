from django.test import TestCase

# Create your tests here.
import datetime

from django.utils import timezone
from django.urls import reverse

from .models import CommissionForm

def create_form(form_id, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return CommissionForm.objects.create(form_id=form_id, pub_date=time)

class CommissionFormTests(TestCase):
    
    def test_was_published_recently_with_recent_form(self):
        """
        was_published_recently returns True for forms whose pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_form = CommissionForm(pub_date=time)
        self.assertIs(recent_form.was_published_recently(), True)

    def test_was_published_recently_with_past_form(self):
        """
        was_published_recently returns False for forms whose pub_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_form = CommissionForm(pub_date=time)
        self.assertIs(old_form.was_published_recently(), False)

    def test_was_published_recently_with_future_form(self):
        """
        was_published_recently() returns False for forms whose pub_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_form = CommissionForm(pub_date=time)
        self.assertIs(future_form.was_published_recently(), False)

class LoadersIndexViewTests(TestCase):
    def test_no_forms(self):
        """
        If no forms exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('loaders:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No forms are available.")
        self.assertQuerysetEqual(response.context['latest_commission_form_list'], [])

    def test_past_question(self):
        """
        Forms with a pub_date in the past are displayed on the index page.
        """
        create_form(form_id="past01", days=-30)
        response = self.client.get(reverse('loaders:index'))
        self.assertQuerysetEqual(response.context['latest_commission_form_list'], ['<CommissionForm: past01>'])

    def test_future_form(self):
        """
        Forms with a pub_date in the future aren't displayed on the index page.
        """
        create_form(form_id="future01", days=30)
        response = self.client.get(reverse('loaders:index'))
        self.assertContains(response, "No forms are available.")
        self.assertQuerysetEqual(response.context['latest_commission_form_list'], [])

    def test_future_form_and_past_form(self):
        """
        Even if both past and future forms exist, only past forms are displayed.
        """
        create_form(form_id="past01", days=-30)
        create_form(form_id="future01", days=30)
        response = self.client.get(reverse('loaders:index'))
        self.assertQuerysetEqual(
            response.context['latest_commission_form_list'],
            ['<CommissionForm: past01>']
        )

    def test_two_past_forms(self):
        """
        The forms index page may display multiple forms.
        """
        create_form(form_id="past01", days=-30)
        create_form(form_id="past02", days=-5)
        response = self.client.get(reverse('loaders:index'))
        self.assertQuerysetEqual(
            response.context['latest_commission_form_list'],
            ['<CommissionForm: past02>', '<CommissionForm: past01>']
        )

