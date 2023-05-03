#patron2
pattern = "PERSON-1 likes OBJECT and PERSON-2 does not, so _ refused to buy some from the store."

#on fait les différentes listes des variables
nom = ["Joe", "Chandler", "Ross", "Gunther", "Rick", "Morty", "Donald", "Peter", "Barack", "Marshall", "Barney", "Ted", "Monica", "Phoebe", "Rachel", "Karen", "Lily", "Robin", "Lucile", "Rafaëlle", "Suzy", "Gloria", "Janice", "Marie", "Sokka", "Toph", "Katara", "Aang", "Zuko", "David", "Luke", "Leia", "Anakin", "Obi-Wan", "Elijah", "Viggo", "Sean", "Frodon", "Aragorn", "Sam", "Billy", "Orlando", "Ian", "Amir", "Rilès", "Nilah"]

obj = ["roses", "lilies", "tulips", "sunflowers", "daisies", "poppies", "windflowers", "lotus", "dandelions", "iris", "orchids" "vegetables", "carrots", "cucumbers", "coconuts", "pistachios", "eggplants", "cabbages", "broccoli", "cauliflowers", "tomatoes", "zucchinis", "pickles", "mushrooms", "salads", "spinach", "chocolate", "ice cream", "chips", "crips", "turnips"]


#on débute la génération
k = 0

for name in nom : 
  for person in nom : 
    if name != person :
      for objet in obj : 
        print(k, name, objet, person)
        k = k + 1

        sentence = pattern.replace('PERSON-1', name)
        sentence = sentence.replace('OBJECT', objet)
        sentence = sentence.replace('PERSON-2', person)
                
        print(sentence)


#######################################################


#patron84
pattern = "FLOWER-1 did not bloom while FLOWER-2 did so because _ grow in SEASON."

#on fait les différentes listes des variables

fleur = ["roses/lilies/tulips/sunflowers/daisies/poppies/windflowers/lotus/dandelions/iris/orchids"]
fleur = "roses/lilies/tulips/sunflowers/daisies/poppies/windflowers/lotus/dandelions/iris/orchids".split('/')

saison = ["spring", "summer", "autumn", "winter"]

#génération
k = 0

for flowers1 in fleur :
  for flowers2 in fleur :
    if flowers1 != flowers2 :
      for season in saison :
        print(k, flowers1, flowers2, season)
        k = k + 1
        
        sentence = pattern.replace('FLOWER-1', flowers1)
        sentence = sentence.replace('FLOWER-2', flowers2)
        sentence = sentence.replace('SEASON', season)
        
        print(sentence)


######################################################


#patron22
patternM = "PERSON fed his children FOOD-1 instead of FOOD-2 because he thought that the _ was ADJ."

#on fait les différentes listes des variables
nommasc = ["Joe", "Chandler", "Ross", "Gunther", "Rick", "Morty", "Donald", "Peter", "Barack", "Marshall", "Barney", "Ted", "Sokka", "Aang", "Zuko", "David", "Luke", "Anakin", "Obi-Wan", "Elijah", "Viggo", "Sean", "Frodon", "Aragorn", "Sam", "Billy", "Orlando", "Ian", "Amir", "Rilès"]


nomfem = ["Monica", "Phoebe", "Rachel", "Karen", "Lily", "Robin", "Lucile", "Rafaëlle", "Suzy", "Gloria", "Janice", "Marie", "Toph", "Katara", "Leia", "Nilah"]

miam1 = ["vegetables", "carrots", "cucumbers", "coconuts", "pistachios", "eggplants", "cabbages", "broccoli", "cauliflowers", "tomatoes", "zucchinis", "pickles", "mushrooms", "salads", "spinach"]

miam2 = ["chocolate", "ice cream", "chips", "crips", "fast-food", "McDonalds", "KFC", "TacoBell"]

