from django.test import TestCase
from django.urls import reverse
from django.http import response
from behindrole.models import Tweet
from django.contrib.auth import get_user_model
# Create your tests here.


# class SimpleTests (SimpleTestCase):

#     def test_home_page_status(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)

#     def test_about_page_status(self):
#         response = self.client.get('/about/')
#         self.assertEqual(response.status_code, 200)

# class TweetModelTests(TestCase):

#     # setup a test database and create an object  fill the proper field of model.
#     def setUp(self):
#         Tweet.objects.create(tweetTitle="this is a tweet")

#     # test content

#     def test_text_content(self):
#         tweet = Tweet.objects.get(id=1)
#         # get value
#         expected_object_name = tweet.tweetTitle
#         # compare first record  from db and what is in object field from model
#         self.assertEqual(expected_object_name, "this is a tweet")


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


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret',
        )
        self.tweet = Tweet.objects.create(

            tweetTitle='A good title',
            body='Nice body content',


        )

    def test_string_presentation(self):
        tweet = Tweet(tweetTitle="A sample title")
        self.assertEqual(str(tweet), tweet.tweetTitle)

    def test_tweet_content(self):
        self.assertEqual(f"{self.tweet.tweetTitle}", 'A good title')
        self.assertEqual(f"{self.tweet.body}", 'Nice body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
