import json
import os
from datetime import datetime

# Файл для сохранения заметок
NOTES_FILE = "notes.json"

def load_notes():
    """Загружает заметки из файла JSON."""
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            return json.load(file)
    else:
        return []

def save_notes(notes):
    """Сохраняет заметки в файл JSON."""
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

def add_note():
    """Добавляет новую заметку."""
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"id": len(notes) + 1, "title": title, "body": body, "timestamp": timestamp}
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно добавлена.")

def list_notes():
    """Выводит список всех заметок."""
    if notes:
        for note in notes:
            print(f"{note['id']}. {note['title']} - {note['timestamp']}")
    else:
        print("Список заметок пуст.")

def edit_note():
    """Редактирует существующую заметку."""
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            note['title'] = input("Введите новый заголовок заметки: ")
            note['body'] = input("Введите новый текст заметки: ")
            note['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована.")
            return
    print("Заметка с указанным ID не найдена.")

def delete_note():
    """Удаляет существующую заметку."""
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена.")
            return
    print("Заметка с указанным ID не найдена.")

# Загрузка заметок из файла
notes = load_notes()

# Главный цикл программы
while True:
    print("\nМеню:")
    print("1. Добавить заметку")
    print("2. Список заметок")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        list_notes()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")