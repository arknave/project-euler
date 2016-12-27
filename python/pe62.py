from collections import Counter

def get_digits(x):
  digit_count = [0] * 10
  if x == 0:
    digit_count[0] = 1
    return tuple(digit_count)
  else:
    while x > 0:
      digit_count[x % 10] += 1
      x //= 10

  return tuple(digit_count)

def main():
  freq = Counter()
  smallest = {}
  x = 1

  while True:
    cube = x * x * x
    digits = get_digits(cube)
    freq[digits] += 1
    if freq[digits] == 1:
      smallest[digits] = cube

    if freq[digits] >= 5:
      print(smallest[digits])
      break

    x += 1

main()
