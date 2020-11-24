from django.test import TestCase
from django.urls import reverse
from django.http import response
from behindrole.models import Tweet
# Create your tests here.


# class SimpleTests (SimpleTestCase):

#     def test_home_page_status(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)

#     def test_about_page_status(self):
#         response = self.client.get('/about/')
#         self.assertEqual(response.status_code, 200)

class TweetModelTests(TestCase):

    # setup a test database and create an object  fill the proper field of model.
    def setUp(self):
        Tweet.objects.create(tweetTitle="this is a tweet")

    # test content

    def test_text_content(self):
        tweet = Tweet.objects.get(id=1)
        # get value
        expected_object_name = tweet.tweetTitle
        # compare first record  from db and what is in object field from model
        self.assertEqual(expected_object_name, "this is a tweet")


class HomePageViewTest(TestCase):
    def setUp(self):
        Tweet.objects.create(tweetTitle="this is another test")

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
