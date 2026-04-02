import urllib.request
import urllib.error

urls = [
    "https://github.com/",
    "https://www.binance.com/en",
    "https://tomtit.tomsk.ru/",
    "https://jsonplaceholder.typicode.com/",
    "https://moodle.tomtit-tomsk.ru/"
]

for url in urls:
    try:
        response = urllib.request.urlopen(url, timeout=10)

        status_code = response.getcode()

        if status_code == 200:
            status = "доступен"
        elif status_code == 404:
            status = "не найден"
        elif status_code == 403:
            status = "вход запрещен"
        else:
            status = "доступен"

        print(f"{url} – {status} – {status_code}")

    except urllib.error.HTTPError as e:
        status_code = e.code

        if status_code == 404:
            status = "не найден"
        elif status_code == 403:
            status = "вход запрещен"
        elif 500 <= status_code < 600:
            status = "не доступен"
        else:
            status = "не доступен"

        print(f"{url} – {status} – {status_code}")

    except urllib.error.URLError:
        print(f"{url} – не доступен – ошибка подключения")

    except Exception:
        print(f"{url} – не доступен – неизвестная ошибка")

input("\nНажмите Enter для выхода...")