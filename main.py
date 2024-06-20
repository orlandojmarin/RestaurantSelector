# You have a group of friends coming to visit for your high school reunion, and
# you want to take them out to eat at a local restaurant. You aren't sure if
# any of them have dietary restrictions, but yuor restaurant choices are as
# follows:
# Joe's Gourmet Burgers - Vegetarian: No, Vegan: No, Gluten-Free: No
# Main Street Pizza Company - Vegetarian: Yes, Vegan: No, Gluten-Free: Yes
# Corner Cafe - Vegatarian: Yes, Vegan: Yes, Gluten-Free: Yes
# Mama's Fine Italian - Vegetarian: Yes, Vegan: No, Gluten-Free: No
# The Chef's Kitchen - Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
# Write a program that asks whether any members of your party are vegetarian,
# vegan, or gluten-free, and then displays only the restaurants that you may
# take the group to.

# ask if anyone is vegetarian
vegetarian = input("Is anyone in your party a vegetarian (Yes / No)? ").lower()

# verify that the answer is "yes" or "no". If not, ask again.
while (vegetarian != "yes" and vegetarian != "no"):
    print("Please answer 'Yes' or 'No'.")
    vegetarian = input("Is anyone in your party a vegetarian (Yes / No)? ").lower()

# ask if anyone is vegan
vegan = input("Is anyone in your party a vegan (Yes / No)? ").lower()

# verify that the answer is "yes" or "no". If not, ask again.
while (vegan != "yes" and vegan != "no"):
    print("Please answer 'Yes' or 'No'.")
    vegan = input("Is anyone in your party a vegan (Yes / No)? ").lower()

# ask if anyone is gluten free
gluten_free = input("Is anyone in your party gluten-free (Yes / No)? ").lower()

# verify that the answer is "yes" or "no". If not, ask again.
while (gluten_free != "yes" and gluten_free != "no"):
    print("Please answer 'Yes' or 'No'.")
    gluten_free = input("Is anyone in your party gluten-free (Yes / No)? ").lower()

# print restaurant options based on user input
print("Here are your restaurant choices:")

# restaurant options if there are 3 restrictions
if (vegetarian == "yes" and vegan == "yes" and gluten_free == "yes"):
    print("Corner Cafe")
    print("The Chef's Kitchen")

# restaurant options if there are 2 restrictions 
elif (vegetarian == "yes" and vegan == "yes"):
    print("Corner Cafe")
    print("The Chef's Kitchen")

elif (vegan == "yes" and gluten_free == "yes"):
    print("Corner Cafe")
    print("The Chef's Kitchen")

elif (vegetarian == "yes" and gluten_free == "yes"):
    print("Main Street Pizza Company")
    print("Corner Cafe")
    print("The Chef's Kitchen")

# restaurant options if there is only 1 restriction
elif (vegetarian == "yes"):
    print("Main Street Pizza Company")
    print("Corner Cafe")
    print("Mama's Fine Italian")
    print("The Chef's Kitchen")
    
elif (vegan == "yes"):
    print("Corner Cafe")
    print("The Chef's Kitchen")
    
elif (gluten_free == "yes"):
    print("Main Street Pizza Company")
    print("Corner Cafe")
    print("The Chef's Kitchen")

# restaurant options if there are no restrictions   
else:
    print("Joe's Gourmet Burgers")
    print("Main Street Pizza Company")
    print("Corner Cafe")
    print("Mama's Fine Italian")
    print("The Chef's Kitchen")
    
    

    
         
            
        
        
