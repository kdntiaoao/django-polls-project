from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]


index = IndexView.as_view()


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


detail = DetailView.as_view()


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


results = ResultsView.as_view()


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        context = {"question": question, "error_message": "選択肢を選んでください。"}
        return render(request, "polls/detail.html", context)
    else:
        selected_choice.votes += 1
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