adjectif = ["healthy/better/vigourous/unhealthy/junk food"]
adjectif = "healthy/better/vigourous/unhealthy/junk food".split("/")

#génération
k = 0

for nameM in nommasc : 
  for food1 in miam1 :
    for food2 in miam2 : 
      if food1 != food2 : 
        for adj in adjectif : 
          print(k, nameM, food1, food2, adj)
          k = k + 1

          sentence = patternM.replace('PERSON', nameM)
          sentence = sentence.replace('FOOD-1', food1)
          sentence = sentence.replace('FOOD-2', food2)
          sentence = sentence.replace('ADJ', adj)

          print(sentence)


#je n'ai pas réussi à faire d'une autre manière que celle-ci pour transformer la phrase et accorder les pronoms aux noms féminins


patternF = "PERSON fed her children FOOD-1 instead of FOOD-2 because she thought that the _ was ADJ."


#on fait les différentes listes des variables
nomfem = ["Monica", "Phoebe", "Rachel", "Karen", "Lily", "Robin", "Lucile", "Rafaëlle", "Suzy", "Gloria", "Janice", "Marie", "Toph", "Katara", "Leia", "Nilah"]

miam1 = ["vegetables", "carrots", "cucumbers", "coconuts", "pistachios", "eggplants", "cabbages", "broccoli", "cauliflowers", "tomatoes", "zucchinis", "pickles", "mushrooms", "salads", "spinach"]

miam2 = ["chocolate", "ice cream", "chips", "crips", "fast-food", "McDonalds", "KFC", "TacoBell"]

adjectif = ["healthy/better/vigourous/unhealthy/junk food"]
adjectif = "healthy/better/vigourous/unhealthy/junk food".split("/")

k = 0

for nameF in nomfem : 
  for food1 in miam1 :
    for food2 in miam2 : 
      if food1 != food2 : 
        for adj in adjectif : 
          
          print(k, nameF, food1, food2, adj)
          k = k + 1

          sentence = patternF.replace('PERSON', nameF)
          sentence = sentence.replace('FOOD-1', food1)
          sentence = sentence.replace('FOOD-2', food2)
          sentence = sentence.replace('ADJ', adj)

          print(sentence)


######################################################

#patron78
pattern =  "PERSON-1 had a bigger ANIMAL than PERSON-2 because PERSON-1 fed their ANIMAL much more food."

#on fait les différentes listes des variables
noms = ["Joe", "Chandler", "Ross", "Gunther", "Rick", "Morty", "Donald", "Peter", "Barack", "Marshall", "Barney", "Ted", "Monica", "Phoebe", "Rachel", "Karen", "Lily", "Robin", "Lucile", "Rafaëlle", "Suzy", "Gloria", "Janice", "Marie", "Sokka", "Toph", "Katara", "Aang", "Zuko", "David", "Luke", "Leia", "Anakin", "Obi-Wan", "Elijah", "Viggo", "Sean", "Frodon", "Aragorn", "Sam", "Billy", "Orlando", "Ian", "Amir", "Rilès", "Nilah"]

animal = ["cat", "kitten", "puppy", "dog", "horse", "rabbit", "mouse", "hamster", "guinea pig", "pig", "goldfish", "bunny", "bird", "cow", "duck", "rooster", "chicken", "goat", "sheep", "lion", "tiger", "giraffe", "monkey", "elephant", "crocodile", "zebra", "red panda", "panda", "fish", "turtle", "tortoise"]

k = 0

for name in noms :
  for person in noms :
    if name != person :
      for animals in animal :
        print(k, name, animals, person, animals)
        k = k + 1

        sentence = pattern.replace("PERSON-1", name)
        sentence = sentence.replace("ANIMAL", animals)
        sentence = sentence.replace("PERSON-2", person)

        print(sentence)

######################################################

pattern = "FILM-1 is better than FILM-2, because _ is ADJ."
print (pattern)

