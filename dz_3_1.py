import os
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

def copy_file(file_path, dest_dir):
    # Отримання розширення файлу
    file_extension = file_path.suffix[1:]  # видаляємо крапку з розширення
    # Створення директорії для розширення, якщо вона не існує
    target_dir = dest_dir / file_extension
    target_dir.mkdir(parents=True, exist_ok=True)
    # Копіювання файлу
    shutil.copy2(file_path, target_dir / file_path.name)

def process_directory(src_dir, dest_dir):
    with ThreadPoolExecutor() as executor:
        for root, _, files in os.walk(src_dir):
            for file in files:
                file_path = Path(root) / file
                executor.submit(copy_file, file_path, dest_dir)

def main():
    # Зчитування аргументів командного рядка
    if len(sys.argv) < 2:
        print("Вкажіть шлях до директорії з файлами для обробки.")
        sys.exit(1)

    src_dir = Path(sys.argv[1])
    dest_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")

    if not src_dir.is_dir():
        print(f"Директорія {src_dir} не існує.")
        sys.exit(1)

    dest_dir.mkdir(parents=True, exist_ok=True)

    # Обробка директорії
    process_directory(src_dir, dest_dir)

if __name__ == "__main__":
    main()

#Для запуску програми потрібно вказати шлях до директорії з файлами для обробки шлях до цільової директорі
#приклад використання для директорії D:\9775
#python dz_3_1.py D:\9775 D:\HW_3_1
