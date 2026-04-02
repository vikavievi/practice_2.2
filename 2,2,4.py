import requests

BASE_URL = "https://api.github.com"

def get_user_profile(username):
    url = f"{BASE_URL}/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"ПРОФИЛЬ ПОЛЬЗОВАТЕЛЯ: {username}")
        print(f"Имя: {data.get('name', 'Не указано')}")
        print(f"Ссылка на профиль: {data['html_url']}")
        print(f"Количество репозиториев: {data['public_repos']}")
        print(f"Количество обсуждений: {data.get('public_gists', 0)}")
        print(f"Количество подписок: {data['following']}")
        print(f"Количество подписчиков: {data['followers']}")

    else:
        print(f"Ошибка! Пользователь '{username}' не найден")


def get_user_repos(username):
    url = f"{BASE_URL}/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        repos = response.json()
        print(f" РЕПОЗИТОРИИ ПОЛЬЗОВАТЕЛЯ: {username}")

        if not repos:
            print("Нет репозиториев")
            return

        for i, repo in enumerate(repos, 1):
            print(f"\n{i}. {repo['name']}")
            print(f"Ссылка: {repo['html_url']}")
            print(f"Язык: {repo.get('language', 'Не указан')}")
            print(f"Видимость: {'Публичный' if not repo['private'] else 'Приватный'}")
            print(f"Ветка по умолчанию: {repo['default_branch']}")
            print(f"   Количество просмотров: Требует авторизации")
    else:
        print(f" Не удалось получить репозитории пользователя '{username}'")


def search_repos_by_name(search_query):
    url = f"{BASE_URL}/search/repositories"
    params = {"q": search_query, "sort": "stars", "order": "desc"}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f" РЕЗУЛЬТАТЫ ПОИСКА: '{search_query}'")


        if data['total_count'] == 0:
            print("Ничего не найдено")
            return

        print(f"Найдено: {data['total_count']} репозиториев\n")

        for i, repo in enumerate(data['items'][:10], 1):
            print(f"{i}. {repo['name']}")
            print(f"   Владелец: {repo['owner']['login']}")
            print(f"   Ссылка: {repo['html_url']}")
            print(f"   Язык: {repo.get('language', 'Не указан')}")
            print(f"   Звёзд: {repo['stargazers_count']}")

    else:
        print(" Ошибка при поиске")


def main():
    print("GitHub приложение")

    while True:
        print("\nМЕНЮ:")
        print("1) Просмотр профиля пользователя")
        print("2️) Получение всех репозиториев пользователя")
        print("3️) Поиск репозиториев по названию")
        print("4️) Выход")

        choice = input("\nВыберите действие (1-4): ")

        if choice == '1':
            username = input("Введите имя пользователя GitHub: ")
            get_user_profile(username)

        elif choice == '2':
            username = input("Введите имя пользователя GitHub: ")
            get_user_repos(username)

        elif choice == '3':
            search_term = input("Введите название для поиска: ")
            search_repos_by_name(search_term)

        elif choice == '4':
            print("До свидания!")
            break

        else:
            print("Неверный выбор! Попробуйте снова.")

        input("\nНажмите Enter, чтобы продолжить.")

if __name__ == "__main__":
    main()