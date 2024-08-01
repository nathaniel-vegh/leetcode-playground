"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
"""
from collections import defaultdict

text = "lloo"

def maxNumberOfBalloons(text):
  res = []
  counts = defaultdict(int)
  for c in text:
    counts[c] += 1
  for c, count in counts.items():
    if c == 'b':
      res.append(count // 1)
    if c == 'a':
      res.append(count // 1)
    if c == 'l':
      res.append(count // 2)
    if c == 'o':
      res.append(count // 2)
    if c == 'n':
      res.append(count // 1)
  if len(res) != 5:
    return 0
  return min(res)

print(maxNumberOfBalloons(text))