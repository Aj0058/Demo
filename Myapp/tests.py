from django.test import TestCase
from Myapp.models import Feedback

class FeedbackModelTest(TestCase):
    def setUp(self):
        # Create a sample Feedback object
        Feedback.objects.create(
            Name2="Ayush Singh",
            Email2="AyushSingh@gmail.com",
            Phone2="8949167574",
            Product2="IFB Fridge",
            Message2="Hii"
        )

    def test_feedback_creation(self):
        """Test if Feedback object is created properly."""
        feedback = Feedback.objects.get(Name2="Ayush Singh")
        self.assertEqual(feedback.Email2, "AyushSingh@gmail.com")
        self.assertEqual(feedback.Phone2, "8949167574")
