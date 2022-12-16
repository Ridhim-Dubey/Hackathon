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
count()
test()
end()
