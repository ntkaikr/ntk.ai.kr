import requests
from django.shortcuts import render

CURRENCIES = ["USD", "KRW", "JPY", "EUR", "GBP", "CNY", "AUD", "CAD", "CHF", "SGD"]

def exchanger_view(request):
    result = None
    error = None

    if request.method == "GET" and "amount" in request.GET:
        try:
            amount = float(request.GET.get("amount", 1))
            from_curr = request.GET.get("from_currency")
            to_curr = request.GET.get("to_currency")

            if from_curr == to_curr:
                error = "같은 통화 간 변환은 의미가 없습니다."
            else:
                url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_curr}&to={to_curr}"
                response = requests.get(url, timeout=5)
                data = response.json()
                converted = data["rates"].get(to_curr)
                if converted:
                    result = {
                        "amount": amount,
                        "from": from_curr,
                        "to": to_curr,
                        "rate": converted,
                        "converted": converted,
                        "date": data["date"]
                    }
                else:
                    error = "환율 데이터가 정확히 존재하지 않습니다."
        except Exception:
            error = "API 요청 중 오류가 발생했습니다."

    return render(request, "exchanger/index.html", {
        "currencies": CURRENCIES,
        "result": result,
        "error": error,
    })
