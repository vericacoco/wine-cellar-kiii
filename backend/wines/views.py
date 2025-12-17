from django.shortcuts import render, redirect
from .mongo import wines_collection


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
