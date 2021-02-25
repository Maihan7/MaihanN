text = input("plz insert ")
top = ""
bot =""
for i in range(len(text)):
  if i%2==0:
    top = top+text[i]
  else:
    bot = bot +text[i]
cipher = top +bot
print(cipher)