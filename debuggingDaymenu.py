day = input("Aaj ka din kya hai? (monday/tuesday) > ")
time = input("Kaunse samay ka khana banana hai? (lunch/dinner) > ")
if day == "monday" or  day == "tuesday":
    print ("Daal-Roti banegi aaj")
elif day == "tuesday" and time == "dinner":
    print ("Pav-Bhaji banegi aaj toh :)")