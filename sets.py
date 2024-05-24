from sets_categories_data import (ALCOHOLS)


def clean_ingredients(dish_name, dish_ingredients):
    celanisimos=set()
    comidita=[]
    for e in (dish_name):
        if e not in comidita:
            comidita.append(e)
    for e in (dish_ingredients):
        celanisimos.add(e)
    finishdish=(dish_name),celanisimos        
    return finishdish



def check_drinks(drink_name, drink_ingredients):
  
    for e in drink_ingredients:
        if e in ALCOHOLS:
            return drink_name+" Cocktail" 
    return drink_name+" Mocktail"

