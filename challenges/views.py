from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

challenges_by_month = dict(
    january="January: Eat fruits all days",
    february="February: Walk for 20 min every day",
    march="March: Learn django",
    april="April: Eat fruit",
    may="May: Walk",
    june="June: Eat no meat",
    july="July: challenge",
    august="August: Walk to work",
    september="September: Learn Flask",
    october="October: Eat no meat",
    november="November: Eat fruit",
    december="December: Wrap up django"
)


def index(request):
    # list_items = [
    #     f"<li><a href='{month}'>{month.capitalize()}</a></li>" for month in list(challenges_by_month.keys())
    # ]

    # return HttpResponse(f"<ul>{''.join(list_items)}</ul>")

    context = dict(
        months=list(challenges_by_month.keys())
    )

    return render(request, "challenges/index.html", context)


def monthly_challenge_by_number(request, month):
    months = list(challenges_by_month.keys())
    try:
        forward_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[forward_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("Invalid")


def monthly_challenge(request, month):
    try:

        context = dict(
            month=month,
            challenge_text=challenges_by_month[month]
        )

        response_data = render(request, "challenges/challenge.html", context)
        return HttpResponse(response_data)
    except:
        response_data = render_to_string("404.html", context={"month": month})
        return HttpResponseNotFound(response_data)
