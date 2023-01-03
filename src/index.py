import re

# 1
def firstLeft(arr,target):
  for el in arr:
    if el == target:
      return arr.index(el)
  return -1
print(firstLeft([1,2,3,1,2,3],3))

# 2
def firstRight(arr,target):
  result = -1
  for i, el in enumerate(arr):
    if el == target:
      result = i
  return result
print(firstRight([1,2,3,1,2,3],3))

# 3
def isPalindrome(s):
  return s.lower() == s.lower()[::-1]
print(isPalindrome('Anna'))

# 4
def findTargetListEl(arr, lenNum):
  result = []
  for el in arr:
    if len(el) == lenNum:
      result.append(el)
  return result
print(findTargetListEl(['Mark', 'John', 'Ann'],4))  # ['Mark', 'John']

# 5
def countVowels(s):
  counter = 0
  vowels = ['a','e','i','o','u']
  for ch in s:
    if ch in vowels:
      counter += 1
  return counter
print(countVowels('wolf'))

# 6
def iterateFromNumToNum(a,b):
  counter = 0
  for x in range(a,b+1):
    counter += x
  return counter
print(iterateFromNumToNum(1,5))
print(iterateFromNumToNum(3,6))

# 7
def findMidChar(s):
  isEven = len(s) % 2 == 0
  isOdd = len(s) % 2 == 0
  if isEven:
    return s[int(len(s) / 2)]
  if isOdd:
    return s[int((len(s) - 1) / 2)]
print(findMidChar('test'))
print(findMidChar('testing'))

# 8
def squareNum(n):
  result = ''
  slist = list(format(n))
  for s in  slist:
    squareNum = int(s)*int(s)
    result += format(squareNum)
  return result
print(squareNum(25))  # 425

# 9
# import re
def replaceAll(s, ch):
  result = re.sub(ch, '', s)
  return result
print(replaceAll('te###st', '#'))  # 'test'

# 10
def findRepeat(a):
  result = []
  obj = {}
  for i, n in enumerate(a):
    obj[n] = i
  for n in a:
    if a.index(n) != obj[n]:
      result.append(n)
  return result
print(findRepeat([1,2,3,4,5,6,7,3,8,9]))

# 11
def findRepeats(a):
  result = []
  cache = {}
  for n in a:
    if n in cache:
      cache[n] += 1
    else:
      cache[n] = 1
  for n in cache:
    if cache[n] > 1:
      a = [n for x in range(cache[n])]
      result.append(a)
  return result
print(findRepeats([1,2,3,4,5,3,6,7,5,8,9,5]))  # [[3,3],[5,5,5]]

# 12
def countRepeatsInRange(a,l,r,target):
  counter = 0
  for x in a[l:r]:
    if x == target:
      counter += 1
  return counter
print(countRepeatsInRange[1,2,3,4,5,3,6,7,5,8,9,5], 2, 7, 3) #  2

# 13
def isTargetSum(arr, targetSum):
  for a in arr:
    for b in arr:
      if a + b == targetSum:
        return True
  return False
print(isTargetSum([1,2,3,4,5,6,7], 5)) #  True

# 14
def argsToStr(*args):
  result = ""
  for x in args[1:]:
    result += "" + args[0] + format(x)
  return result
print(argsToStr('!',4,-10,34,0))

# 15
def isObjEmpty(obj):
  if len(obj) > 0:
    return False
  return True
print(isObjEmpty({})) # True

# 16
def findMax(arr):
  return max(arr)
print(findMax([3,5,2,1,3,7,66,8,9,4,100,45]))

def findMax(arr):
  maxVal = arr[0]
  for val in arr:
    if val > maxVal:
      maxVal = val
  return maxVal
print(findMax([3,5,2,1,3,7,66,8,9,4,100,45]))

# 17
def findAllUniqueSums(arr, target):
  result = []
  cache = {}
  for x in arr:
    cache[x] = 1
  for n in cache:
    secondNum = target - n
    if n + secondNum == target:
      if secondNum > n:
        result.append([n, secondNum])
  return result  
print(findAllUniqueSums([1,2,3,4,5,6], 6))

# 18
def findShortestStr(arr):
  minWord = arr[0]
  for word in arr:
    if len(word) < len(minWord):
      minWord = word
  return minWord
print(findShortestStr(['ab', 'a', 'abc']))  # 'a'

# 19
def groupAnagrams(arr):
  cache = {}
  for word in arr:
    sortedWord = ''.join(sorted(word))
    if sortedWord in cache:
      cache[sortedWord].append(word)
    else:
      cache[sortedWord] = [word]
  return list(cache.values())
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  # [["bat"],["nat","tan"],["ate","eat","tea"]]

# 20
def findPopularChar(str):
  result = ''
  cache = {}
  counter = 0

  for char in str:
    if char in cache:
      cache[char] += 1
    else:
      cache[char] = 1
  for char in cache:
    if cache[char] > counter:
      counter = cache[char]
      result = char
  return result
print(findPopularChar('ababa'))  # 'a'