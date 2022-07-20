

##answer 1
print()
print("############ answer 1 ##############")
print("answer 1")
str="my first python class"
print(len(str))

##answer 2
print()
print("############ answer 2  ##############")
print("answer 2")
str="google"
str_count=str.count('g')
print(str_count)
str_count=str.count('o')
print(str_count)
str_count=str.count('l')
print(str_count)
str_count=str.count('e')
print(str_count)
##answer3
print()
print("############ answer 3 ##############")
print("answer 3")
str="w3resourse"
p=str[:2]
q=str[-2:]
print(p+q)
str="w3"
p=str[:2]
q=str[-2:]
print(p+q)

#answer 4
print()
print("############ answer 4 ##############")
str="restart"
print(str.replace('r','$'))

def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change_char('restart'))

##answer 5
print()
print("############ answer 5 ##############")
def string_mix(a,b):
    new_a=b[:2]+a[2:]
    new_b=a[:2]+b[2:]
    print(new_a +' '+ new_b)
print(string_mix('abc','xyz'))

##answer 6
print()
print("############ answer 6 ##############")
str="string"
if(str[-3:]!='ing'):
    print('expected result:' ,str + 'ing')
else:
    print("expected result:", str[:-3] + 'ly')


##answer 7
    print()
print("############ answer 7 ##############")

def not_poor(str1):
	  snot = str1.find('not')
	  spoor = str1.find('poor')
	  
	
	  if spoor > snot and snot>0 and spoor>0:
	    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
	    return str1
	  else:
	    return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))
print ("answer 5")

#answer 8
print()
print("############ answer 8 ##############")

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["Pooja", "nidhi", "parminder"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])

#answer 9
print()
print("############ answer 9 ##############")
str="online tutorial is best"
n=7
first_part= str[0:n]
second_part= str[n+1:]
print(first_part + " " + second_part)

#answer 10
print()
print("############ answer 10 ##############")
def word(str):
  str=str[-1:] + str[1:-1] + str[:1]
  print(str)
print(word('school'))

##answer 11
print()
print("############ answer 11 ##############")
print()
def odd_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

print(odd_values_string('abcdef'))
print(odd_values_string('school'))

##answer 12  *
print()
print("############ answer 12 ##############")
print()
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the Golden Temple is the holy place for sikh'))

##answer 13
print()
print("############ answer 13 ##############")
print()
#user_input=input("what is ur name?")
#print("what is ur name?",user_input.lower())
#print("what is ur name?",user_input.upper())

##answer 14 *
print()
print("############ answer 14 ##############")
print()
#items = input("Input comma separated sequence of words")
#words = [word for word in items.split(",")]
#print(",".join(sorted(list(set(words)))))

##answer 17
print()
print("############ answer 17 ##############")
print()
str=input("enter the word:")
if(len(str)>2):
   print(str[-2:]+str[-2:]+str[-2:]+str[-2:])
else:
    print("word contains only 2 characters")


##answer 17 (another way
print()
print("############ answer 17 (another way) ##############")