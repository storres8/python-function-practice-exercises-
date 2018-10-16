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

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True
def almost_there(n):
  if n >= 90 and n <= 110:
    return True
  elif n >= 190 and n <= 210:
    return True
  else:
    return False

# //////////////////////////Level 2 problems////////////////////////////////////////////

# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False
def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i+1] ==3:
            return True
    return False

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiissssssiiippppppiii'
def paper_doll(text):
  # print(list(text))
  b=[]
  for letter in list(text):
    b.append(letter * 3)


  return ''.join(b)
