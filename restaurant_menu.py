menu_dic = {}
print "This is your personal Restaurant Menu"

while True:
    dish = raw_input("Please enter a dish: ")

    price = float(raw_input("What is the price of the dish? "))
    menu_dic[dish] = price

    new = raw_input("Would you like to enter new dish? (yes/no) ")

    if new == "no":
        break

print menu_dic

text_file = open("Menu.txt", "w")

text_file.write("MENU OF THE DAY\n" + "\n")

for dish, price in menu_dic.iteritems():
    print dish, price
    text_file.write("%s " % dish.title() + ": %6.2f Euro" % price + "\n")

text_file.close()