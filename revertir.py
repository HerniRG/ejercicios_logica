def rev(secuence):
  reverseList = []
  for i in range(len(secuence)-1, -1, -1):
    reverseList.append(secuence[i])
  return reverseList

def main():
  print(rev([1,2,3,4,5]))
  print(rev([9,8,7,6,5,4,3,2,1,0]))

main()