films = ["Forest gump", "The Godfather", "Titanic", "Lord of the rings", "Summer Wars", "Kill Bill", "Usual Suspect", "Truman show", "Snowden", "Harry Potter", "Twelve Angry men", "The Dark Knight", "The Good, the Bad and the Ugly", "Pulp Fiction", "Hôtel du Nord", "That Man from Rio", "Vertigo", "Cars", "Interstellar", "Star Wars", "Seven", "Parasite", "Green Book", "Fight Club", "Inception", "Back to the Futur", "The Kid", "Grave of the fireflies", "Princess Mononoke", "Whiplash", "Modern Times", "The Silence of the lambs"]

adj = ["funny", "comic", "pleasant", "sad",]


k = 0

for film1 in films :
    for film2 in films :
            if film1 != film2 :
                for adjectif in adj:
                    print(k, film1, film2, adjectif)
                    k = k + 1
               
                    sentence = pattern.replace('FILM-1', film1)
                    sentence = sentence.replace('FILM-2', film2)
                    sentence = sentence.replace('ADJ', adjectif)
               
                    print(sentence)


######################################################

pattern1 = "The PROFESSION-1 arrived before the PROFESSION-2 because _ are ADJ." 
#print (pattern)

job = ["police", "fireman", "doctors", "emergency", "inspectors"]

adj = ["closer", "faster", "quicker", "nearest", "speedier"]

k = 0
for name in job :
    
    for i in job:
        if name!=i:
            for a in adj :
                    print(k, name, i, a)
                    k = k + 1
                
                    sentence1 = pattern1.replace('PROFESSION-1', name)
                    sentence1 = sentence1.replace('PROFESSION-2', i)
                    sentence1 = sentence1.replace('ADJ', a)
                
                    print(sentence1)

######################################################

pattern = "The COLOR CONTAINER-1 doesn't fit in the COLOR CONTAINER-2 because _ is too ADJ"  
print (pattern)

container = ["suitcase", "bag", "box", "tupperware", "bagpack", "doggybag", "box"]

colors = ["blue", "yellow", "pink", "black", "red", "green", "purple", "magenta", "cyan", "orange"]

adj = ["large", "big", "small", "tight", "short", "massive", "heavy"]


k = 0
for name in container :
    
    for i in container:
        if name!=i:
            for a in adj :
                for color in colors:
                    print(k, color, name, i, a)
                    k = k + 1
                
                    sentence = pattern.replace('COLOR', color)
                    sentence = sentence.replace('CONTAINER-1', name)
                    sentence = sentence.replace('CONTAINER-2', i)
                    sentence = sentence.replace('ADJ', a)
                
                    print(sentence)

######################################################

pattern = "PERSON-1 is better at playing pretend with kids than PERSON-2 because _ is a more ADJ person."


noms = ["Joe", "Chandler", "Ross", "Gunther", "Rick", "Morty", "Donald", "Peter", "Barack", "Marshall", "Barney", "Ted", "Monica", "Phoebe", "Rachel", "Karen", "Lily", "Robin", "Lucile", "Rafaëlle", "Suzy", "Gloria", "Janice", "Marie", "Sokka", "Toph", "Katara", "Aang", "Zuko", "David", "Luke", "Leia", "Anakin", "Obi-Wan", "Elijah", "Viggo", "Sean", "Frodon", "Aragorn", "Sam", "Billy", "Orlando", "Ian", "Amir", "Rilès", "Nilah"]

adj1 = ["funny", "creative", "comic", "pleasant", "sporty"]

adj2 = ["serious", "boring", "shy", "nervous"]

k = 0
for name in noms :
   
    for person in noms :
        if name!=person :
            for adj in adj1 + adj2 :
                print(k, name, person, adj)
                k = k + 1
               
                sentence = pattern.replace('PERSON-1', name)
                sentence = sentence.replace('PERSON-2', person)
                sentence = sentence.replace('ADJ', adj)
               
                print(sentence)










