// # **Ancestral Stories:** In many African cultures, the art of storytelling is passed
// # down from generation to generation. Imagine you're creating an application that
// # records these oral stories and translates them into different languages. The
// # stories vary by length, moral lessons, and the age group they are intended for.
// # Think about how you would model `Story`, `StoryTeller`, and `Translator`
// # objects, and how inheritance might come into play if there are different types of
// # stories or storytellers.

class Ancestral_Stories{
    constructor(length,moral_lesson,the_age_group){
        this.length=length
        this.moral_lesson=moral_lesson
        this.the_age_group=the_age_group
    }

    type_of_story(this){

     if (length==="short" && moral_lesson==="Educative" && the_age_group==="youth"){
        return "story will be intresting "
     }
     else if( length==="long" && moral_lesson==="life" && the_age_group ==="old women"){
        return "the story will be motivating"

     }
    else
        return " no story"


    }

    story(this,story){
        if (story=="About Animals"){
            return  "the story will be boring"

        }
         else if(story=="About culture") {
            return "the story will be instresting"

         }
        else if(story=="Ghost"){
            return "the story will be scary"

        }
      else
        return "no story"
}
   
}

   
       



// # **African Cuisine:** You're creating a recipe app specifically for African cuisine.
// # The app needs to handle recipes from different African countries, each with its
// # unique ingredients, preparation time, cooking method, and nutritional
// # information. Consider creating a `Recipe` class, and think about how you might
// # create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
// # `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
// # methods.

class African_Cuisine{
    cinstructor(ingredient,prepation_time,cooking_method,nutrition){
        this.ingredient=ingredient
        this.prepation_time=prepation_time
        this.cooking_method=cooking_method
       this.nutrition=nutrition
    }

       
}
class MoroccanRecipe extends African_Cuisine{

}


class NigerianRecipe extends African_Cuisine{

}
     
 class EthiopianRecipe extends African_Cuisine{

 }   
        

             
             
             
// # **Wildlife Preservation:** You're a wildlife conservationist working on a
// # program to track different species in a national park. Each species has its own
// # characteristics and behaviors, such as its diet, typical lifespan, migration
// # patterns, etc. Some species might be predators, others prey. You'll need to
// # create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
// # these classes might relate to each other through inheritance.

class Wilidlife{
    constructor(,diet,typical_lifespan,migration,patterns){
        this.diet=diet
        this.typical_lifespan=typical_lifespan
        this.migration=migration
        this.patterns=patterns
    }
}
         
class species extends Wilidlife{

}
    
class Predator extends Wilidlife{

}
    
class prey extends Wilidlife{

}
  

// # **African Music Festival:** You're in charge of organizing a Pan-African music
// # festival. Many artists from different countries, each with their own musical style
// # and instruments, are scheduled to perform. You need to write a program to
// # manage the festival lineup, schedule, and stage arrangements. Think about how
// # you might model the `Artist`, `Performance`, and `Stage` classes, and consider
// # how you might use inheritance if there are different types of performances or
// # stages.
class Music_festival{
    constructor(artist_name,country,music_style,instrument){
        this.artist_name=artist_name
        this.country=country
        this.music_style=music_style
        this.instrument=instrument
    }
}
   
class Artist extends Music_festival{

}
   
class Perfomance extends Music_festival{

}
    
    
class Stage extends Music_festival{

}
   
    
// # Create a class called Product with attributes for name, price, and quantity.
// # Implement a method to calculate the total value of the product (price * quantity).
// # Create multiple objects of the Product class and calculate their total values.
        
class Product{
    constructor(name,price,quantity){
        this.name=name
        this.price=price
        this.quantity=quantity
    }
}
    
        
// # Implement a class called Student with attributes for name, age, and grades (a
// # list of integers). Include methods to calculate the average grade, display the
// # student information, and determine if the student has passed (average grade >=
// # 60). Create objects for the Student class and demonstrate the usage of these
// # methods.
class Student{
    constructor(name,age,grade){
        this.name=name
        this.age=age
        this.grade =grade
    }

   
    calculate_average(this){

    }
        if(grade<60){
            return "below average"
        }
           
        elseif( grade ===60){
            return "average"

        }
        elseif (grade >60) {
            return "above average"
        }
           
    }

// # Create a FlightBooking class that represents a flight booking system. Implement
// # methods to search for available flights based on destination and date, reserve
// # seats for customers, manage passenger information, and generate booking
// # confirmations.

class FlightBooking{
    constructor(name,place,date){
        this.name=name
        this.place=place
        this.date=date
    }
}
     