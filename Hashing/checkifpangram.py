def checkIfPangram(sentence):
  letters = set(sentence)
  return True if len(letters) == 26 else False
  
sent = "Hello"
temp = set(sent)
print(temp)