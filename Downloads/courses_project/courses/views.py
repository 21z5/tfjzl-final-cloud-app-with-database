from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Category, Enrollment, Submission, Choice


def course_list(request):
    courses = Course.objects.filter(is_published=True)
    category_slug = request.GET.get("category")
    if category_slug:
        courses = courses.filter(category__slug=category_slug)
    categories = Category.objects.all()
    context = {"courses": courses, "categories": categories}
    return render(request, "courses/course_list.html", context)


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug, is_published=True)
    is_enrolled = False
    if request.user.is_authenticated:
        is_enrolled = Enrollment.objects.filter(student=request.user, course=course).exists()
    context = {"course": course, "is_enrolled": is_enrolled}
    return render(request, "courses/course_detail.html", context)


@login_required
def enroll(request, slug):
    course = get_object_or_404(Course, slug=slug, is_published=True)
    Enrollment.objects.get_or_create(student=request.user, course=course)
    messages.success(request, f"تم تسجيلك في كورس: {course.title}")
    return redirect("course_detail", slug=course.slug)


@login_required
def my_courses(request):
    enrollments = Enrollment.objects.filter(student=request.user).select_related("course")
    return render(request, "courses/my_courses.html", {"enrollments": enrollments})


@login_required
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    enrollment = get_object_or_404(Enrollment, student=request.user, course=course)
    if request.method == "POST":
        submission = Submission.objects.create(enrollment=enrollment)
        choice_ids = request.POST.getlist("choice")
        for choice_id in choice_ids:
            choice = Choice.objects.get(pk=choice_id)
            submission.choices.add(choice)
        return redirect("show_exam_result", course_id=course.id, submission_id=submission.id)
    return redirect("course_detail", slug=course.slug)


@login_required
def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)

    selected_choices = submission.choices.all()
    selected_ids = [choice.id for choice in selected_choices]

    total_score = 0
    possible = 0
    for question in course.question_set.all():
        possible += question.grade
        if question.is_get_score(selected_ids):
            total_score += question.grade

    context = {
        "course": course,
        "submission": submission,
        "selected_ids": selected_ids,
        "possible": possible,
        "grade": total_score,
    }
    return render(request, "courses/exam_result_bootstrap.html", context)