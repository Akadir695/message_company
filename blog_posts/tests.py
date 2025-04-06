from django.test import TestCase
from .models import Post  # Import the Post model
from django.urls import reverse  # Correct import of reverse function

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a Post instance using the model class (Post, not post)
        cls.post = Post.objects.create(text="this is a test")
    
    def test_model_content(self):
        # Assert that the post text is correct
        self.assertEqual(self.post.text, "this is a test")
    
    def test_urls_exists_at_the_correct_location(self):
        # Test if the URL exists at the correct location
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_urls_exists_by_name(self):
        # Test if the URL exists using its name (reverse)
        response = self.client.get(reverse('home'))  # 'home' should match your URL name
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self):
     # Test if the correct template is used
     response = self.client.get(reverse('home'))  # 'home' should match your URL name
     self.assertTemplateUsed(response, "blog_posts/postlist.html")  # Update this line to match the actual template name

    def test_template_content(self):
        # Test if the content is rendered correctly in the template
        response = self.client.get(reverse('home'))  # 'home' should match your URL name
        self.assertContains(response, "this is a test")  # Check that the text appears in the rendered template
