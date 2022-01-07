import regex #we use the captures function for repeated input

class recipe():
    def __init__(self, ingredients, allergens):
        self.ingredients = ingredients
        self.allergens = allergens

recipes = [] #list of all recipes
ingredients = [] #set of all ingredients
allergens = [] #set of all allergens





#read input
inputFile = "input1.txt"
pattern = regex.compile(r"((\w+) )+\(contains ((\w+)(, )?)+\)")

with open(inputFile) as f:
    fulltext = f.read();

collection = pattern.finditer(fulltext) #match pattern to input

for match in collection: #aka for recipe in input

    #unpack caputring groups
    curr_ingredients = match.captures(2)
    curr_allergens = match.captures(4)

    #add data to our lists
    recipes.append(recipe(curr_ingredients, curr_allergens))
    
    for ingredient in curr_ingredients:
        if ingredient not in ingredients:
            ingredients.append(ingredient)

    for allergen in curr_allergens:
        if allergen not in allergens:
            allergens.append(allergen)


#process data
contains = {} #dictionary to link ingredients to allergens

for allergen in allergens:
    
    possible_ingredients = [] #list of which ingredients may contain our current allergen
    
    for recipe in recipes:
        if allergen in recipe.allergens:

            #if this is the first recipe, anything is possible
            if len(possible_ingredients) == 0:
                possible_ingredients.extend(recipe.ingredients)

            #otherwise, we take the intersection with what's already possible
            else:
                possible_ingredients = [ingredient for ingredient in
                                        possible_ingredients if ingredient
                                        in recipe.ingredients]

    contains[allergen] = possible_ingredients

#at this point, we have not totally deduced to the maximum extent which
#allergen is which ingredient, but we don't need to do any more here.
#the only way to reduce it further is to take an ingredient that is definitely
#a single allergen and remove it from the other allergens, but this doesn't
#yield any more ingredients that cannot possibly be allergens

#take all ingredients that can't be an allergen
non_allergens = []
for ingredient in ingredients:
    found = False
    for allergen in allergens:
        if ingredient in contains[allergen]:
            found = True

    if not found:
        non_allergens.append(ingredient)

#now we count the final output
count = 0
for recipe in recipes:
    for ingredient in non_allergens:
        if ingredient in recipe.ingredients:
            count+= 1

print(count)
            

                
            


    
    
