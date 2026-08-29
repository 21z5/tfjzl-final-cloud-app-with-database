from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_courses = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Learner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=100, default='student')
    social_link = models.URLField(blank=True)

    def __str__(self):
        return self.user.username


class Course(models.Model):
    title = models.CharField(max_length=200, default='online course')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True)
    level = models.CharField(max_length=50, default='Beginner')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    is_published = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=200, default='lesson')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateField(auto_now_add=True)


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    grade = models.IntegerField(default=5)

    def __str__(self):
        return self.content

    def is_get_score(self, selected_ids):
        all_answers = self.choice_set.filter(is_correct=True)
        selected_correct = self.choice_set.filter(id__in=selected_ids, is_correct=True)
        if all_answers.count() == selected_correct.count() and selected_ids.count() == selected_correct.count():
            return True
        return False


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.content


class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)
    pub_date = models.DateTimeField(auto_now_add=True)