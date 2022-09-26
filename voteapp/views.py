from django.shortcuts import render, Http404, get_object_or_404, HttpResponseRedirect
from django.http import  JsonResponse
from django.urls import reverse
from .models import Award, Choice, Triva
import random, math

rand = random.randrange(1,2)

def home(request):
    award = Award.objects.all()
    artnum = 2
    context = {
        'award':award,
        'artnum': artnum
    }
    return render(request,  "index.html", context)


# For the voting of the artist 
def vote(request, award_id):
    triva = Triva.objects.get(id=rand)
    try:
        award = Award.objects.get(pk=award_id)
        c = Choice.objects.filter(award_id=award_id)
    except Award.DoesNotExist:
        raise Http404("Award Category Does Not Exist")
    context = {
        'award': award,
        'c': c,
        'triva':triva
    }
    return render(request, 'vote.html', context)

# function for the saving of the votes on submitting the form
def voteSave(request):
    award_id = request.POST.get('award_id')
    award = get_object_or_404(Award, pk=award_id)
    try:
        select = request.POST.get('artist')
        artist_select = Choice.objects.get(pk=select)
    except (KeyError, Choice.DoesNotExist):
        context = {
            'award': award,
            'error_message': 'You didnt Select any choice'
        }
        return render(request, 'vote.html')
    else:
        artist_select.votes += 1
        artist_select.save()
    return HttpResponseRedirect(award_id+"/results")

# Displaying the results of the voting of the artists
def result(request, award_id):
    triva = Triva.objects.get(id=rand)
    award = get_object_or_404(Award, pk=award_id)
    c = Choice.objects.filter(award_id=award_id)
    context = {
        'award': award,
        'c':c,
        'triva': triva
        }
    return render(request, "results.html", context)


# Creating an api endpoint for grabing the data of the awards
def resultsData(request, data_id):
    voteData = []
    award = get_object_or_404(Award, pk=data_id)
    votes = Choice.objects.filter(award_id=data_id)

    for item in votes:
        voteData.append({item.artist:item.votes})
    
    print(voteData)
    return JsonResponse(voteData, safe=False)

# about us page
def aboutUs(request):
    triva = Triva.objects.get(id=rand)
    context = {
        'triva': triva
        }
    return render(request, "about.html", context)