def greet(bot_name, birth_year):
  print("Hello! My name is {0}.".format(bot_name))
  print("I was created {0}.".format(birth_year))


def remind_name():
  print('Please, remind me your name.')
  name = input()
  print("What a great name you have, {0}!".format(name))


def guess_age():
  print('Please tell me your age.')

  rem3 = int(input())
  age = (rem3)
  if age < 100:
    print(
      "Your age is {0}; that's a good time to start programming!".format(age))
  else:
    print("You are a ghost!!! I have to run away from you!!!")


def count():
  print('Now I will prove to you that I can count to any number you want.')
  num = int(input())

  counter = 0
  while counter <= num:
    print("{0} !".format(counter))
    counter += 1

def game():
  import tkinter
  import random
  w=input("Would you like to play game?")
  if w=='Yes' or w=='yes':
    root = tkinter.Tk()
    root.title("JANKEN by EXON")
    root.geometry("400x400")
    random_num = random.randint(1, 3)
    if random_num == 1:
      comp_choice = "R"
    elif random_num == 2:
      comp_choice = "P"
    elif random_num == 3:
      comp_choice = "S"

    # create functions
    def rock():
      label_user_choice["text"] = "ROCK"
      if comp_choice == "R":
        label_result["text"] == "🤝TIE🤝"
        label_comp_choice["text"] = "ROCK"
      elif comp_choice == "P":
        label_result["text"] = "😅!!COMPUTER WINS !!😅"
        label_comp_choice["text"] = "PAPER"
      elif comp_choice == "S":
        label_result["text"] = "🥳!!PLAYER WINS!!🥳"
        label_comp_choice["text"] = "SCISSORS"

    def paper():
      label_user_choice["text"] = "PAPER"
      if comp_choice == "P":
        label_result["text"] = "🤝TIE🤝"
        label_comp_choice["text"] = "PAPER"
      elif comp_choice == "R":
        label_result["text"] = "🥳!!PLAYER WINS!!🥳"
        label_comp_choice["text"] = "ROCK"
      elif comp_choice == "S":
        label_result["text"] = "😅!!COMPUTER WINS !!😅"
        label_comp_choice["text"] = "SCISSORS"

    def scissors():
      label_user_choice["text"] = "SCISSORS"
      if comp_choice == "S":
        label_result["text"] = "🤝TIE🤝"
        label_comp_choice["text"] = "SCISSORS"
      elif comp_choice == "R":
        label_result["text"] = "😅!!COMPUTER WINS !!😅"
        label_comp_choice["text"] = "ROCK"
      elif comp_choice == "P":
        label_result["text"] = "🥳!!PLAYER WINS!!🥳"
        label_comp_choice["text"] = "PAPER"

    def reset():
      global comp_choice
      if random_num == 1:
        comp_choice = "R"
      elif random_num == 2:
        comp_choice = "P"
      elif random_num == 3:
        comp_choice = "S"
      label_comp_choice["text"] = ""
      label_user_choice["text"] = ""
      label_result["text"] = "..CHOOSE.."

  # create widgets

    label_result = tkinter.Label(root, text="...CHOOSE...")
    label_result.pack()
    button_rock = tkinter.Button(root, text="☄️ROCK☄️", command=rock)
    button_rock.pack()
    button_paper = tkinter.Button(root, text="📄PAPER📄", command=paper)
    button_paper.pack()
    button_scissors = tkinter.Button(root, text="✂️SCISSORS✂️", command=scissors)
    button_scissors.pack()
    label_comp_choice = tkinter.Label(root, justify=tkinter.LEFT, font="Courier", text="")
    label_comp_choice.pack()
    label_user_choice = tkinter.Label(root, justify=tkinter.LEFT, font="Courier", text="")
    label_user_choice.pack()
    button_reset = tkinter.Button(root, text="RESET", command=reset)
    button_reset.pack()

    root.mainloop()
  else:
    print('Okay 😊')
def test():
  print("do you want to tell me about your day?")
  print("How was your day?")
  day = input()
  if day == 'sad' or day=='boring' or day=='not good' or day=='bad':
      print(
      "I hope it will be fine. There is many ups and down in your life but always remeber we have to keep ourself happy in every moment."
    )
  else:
    print("Great!")


def end():
  print('Have a nice day!')



greet('Sympathy bot', 'by Team-EXON')
remind_name()
guess_age()
game()
count()
test()
end()
