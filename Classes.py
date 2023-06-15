

# **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.

class Ancestral_Stories:
    def __init__(self,length,moral_lesson,the_age_group):
         self.length=length
         self.moral_lesson=moral_lesson
         self.the_age_group=the_age_group
    def type_of_story(self,length,moral_lesson,the_age_group):
        if length=="short" and moral_lesson=="Educative"and the_age_group=="youth":
           return "story will be intresting "
        elif length=="long" and moral_lesson== "life" and the_age_group =="old women":
            return "the story will be motivating"
        else:
            return " no story"
    def story(self,story):
        if story=="About Animals":
            return  "the story will be boring"
        elif story=="About culture":
            return "the story will be instresting"
        elif story=="Ghost":
            return "the story will be scary"
        else:
            return "no story"
    
       
        
Ancestral=Ancestral_Stories("short","Educative","youths")
print(Ancestral.type_of_story())





# **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.

class African_Cuisine:
    def __init__(self,ingredient,prepation_time,cooking_method,nutrition):
        self.ingredient=ingredient
        self.prepation_time=prepation_time
        self.cooking_method=cooking_method
        self.nutrition=nutrition
class MoroccanRecipe(African_Cuisine):
     def __init__(self, ingredient, prepation_time, cooking_method, nutrition):
         super().__init__(ingredient, prepation_time, cooking_method, nutrition)
         ingredients=["flour","onions","baking powder"]
         if ingredient in ingredients and prepation_time >15 and cooking_method=="fry":
             return "sweet moroccan food"
         elif ingredient in ingredients and prepation_time==15 and cooking_method=="boil":
             return "has no good taste"
         elif ingredient in ingredients and prepation_time <15 and  cooking_method=="less fried":
             return " not cooked well"
        
   
class NigerianRecipe(African_Cuisine):
     def __init__(self, ingredient, prepation_time, cooking_method, nutrition):
         super().__init__(ingredient, prepation_time, cooking_method, nutrition)
         ingredients=["flour","onions","baking powder"]
         if ingredient in ingredients and prepation_time >15 and cooking_method=="fry":
             return "sweet moroccan food"
         elif ingredient in ingredients and prepation_time==15 and cooking_method=="boil":
             return "has no good taste"
         elif ingredient in ingredients and prepation_time <15 and  cooking_method=="less fried":
             return " not cooked well"
       
class EthiopianRecipe(African_Cuisine):
     def __init__(self, ingredient, prepation_time, cooking_method, nutrition):
         super().__init__(ingredient, prepation_time, cooking_method, nutrition)
         ingredients=["flour","onions","baking powder"]
         if ingredient in ingredients and prepation_time >15 and cooking_method=="fry":
             return "sweet Ethiopian  food"
         elif ingredient in ingredients and prepation_time==15 and cooking_method=="boil":
             return "has no good taste"
         elif ingredient in ingredients and prepation_time <15 and  cooking_method=="less fried":
             return " not cooked well"
             
             
             
# **Wildlife Preservation:** You're a wildlife conservationist working on a
# program to track different species in a national park. Each species has its own
# characteristics and behaviors, such as its diet, typical lifespan, migration
# patterns, etc. Some species might be predators, others prey. You'll need to
# create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# these classes might relate to each other through inheritance.

class Wilidlife:
     def __init__(self,diet,typical_lifespan,migration,patterns):
         self.diet=diet
         self.typical_lifespan=typical_lifespan
         self.migration=migration
         self.patterns=patterns
         
         
class species(Wilidlife):
    def __init__(self, diet, typical_lifespan, migration, patterns):
        super().__init__(diet, typical_lifespan, migration, patterns)
        return f"species will live for {typical_lifespan} and will {migration} every {patterns}"


class Predator(Wilidlife):
    def __init__(self, diet, typical_lifespan, migration, patterns):
        super().__init__(diet, typical_lifespan, migration, patterns)
        return f"predator will live for {typical_lifespan} and will {migration} every {patterns}"
        

class prey(Wilidlife):
    def __init__(self, diet, typical_lifespan, migration, patterns):
        super().__init__(diet, typical_lifespan, migration, patterns)
        return f"prey will live for {typical_lifespan} and will {migration} every {patterns}"


# **African Music Festival:** You're in charge of organizing a Pan-African music
# festival. Many artists from different countries, each with their own musical style
# and instruments, are scheduled to perform. You need to write a program to
# manage the festival lineup, schedule, and stage arrangements. Think about how
# you might model the `Artist`, `Performance`, and `Stage` classes, and consider
# how you might use inheritance if there are different types of performances or
# stages.
class Music_festival:
    def __init__(self,artist_name,country,music_style,instrument):
        self.artist_name=artist_name
        self.country=country
        self.music_style=music_style
        self.instrument=instrument
class Artist(Music_festival):
    def __init_subclass__():
        return super().__init_subclass__()

class Perfomance(Music_festival):
    def __init_subclass__():
        return super().__init_subclass__()
    
class Stage(Music_festival):
    def __init_subclass__():
        return super().__init_subclass__()
    
    
# Create a class called Product with attributes for name, price, and quantity.
# Implement a method to calculate the total value of the product (price * quantity).
# Create multiple objects of the Product class and calculate their total values.
        
class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
        
    def calculate_tatal_value(self):
        value= price*quantity
        
        
# Implement a class called Student with attributes for name, age, and grades (a
# list of integers). Include methods to calculate the average grade, display the
# student information, and determine if the student has passed (average grade >=
# 60). Create objects for the Student class and demonstrate the usage of these
# methods.
class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade =grade
    def calculate_average(self):
        if grade<60:
            return "below average"
        elif grade == 60:
            return "average"
        elif grade >60:
            return "above average"


# Create a FlightBooking class that represents a flight booking system. Implement
# methods to search for available flights based on destination and date, reserve
# seats for customers, manage passenger information, and generate booking
# confirmations.

class FlightBooking:
    def __init__(self,name,place,date):
        self.name=name
        self.place=place
        self.date=date
    def available_flight(self):
           