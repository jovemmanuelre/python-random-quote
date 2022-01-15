import random
def primary():
  f = open("python-random-quote/quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 3
  rnd = random.randint(0, last)
  rnd1 = random.randint(0,last)
  print(quotes[rnd],quotes[rnd1],end='',)

if __name__== "__main__":
  primary()