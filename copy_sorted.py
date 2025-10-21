import os
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor

def copy_file(file_path, target_dir):
    ext = os.path.splitext(file_path)[1][1:].lower()  
    if not ext: 
        return
    ext_dir = os.path.join(target_dir, ext)
    os.makedirs(ext_dir, exist_ok=True)  
    shutil.copy2(file_path, ext_dir) 

def process_directory(source_dir, target_dir):
    with ThreadPoolExecutor() as executor:
        for root, _, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                executor.submit(copy_file, file_path, target_dir)

def main():
    if len(sys.argv) < 2:
        print("Использование: python main.py <source_dir> [target_dir]")
        sys.exit(1)

    source_dir = sys.argv[1]
    target_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    if not os.path.exists(source_dir):
        print(f"Ошибка: Директория {source_dir} не существует.")
        sys.exit(1)

    os.makedirs(target_dir, exist_ok=True) 
    process_directory(source_dir, target_dir)
    print(f"Файлы скопированы и отсортированы в {target_dir}.")

if __name__ == "__main__":
    main()