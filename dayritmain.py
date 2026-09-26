pet_list = ["Whitey - Dog - Adopted",
          "Tophey - Cat - Available",
          "Browney - Dog - Available",
          "Balcky - Dog - Available"]

print("1. Add a pet", "2. View all pets", "3. Count available vs adopted", "4. Find a pet by name", "5. Exit")
choice = input("Choose an option : ")

if choice == "1":
    add_pet = input("Pet name - Animal type - Adoption status (Available/Adopted): ")
    pet_list.append(add_pet)
    print(pet_list)

elif choice == "2":
    print(pet_list)

elif choice == "3":
    available_count1 = sum(1 for pet in pet_list if "Available" in pet)
    available_count2 = sum(1 for pet in pet_list if "Adopted" in pet)
    print(available_count1, "Available")
    print(available_count2, "Adopted")

elif choice == "4":
    find_pet = input("Pet name: ")
    pet_list.copy(find_pet)
    print (pet_list.copy)

else:
    print("Thankyou!!!")

    #push