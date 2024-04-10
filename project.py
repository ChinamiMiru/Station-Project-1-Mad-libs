print("It was about (Number) (Measure of time) ago when I arrived at the hospital in a (Mode of Transportation). The hospital is a/an (Adjective) place, there are a lot of (Adjective2) (Noun) here. There are nurses here who have (Color) (Part of the Body ). If someone wants to come into my room I told them that they have to (Verb) first. I’ve decorated my room with (Number2) (Noun2). Today I talked to a doctor and they were wearing a (Noun3) on their ( Part of the Body 2). I heard that all doctors (Verb) (Noun4) every day for breakfast. The most ( Adjective3) thing about being in the hospital is the (Silly Word ) (Noun) !")
print("This weekend I am going camping with ( Proper Noun (Person’s Name)). I packed my lantern, sleeping bag, and (Noun). I am so (Adjective (Feeling)) to (Verb) in a tent. I am (Adjective (Feeling) 2) we might see a(n) (Animal), I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and (Verb2). I have heard that the (Color) lake is great for ( Verb (ending in ing) ). Then we will (Adverb (ending in ly)) hike through the forest for (Number) (Measure of Time). If I see a (Color) (Animal) while hiking, I am going to bring it home as a pet! At night we will tell (Number) (Silly Word) stories and roast (Noun2) around the campfire!!")  
print("Dear (Proper Noun (Person’s Name) ), I am writing to you from a (Adjective) castle in an enchanted forest. I found myself here one day after going for a ride on a (Color) (Animal) in (Place). There are (Adjective2) (Magical Creature (Plural)) and (Adjective3) (Magical Creature (Plural)2) here! In the ( Room in a House) there is a pool full of (Noun). I fall asleep each night on a (Noun2) of (Noun(Plural)3) and dream of (Adjective4) ( Noun (Plural)4). It feels as though I have lived here for (Number) ( Measure of time). I hope one day you can visit, although the only way to get here now is (Verb (ending in ing)) on a (Adjective5) (Noun5)!!")

task1 = ["It was about {} {} ago when I arrived at the hospital in a {}. The hospital is a/an {} place, there are a lot of {} {} here. There are nurses here who have {} {}. If someone wants to come into my room I told them that they have to {} first. I’ve decorated my room with {} {}. Today I talked to a doctor and they were wearing a {} on their {}. I heard that all doctors {} {} every day for breakfast. The most {} thing about being in the hospital is the {} {} !"]
task2 = ["This weekend I am going camping with {}. I packed my lantern, sleeping bag, and {}. I am so {} to {} in a tent. I am {} we might see a(n) {}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {}. I have heard that the {} lake is great for {}. Then we will {} hike through the forest for {} {}. If I see a {} {} while hiking, I am going to bring it home as a pet! At night we will tell {} {} stories and roast {} around the campfire!!"]
task3 = ["Dear {}, I am writing to you from a {} castle in an enchanted forest. I found myself here one day after going for a ride on a {} {} in {}. There are {} {} and {} {} here! In the {} there is a pool full of {}. I fall asleep each night on a {} of {} and dream of {} {}. It feels as though I have lived here for {} {}. I hope one day you can visit, although the only way to get here now is {} on a {} {}!!"]

user_choice = input("Choose a task(1, 2, or 3): ")

if user_choice == '1':
 task = task1
 placeholders = ['number','measure of time', 'mode of transportation', 'adjective', 'adjective2', 'noun']
elif user_choice == '2':
 task = task2
 placeholders = ['{}']
elif user_choice == '3':
 task = task3
 placeholders = ['{}']
else:
 print("invalid choice, please eneter 1, 2, or 3")
 exit()

for i in range(len(task)):
 placeholders =task[i].count("{}")
 user_inputs = [input("enter value: ") for _ in range(placeholders)]  
 task[i] = task[i].format(*user_inputs)
 print(task)






