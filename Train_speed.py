def time(dist,speed):
 
 speed=int(input("Enter the speed of the train: "))
 if(speed<1 or speed>200):
  print("Error");
  return None
   
 else:
  time_taken=(dist/speed)*(18/5)
  return time_taken

result=time(400,0)
if result is not None:
  print(result)