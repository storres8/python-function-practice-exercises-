# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald
# Note: 'macdonald'.capitalize() returns 'Macdonald'

def old_macdonald(name):
  a = list(
    enumerate(
      name
    )
  )
  b=[]

  for index, letter in a:
    if index == 0:
      b.append(letter.upper())
    elif index == 3:
      b.append(letter.upper())
    else:
      b.append(letter.lower())

  return(''.join(b))

# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

def master_yoda(string):
  a = string.split()
  a.reverse()
  b = ' '.join(a)

  return b
