#Author Pacifique Linda IKIREZI
#Question1 Madlib Game

#Holds customization of the inputs
class color:
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
print("Let's play a guessing game!!")
def madlib ():
#Inputs
   A = str(input("Give me a noun: "))
   B = str(input("Give me a word: "))
   C = input("Give me a verb: ")
   D = input("Give me a adjective: ")
   E = input("Give me a body part: ")
   F = input("Give me a word: ")
   G = input("Give me a verb in past tense: ")
   H = input("Give me a verb: ")
   I = input("Give me a verb: ")
   J = input("Give me a verb: ")
#Outputs
   print("\nAny " + color.UNDERLINE  + A + color.END + " Will Do, As long as he can " + color.UNDERLINE  + B + color.END)
   print("Knows how to " + color.UNDERLINE  + C + color.END + " it whole, over coals.")
   print ("Has " + color.UNDERLINE  + D + color.END + " toes, "+ color.UNDERLINE  + E + color.END + " fit in sandals.")
   print (color.UNDERLINE  + F + color.END +" is a must, shoulder length and wild.")
   print ("Does not mind being " + color.UNDERLINE  + G + color.END + " in the rain;")
   print (color.UNDERLINE  + H + color.END + " olives, drinks wine. Can name the clouds.")
   print ("Will " + color.UNDERLINE  + I + color.END + " everything he is been " + color.UNDERLINE  + J + color.END +"\n")

   input("Click enter to see the original text")
#Original Story
   print("Any Apostle Will Do, As long as he can fish.")
   print("Knows how to cook it whole, over coals.")
   print("Has lovely toes,feet fit in sandals.")
   print("Hair is a must, shoulder length and wild.")
   print("Does not mind being caught in the rain; ")
   print("loves olives, drinks wine.Can name the clouds. ")
   print("Will eat everything he’s been given")

madlib()