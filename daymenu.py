day = input("Din enter karo\n")
if day == "monday": # Agar din Monday hai toh
	print("Rajma Chawal")
elif day == "tuesday": # Agar uppar wali conditions galat hai (Yaani day Monday nahi hai) aur day Tuesday hai toh
	print ("Pao Bhaji")
elif day == "wednesday": # Agar uppar wali conditions galat hai (Yaani day Monday aur Tuesday nahi hai) aur day Wednesday hai toh
	print ("Chole Bhature")
elif day == "thursday": # Agar uppar wali conditions galat hai (Yaani day Monday, Tuesday aur Wednesday nahi hai) aur day Thursday hai toh
	print ("Dosa")
elif day == "friday": # Agar uppar wali conditions galat hai (Yaani day Monday, Tuesday, Wednesday aur Thursday nahi hai) aur day Friday hai toh
	print ("Litti Chokha")
elif day == "saturday": # Agar uppar wali conditions galat hai (Yaani day Monday, Tuesday, Wednesday, Thursday aur Friday nahi hai) aur day Saturday hai toh
	print ("Thukpa")
else: # Agar uppar wali conditions galat hai (Yaani day Monday, Tuesday, Wednesday, Thursday, Friday aur Saturday nahi hai)
	print ("Poha")
