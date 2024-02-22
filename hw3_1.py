import os
import shutil
import argparse

def copy_files(src_dir, dest_dir):
    try:
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)
            if os.path.isfile(item_path):
                file_extension = os.path.splitext(item)[1][1:]
                new_dir = os.path.join(dest_dir, file_extension)
                os.makedirs(new_dir, exist_ok=True)
                shutil.copy(item_path, new_dir)
            elif os.path.isdir(item_path):
                copy_files(item_path, dest_dir)
    except Exception as e:
        print(f"Помилка при копіюванні файлів: {e}")

def main():
    parser = argparse.ArgumentParser(description='Копіювання файлів з однієї директорії до іншої.')
    parser.add_argument('src_dir', type=str, help='Шлях до вихідної директорії')
    parser.add_argument('dest_dir', type=str, nargs='?', default='dist', help='Шлях до директорії призначення')
    args = parser.parse_args()

    copy_files(args.src_dir, args.dest_dir)

if __name__ == "__main__":
    main()