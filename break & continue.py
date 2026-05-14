 # Break , continue
 
names = ["Ahmed","Ali","Stop","Omar"]
 
for i in names:
 	if i == "Stop":
 		print ("Break the loop")
 		break
 	print(i)
 	
print ("*"*20)

i = 0
while i< 10:
	i+=1
	if i == 2:
		continue
	if i== 8:
		break
	print ("i = ",i)