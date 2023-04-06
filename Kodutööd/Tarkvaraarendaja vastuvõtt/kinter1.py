from tkinter import *
from tkinter import ttk
from random import choice, randint
from random import *

# Создаем пустые списки для правильных и неправильных ответов
vastuvõetud = []
eisoobi = []

def show_questionnaire(name):
    def create_question_frame(question_num):
        nonlocal correct_answers_count
        with open("kusimused_vastused.txt", "r") as f:
            all_lines = f.readlines()
            questions = [line.split(':')[0].strip() for line in all_lines]
            answers = [line.split(':')[1].strip() for line in all_lines]

        random_index = randint(0, len(questions)-1)
        random_question = questions[random_index]
        correct_answer = answers[random_index]

        def next_question():
            nonlocal correct_answers_count
            user_answer = entry.get()
            print(f"{name} vastas küsimusele {question_num}: {user_answer}")
            if user_answer.lower() == correct_answer.lower():
                print("Õige vastus!")
                correct_answers_count += 1
            else:
                print("Vale vastus.")
                print(f"Õige vastus on: {correct_answer}")
                answers_list.append(user_answer)
                question_frame.pack_forget()
            if question_num < 5:
                create_question_frame(question_num + 1)
            else:
                if correct_answers_count >= 3:
                    vastuvõetud.append(name)
                else:
                    eisoobi.append(name)
                questionnaire_window.destroy()
                ttk.Label(root, text=f"{name}, sa vastasid õigesti {correct_answers_count} küsimusele.").pack()

        question_frame = ttk.Frame(questionnaire_window, padding=10)
        question_frame.pack()

        ttk.Label(question_frame, text=f"Küsimus {question_num}: {random_question}").pack()
        entry = ttk.Entry(question_frame)
        entry.pack()

        ttk.Button(question_frame, text="Saada", command=next_question).pack()

    correct_answers_count = 0
    answers_list = []

    questionnaire_window = Toplevel(root)
    questionnaire_window.title("Küsitlus")

    create_question_frame(1)

def start_questionnaire():
    name = name_entry.get()
    name_window.destroy()
    show_questionnaire(name)

# Сортируем списки принятых и не принятых соискателей
vastuvõetud.sort(key=lambda x: x[1], reverse=True)
eisoobi.sort()

# Создаем файлы с правильными и неправильными ответами
with open('vastuvõetud.txt', 'w+') as file:
    for nimi, punktid in vastuvõetud:
        file.write(f'{nimi}: {punktid}\n')

with open('eisoobi.txt', 'w+') as fail:
    for nimi, punktid in vastuvõetud:
        fail.write(f'{nimi}: {punktid}\n')


root = Tk()
root.title("Tarkvara vastuvõtt")
root.geometry("400x200")
frm = ttk.Frame(root, padding=20)
menu = Menu(root)
root.config(menu=menu)
m1 = Menu(menu)
menu.add_cascade(label="Tabs", menu=m1)
m1.add_command(label="Card1", accelerator="Command+A", command=lambda: new_window(0))
m1.add_command(label="Card2", accelerator="Command+B", command=lambda: new_window(1))
m1.add_command(label="Card3", accelerator="Command+C", command=lambda: new_window(2))
m1.add_command(label="Card4", accelerator="Command+D", command=lambda: new_window(3))

ttk.Label(frm, text="Tere taotleja!").pack()
ttk.Button(frm, text="Quit", command=root.destroy).pack()
btn = Button(frm, text="Alusta küsitlust!", font="Comic_Sans_MS 15", fg="White", bg="#148038",
             relief=GROOVE, width=15, height=2, command=lambda: name_window.deiconify())

frm.pack()
btn.pack()

# Создаем окно для ввода имени
name_window = Toplevel(root)
name_window.title("Sisestage oma nimi")
name_label = ttk.Label(name_window, text="Sisestage oma nimi:")
name_label.pack()
name_entry = ttk.Entry(name_window)
name_entry.pack()
start_button = ttk.Button(name_window, text="Alusta", command=start_questionnaire)
start_button.pack()
name_window.withdraw()

root.mainloop()

