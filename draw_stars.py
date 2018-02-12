x = [4, 6, 1, 3, 5, 7, 25]
y=[4, "teddy", 1, "kebede", 5, 7, "wiill joe"]

def draw_stars(arr):
    for i in range(len(arr)):
        print '*'*arr[i]
    
    
def draw_starsM(arr):
  for i in arr:
    if isinstance(i, int):
      print "*" * i
    elif isinstance(i, str):
         length = len(i)
         letter = i[0].lower()
         print letter * length

y= [4, "Teddy", 1, "Kebede", 5, 7, "Will Joe"]
draw_starsM(y)