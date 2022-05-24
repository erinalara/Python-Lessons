

def word(w):

  i = 0
  for j in range(len(w)-1, -1, -1):
    if w[j] != w[i]:
      return False
    i = i+1
  return True

def main():
  string = input("input word\n")
  print(word(string))

main()