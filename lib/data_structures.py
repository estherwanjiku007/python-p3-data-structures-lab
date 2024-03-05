spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
   the_list2=[]   
   for l in range(0,len(spicy_foods)):     
    the_list=spicy_foods[l]["name"]
    the_list2.append(the_list)
   # print(the_list2)    
   return the_list2     
get_names(spicy_foods)

spicy_foods2={}
def get_spiciest_foods(spicy_foods):     
     for a in spicy_foods:
      for t in range(0,len(spicy_foods)):        
        spicy_foods3=spicy_foods[t]["heat_level"]        
        if spicy_foods3>5:      
         return spicy_foods2          
result=get_spiciest_foods(spicy_foods)
def print_spicy_foods(spicy_foods):
    for b in range(0,len(spicy_foods)):
       #print(b)
       my_heat_level=spicy_foods[b]["name"]
       cuisine=spicy_foods[b]["cuisine"]
       heat_level2=spicy_foods[b]["heat_level"]
       emojis="🌶" *heat_level2 
       print(f"{my_heat_level} ({cuisine}) | Heat Level: {emojis}")   
result=print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):  
  for l in range(0,len(spicy_foods)):      
     if spicy_foods[l]["cuisine"]==cuisine:  
        #print(spicy_foods[l])     
        return spicy_foods[l]
my_result=get_spicy_food_by_cuisine(spicy_foods,"Thai")

def print_spiciest_foods(spicy_foods): 
 for x in range(0,len(spicy_foods)):    
   the_name=spicy_foods[x]["name"] 
   the_cuisine=spicy_foods[x]["cuisine"] 
   the_heat_level=spicy_foods[x]["heat_level"]
   the_emojis="🌶"*the_heat_level
   if spicy_foods[x]["heat_level"]>5:
      pass
      print(f"{the_name} ({the_cuisine}) | Heat Level: {the_emojis}")
the_result=print_spiciest_foods(spicy_foods)
new_spices=[]
def get_average_heat_level(spicy_foods):   
   for y in range(0,len(spicy_foods)):            
      new_heat_levels=spicy_foods[y]["heat_level"]
      new_spices.append(new_heat_levels)     
      total1=sum(new_spices)      
      the_avg=total1/len(spicy_foods)
      return the_avg     
all_result=get_average_heat_level(spicy_foods) 

new_spicy_foods=[]
def create_spicy_food(spicy_foods, spicy_food):  
   
    all_new_spicy_foods=spicy_foods.copy()
    all_new_spicy_foods.append(spicy_food)
    #print(new_spicy_foods)    
    return all_new_spicy_foods
my_new_result=create_spicy_food(spicy_foods, 
                                {
                "name": "Griot",
                "cuisine": "Haitian",
                "heat_level": 10,
            }, )
print(my_new_result)        