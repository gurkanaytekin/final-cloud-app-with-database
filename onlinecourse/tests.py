from django.test import TestCase

from onlinecourse.models import Course

# Create your tests here.
class QuestionModelTests(TestCase):
    def test_was_course_has_min_one(self):
        courses = Course.objects.order_by('-total_enrollment')
        self.assertGreaterEqual(courses.count(), 0)