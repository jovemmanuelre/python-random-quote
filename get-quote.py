import random
def primary():
  f = open("python-random-quote/quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 3
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  primary()