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
