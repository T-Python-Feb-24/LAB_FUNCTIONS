def generate_pattern(n:int)->int:
   for i in range(n,0,-1):
      for j in range (i,0,-1):
          print(j,end="")
      print()
print(generate_pattern(5))
