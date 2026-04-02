import json
import urllib.request

URL = "https://www.cbr-xml-daily.ru/daily_json.js"

def load_rates():
    try:
        with urllib.request.urlopen(URL) as response:
            data = json.loads(response.read())
            return data["Valute"]
    except:
        print("Ошибка загрузки курсов! Проверьте интернет.")
        return None


def show_all_currencies(rates):
    if not rates:
        return
    print("\nВСЕ ВАЛЮТЫ")
    for code, info in rates.items():
        print(f"{code}: {info['Name']} - {info['Value']} RUB")

def show_currency_by_code(rates, code):
    if not rates:
        return
    code = code.upper()
    if code in rates:
        info = rates[code]
        print(f"\n{code}: {info['Name']} - {info['Value']} RUB")
    else:
        print(f"Валюта с кодом {code} не найдена!")

def load_groups():
    try:
        with open("save.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return {}

def save_groups(groups):
    with open("save.json", "w", encoding="utf-8") as file:
        json.dump(groups, file, ensure_ascii=False, indent=2)

def show_all_groups(groups):
    if not groups:
        print("\nНет созданных групп!")
        return
    print("\nВСЕ ГРУППЫ")
    for group_name, currencies in groups.items():
        print(f"\nГруппа '{group_name}':")
        if currencies:
            for code in currencies:
                print(f"  - {code}")
        else:
            print("  (пусто)")


def show_group(groups, rates, group_name):
    if group_name not in groups:
        print(f"Группа '{group_name}' не найдена!")
        return

    currencies = groups[group_name]
    if not currencies:
        print(f"Группа '{group_name}' пуста!")
        return

    print(f"\nКУРСЫ В ГРУППЕ '{group_name}'")
    for code in currencies:
        if code in rates:
            info = rates[code]
            print(f"{code}: {info['Name']} - {info['Value']} RUB")
        else:
            print(f"{code}: (не найден в текущих курсах)")


def create_group(groups):
    name = input("Введите имя новой группы: ")
    if name in groups:
        print("Группа с таким именем уже существует!")
        return
    groups[name] = []
    save_groups(groups)
    print(f"Группа '{name}' создана!")


def add_currency_to_group(groups, rates):
    if not groups:
        print("Сначала создайте хотя бы одну группу!")
        return

    print("Доступные группы:", ", ".join(groups.keys()))
    group_name = input("Введите имя группы: ")

    if group_name not in groups:
        print("Группа не найдена!")
        return

    code = input("Введите код валюты (например, USD, EUR): ").upper()
    if code not in rates:
        print("Валюта с таким кодом не найдена!")
        return

    if code in groups[group_name]:
        print("Такая валюта уже есть в группе!")
        return

    groups[group_name].append(code)
    save_groups(groups)
    print(f"Валюта {code} добавлена в группу '{group_name}'!")


def remove_currency_from_group(groups):
    if not groups:
        print("Нет созданных групп!")
        return

    print("Доступные группы:", ", ".join(groups.keys()))
    group_name = input("Введите имя группы: ")

    if group_name not in groups:
        print("Группа не найдена!")
        return

    if not groups[group_name]:
        print("В этой группе нет валют!")
        return

    print(f"Валюты в группе '{group_name}':", ", ".join(groups[group_name]))
    code = input("Введите код валюты для удаления: ").upper()

    if code in groups[group_name]:
        groups[group_name].remove(code)
        save_groups(groups)
        print(f"Валюта {code} удалена из группы '{group_name}'!")
    else:
        print("Такой валюты нет в этой группе!")


def main_menu():
    groups = load_groups()

    while True:
        print("ПРОГРАММА МОНИТОРИНГА КУРСОВ ВАЛЮТ")
        print("1. Показать все валюты")
        print("2. Показать курс конкретной валюты")
        print("3. Создать группу валют")
        print("4. Показать все группы")
        print("5. Показать курсы из группы")
        print("6. Добавить валюту в группу")
        print("7. Удалить валюту из группы")
        print("8. Выйти")

        choice = input("Выберите действие (1-8): ")

        if choice == "1":
            rates = load_rates()
            show_all_currencies(rates)

        elif choice == "2":
            rates = load_rates()
            if rates:
                code = input("Введите код валюты (например, USD): ")
                show_currency_by_code(rates, code)

        elif choice == "3":
            create_group(groups)

        elif choice == "4":
            show_all_groups(groups)

        elif choice == "5":
            rates = load_rates()
            if rates and groups:
                name = input("Введите имя группы: ")
                show_group(groups, rates, name)
            elif not groups:
                print("Нет созданных групп!")

        elif choice == "6":
            rates = load_rates()
            if rates:
                add_currency_to_group(groups, rates)

        elif choice == "7":
            remove_currency_from_group(groups)

        elif choice == "8":
            print("До свидания!")
            break

        else:
            print("Неверный выбор! Попробуйте снова.")

if __name__ == "__main__":
    main_menu()