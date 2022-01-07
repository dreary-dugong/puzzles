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


#now we reduce things further by comparing allergen lists to each other
#we repeat until no change is made in an iteration
changed = True
while changed:
    
    changed = False
    for allergen in allergens:

        #if we know an ingredient is one allergen, it can't be another
        if len(contains[allergen]) == 1:
            curr_ingredient = contains[allergen][0]
            for other_allergen in allergens:
                if other_allergen != allergen and curr_ingredient in contains[other_allergen]:
                    contains[other_allergen].remove(curr_ingredient)
                    changed = True

#get alphabetical list for output
allergens.sort()
print(allergens)
output = ""
for allergen in allergens:
    output += contains[allergen][0] + ","
output=output[0:-1]
print(output)
    
                
            


    
    
