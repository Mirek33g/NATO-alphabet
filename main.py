import csv

with open("nato_phonetic_alphabet.csv") as nato:
  data = csv.reader(nato)
  dic = {key: value for (key, value) in data}

name = input("Enter a word: ").upper()


done = [dic[l] for l in name]

print(done)

