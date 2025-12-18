from django.shortcuts import render, redirect
from .mongo import wines_collection
import os
import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .mongo import wines_collection

RECOMMENDER_URL = os.environ.get("RECOMMENDER_URL", "http://recommender:8001")

def recommend(request):
    wine_type = request.GET.get("type", "red")

    r = requests.get(
        f"{RECOMMENDER_URL}/recommend",
        params={"wine_type": wine_type},
        timeout=5
    )
    r.raise_for_status()
    return JsonResponse(r.json())



def wine_list(request):
    wines = list(wines_collection.find())

    if request.method == "POST":
        wine = {
            "name": request.POST.get("name"),
            "wine_type": request.POST.get("wine_type"),
            "year": int(request.POST.get("year")),
            "region": request.POST.get("region"),
            "quantity": int(request.POST.get("quantity")),
        }
        wines_collection.insert_one(wine)
        return redirect("wine_list")

    return render(request, "wines/wine_list.html", {"wines": wines})
