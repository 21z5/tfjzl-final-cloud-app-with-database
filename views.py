from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, Submission, Choice, Enrollment, Question

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    user = request.user
    enrollment = Enrollment.objects.get(user=user, course=course)
    submission = Submission.objects.create(enrollment=enrollment)
    choices = extract_answers(request)
    submission.choices.set(choices)
    submission_id = submission.id
    return HttpResponseRedirect(reverse(viewname='onlinecourse:show_exam_result', args=[course_id, submission_id]))

def extract_answers(request):
    submitted_answers = []
    for key in request.POST:
        if key.startswith('choice'):
            value = request.POST[key]
            choice_id = int(value)
            submitted_answers.append(choice_id)
    return submitted_answers

def show_exam_result(request, course_id, submission_id):
    context = {}
    course = get_object_or_404(Course, pk=course_id)
    submission = Submission.objects.get(pk=submission_id)
    choices = submission.choices.all()
    
    # حساب مجموع الدرجات لكل الأسئلة في الكورس (الـ possible)
    total_possible = 0
    questions = course.question_set.all()
    for question in questions:
        total_possible += question.grade

    # حساب درجات إجابات الطالب الصحيحة (الـ grade)
    total_score = 0
    for choice in choices:
        if choice.is_correct:
            total_score += choice.question.grade

    context['course'] = course
    context['submission'] = submission
    context['grade'] = total_score
    context['possible'] = total_possible
    context['choices'] = choices
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
