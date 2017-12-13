from django.test import TestCase

# Create your tests here.
import datetime

from django.utils import timezone

from .models import CommissionForm


class CommissionFormTests(TestCase):
    
    def test_was_published_recently_with_recent_form(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_form = CommissionForm(pub_date=time)
        self.assertIs(recent_form.was_published_recently(), True)

    def test_was_published_recently_with_past_form(self):
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

