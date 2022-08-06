def most_frequent():
  x=(input("enter a string:"))
  for letter in set(x):
    print (letter, '=',  x.count(letter))

most_frequent()    