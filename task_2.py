import psutil
import time

def show_system_info():

    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"Загрузка CPU: {cpu_percent}%")

    memory = psutil.virtual_memory()
    print(f"Использовано RAM: {memory.used / (1024 ** 3):.1f} ГБ из {memory.total / (1024 ** 3):.1f} ГБ")
    print(f"Загрузка RAM: {memory.percent}%")

    disk = psutil.disk_usage('/')
    print(f"Загрузка диска: {disk.percent}%")
    print(f"Свободно на диске: {disk.free / (1024 ** 3):.1f} ГБ из {disk.total / (1024 ** 3):.1f} ГБ")

if __name__ == "__main__":
    print("СИСТЕМНЫЙ МОНИТОР")
    print("Для выхода нажмите Ctrl+C\n")

    try:
        while True:
            show_system_info()
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nПрограмма завершена")