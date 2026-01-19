a=200
b=33
if b>a:
    print("b est plus grand que a")
else:
    print("b n'est pas grand que a")

x="HELLO"
y=15
print(bool(x))
print(bool(y))

bool("abc")
bool(123)
bool(["apple","cherry","banana"])

class myclass():
    def __len__(self):
        return 0
    
myobj = myclass()
print(bool(myobj))

def myFunction() :
    return True

if myFunction():
    print("Yes")
else:
    print("NO")

x= 200
print(isinstance(x,int))

numbers = [1, 2, 3, 4, 5]
count = len (numbers)
if count > 3 :
    print(f"La liste comporte {count} elements")
if (count:= len(numbers))>3:
    print((f"La liste comporte {count}  elements"))

# création des listes

thislist =["apple","cherry","banana"]
print(thislist)

#REMARQUE
#Autorisation des doublons : à ce niveau on peut écriere un éléments de la liste plusieurs fois

thislist =["apple","cherry","banana","apple", "banana"]
print(thislist)

#Pour déterminer la longueur d'une liste on utilise la fonction len()

thislist =["apple","cherry","banana"]
print(len(thislist))

#Il est noté que les éléments d'une liste peuvent être de types int , booléen ou string

list1 = ["abc", 34, True, 40, "male"]

#Pour accéder à un élément de la liste on peut écrire:

thislist =["apple","cherry","banana"]
print( thislist[1])

#Pour vérifier si un élément existe dans une liste on utilise in 

thislist =["apple","cherry","banana"]
if "apple" in thislist:
    print("oui, 'apple' est dans la liste des fruits")

#Modification d'un élément de la liste
#  
thislist =["apple","cherry","banana"]
thislist[1] = "Blackcurrant"
print( thislist)

#Pour insérer de nouvelles éléments dans une liste on utilise insert()

thislist =["apple","cherry","banana"]
thislist.insert(2, "watermelon")
print( thislist)

#Pour ajouter un élément à la fin de la liste on utilise append()

thislist =["apple","cherry","banana"]
thislist.append("watermelon")
print( thislist)

#Pour ajouter des éléments d'une autre liste à la liste actuelle on utilise extend()
# les éléments de l'autre liste seront ajouter à la fin de la nouvelle liste

thislist =["apple","cherry","banana"]
tropical = ["mango", "pineaapple", "papaya"]
thislist.extend(tropical)
print( thislist)

#Pour supprimmer un ou des éléments dans une liste on utilise remove()

thislist =["apple","cherry","banana"]
thislist.remove("cherry")
print( thislist)

#S'il existe le même élément dans une liste le programme supprime unique le premier

thislist =["apple","cherry","banana","apple","banana"]
thislist.remove("banana")
print(thislist)

#Suppression d'un index spécifié dans une liste on utilise pop()
#REMARQUE: si on ne spécifie pas l'index(1 ou 2 choses à supprimer); pop() 
# supprime le dernier élément de la liste

thislist =["apple","banana","cherry"]
thislist.pop(1)
print(thislist)

# del permet  également de supprimer un ou plusiers  élément de la liste avec l'index spécifié 

thislist =["apple","banana","cherry"]
del thislist[0]
print(thislist)

# Pour effacer la liste on utilise clear() qui permet de vider touts les éléments d'une liste 
# mais cette liste existera toujours mais ne comportera plus aucun éléments

thislist =["apple","banana","cherry"]
thislist.clear()
print(thislist)

#On peut parcourir les éléments d'une liste en utilisant for
# exemple: imprimez tous les éléments d'une liste un par un 

thislist =["apple","banana","cherry"]
for x in thislist:
    print(x)

# Parcourir les numéros d'index. On utilise les foctions range() et len()

thislist =["apple", "banana", "cherry"]
for y in range(len(thislist)):
    print(thislist[y])

# Utilisation de la boucle while
#il faut incrémenter l'index de 1 après chaque itération

thislist =["apple","banana","cherry"]
k = 0
while k < len(thislist):
    print(thislist[k])
    k = k + 1

#Obtention d'une nouvelle liste  de fruits ne contenant 
# ques les fruits dont le nom contient la lettre a

fruits = ["apple", "banana", "cherry", "Kiwi" ," mango"]
newlist = []

for x in fruits:
    if "a" in x :
        newlist.append(x)

print(thislist)

#On peut écrire le code précédent avec une seule ligne de code plus simple :

fruits = ["apple", "banana", "cherry", "Kiwi" ," mango"]
newlist = [x for x in fruits if "a" in x ]
print(thislist)

# Pour mettre  en majuscule les valeurs de la nouvelle liste 

newlist = [x.upper() for x in fruits]

#NOTION DE TRI 

#Pour trier par ordre alphabétique ou numérique on utilise la fonction sort()

thislist = ["orange", "mango" , "kiwi" , "pineapple" , "banana"]
thislist.sort()
print(thislist)

#Pour trier par ordre décroissant on utilise l'argument mot-clé reverse= true
#La même méthode est utilisée dans le cas numérique

thislist = ["orange", "mango" , "kiwi" , "pineapple" , "banana"]
thislist.sort(reverse=True)
print(thislist)

#Personnalisation  de la fonction tri
# Dans ce cas le programmation renvoie les éléments du plus petit au plus grand














