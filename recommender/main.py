from fastapi import FastAPI

app = FastAPI(title="Wine Recommendation Service")


@app.get("/recommend")
def recommend_wine(wine_type: str = "red"):
    if wine_type.lower() == "red":
        recommendation = "Cabernet Sauvignon"
    elif wine_type.lower() == "white":
        recommendation = "Chardonnay"
    else:
        recommendation = "Pinot Noir"

    return {
        "recommended_wine": recommendation
    }
