import requests

def exchange_rate(currency_from, currency_to, amount=1):
    """
    Funkcja zwraca wartość jednej waluty w drugiej walucie na podstawie kursów z API NBP
    :param currency_from: Kod waluty, z której chcemy przeliczyć wartość (np. 'EUR')
    :param currency_to: Kod waluty, na którą chcemy przeliczyć wartość (np. 'USD')
    :param amount: Wartość waluty, którą chcemy przeliczyć (domyślnie 1)
    :return: Wartość waluty przeliczonej na drugą walutę
    """
    if currency_from == 'PLN':
        rate_from = 1
    # Utworzenie adresu URL z danymi dotyczącymi kursów walut
    else:
        url_from = f"https://api.nbp.pl/api/exchangerates/rates/a/{currency_from}/?format=json"

        # Wysłanie żądania do API i pobranie danych
        response = requests.get(url_from)
        data_from = response.json()

        # Wyciągnięcie aktualnego kursu waluty z danych

        rate_from = data_from['rates'][0]['mid']

    url_to = f"https://api.nbp.pl/api/exchangerates/rates/a/{currency_to}/?format=json"

    if currency_to == 'PLN':
        result = rate_from * amount # Kurs waluty w złotych
    else:
        # Wysłanie żądania do API i pobranie danych
        response = requests.get(url_to)
        data_to = response.json()

        rate_to = data_to['rates'][0]['mid']

        result = amount * (rate_from / rate_to)

    return round(result, 2)

print(exchange_rate('EUR', 'USD', 100))