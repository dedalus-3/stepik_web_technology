from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Question
from .forms import AnswerForm, AskForm, RegisterUserForm, LoginUserForm


@require_GET
def AllNewQuestion(request):
    """ Выдает список вопросов, отсортированных по дате добавления.
        С использованием пагинации на странице"""
    questions_list = Question.objects.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions_list, limit)
    paginator.baseurl = '/?page='
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    return render(request, 'questions/list_new.html', {
        'questions': questions,
        'paginator': paginator,
        'page': page,
    })

@require_GET
def AllPopularQuestion(request):
    """ Выдает список вопросов, отсортированных по рейтингу.
            С использованием пагинации на странице"""
    questions_list = Question.objects.popular()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions_list, limit)
    paginator.baseurl = '/?page='
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    return render(request, 'questions/list_popular.html', {
        'questions': questions,
        'paginator': paginator,
        'page': page,
    })

def QuestionDetail(request, id):
    """ Контроллер страницы вопроса со списком комментариев и
        возможностью добавления нового комментария, который будет
            сразу отображаться. """
    question = get_object_or_404(Question, id=id)
    answers = question.answer.all()
    new_answer = None
    if request.method == 'POST':
        if request.user.is_authenticated():
            answer_form = AnswerForm(data=request.POST, initial={'question': question})
            if answer_form.is_valid():
                new_answer = answer_form.save(commit=False)
                new_answer.author = request.user
                new_answer.save()
                return HttpResponseRedirect('')
        else:
            return HttpResponseRedirect('../../login/')
    else:
        answer_form = AnswerForm(initial={'question': question})
    return render(request, 'questions/question_detail.html', {
        'question': question,
        'answers': answers,
        'new_answer': new_answer,
        'answer_form': answer_form
    })


def CreateAsk(request):
    """ Контроллер по созданию вопроса """
    if request.method == 'POST':
        ask_form = AskForm(data=request.POST)
        if ask_form.is_valid():
            ask = ask_form.save(commit=False)
            ask.author = request.user
            ask.save()
            return HttpResponseRedirect('../'+ask.get_absolute_url())
    else:
        ask_form = AskForm()
    return render(request, 'questions/create_question.html', {
        'ask_form': ask_form
    })

def Signup(request):
    """ Контроллер по регистрации пользователя с использованием
        автоматического входа и редиректа на домашнюю страницу """
    if request.method == 'POST':
        register_user_form = RegisterUserForm(data=request.POST)
        if register_user_form.is_valid():
            new_user = register_user_form.save(commit=False)
            new_user.set_password(register_user_form.cleaned_data['password'])
            new_user.save()
            user = authenticate(username=new_user.username, password=register_user_form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        register_user_form = RegisterUserForm()
    return render(request, 'questions/authentication/signup.html', {
        'register_user_form': register_user_form
    })

def Login(request):
    """ Контроллер по входу под своим профилем """
    if request.method == 'POST':
        login_form = LoginUserForm(data=request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
    else:
        login_form = LoginUserForm()
    return render(request, 'questions/authentication/login.html', {
        'login_form': login_form
    })