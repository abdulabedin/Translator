#Description: A program that allows a user to translate between English, French and Spanish.
#This program used the skeleton code provided on p. 81 Figure 5.9 "Translating text (badly)" of the Gutag textbook.

EtoF = {'bread': 'pain', 'wine': 'vin', 'with': 'avec', 'I': 'je', 'eat': 'mange', 'drink': 'bois', 'John': 'Jean', 'friends': 'amis', 'and': 'et', 'of': 'du', 'red': 'rouge',  'hello': 'bonjour', 'house': 'maison', 'two': 'deux', 'time': 'temps', 'god': 'dieu', 'yes': 'oui', 'your': 'votre', 'food': 'nourriture', 'love': 'amour', 'my': 'mon', 'name': 'nom', 'family': 'famille', 'is': 'est', 'apples': 'pommes', 'us': 'nous', 'believe': 'croyez', 'in': 'dans', 'bye': 'au revoir', 'week': 'semaine',
        'can': 'pouvez', 'do': 'faire', 'use': 'utiliser', 'good': 'bien', 'beautiful': 'beau', ' beer': 'biere', 'career': 'carrier', 'students': 'eleves', 'school': 'ecole', 'car': 'voiture', 'computer': 'ordinateur', 'night': 'nuit', 'truth': 'verite', 'she': 'elle', 'sleep': 'dormir', 'because': 'car', 'never': 'jamais', 'travel': 'voyage', 'life': 'vie', 'homework': 'devoirs', 'chores': 'corvees', 'brother': 'frere', 'sister': 'soeur', 'money': 'argent', 'hate': 'haine', 'kitchen': 'cuisine', 'clothes': 'vetements'}

EtoS = {'bread': 'pan', 'wine': 'vino', 'with': 'con', 'John': 'Juan', 'friends': 'amigos', 'of': 'de', 'red': 'rojo', 'hello': 'hola', 'house': 'casa', 'two': 'dos', 'time': 'tiempo', 'god': 'dios', 'I': 'yo', 'yes': 'si', 'your': 'tu', 'food': 'comida', 'love': 'amor', 'my': 'mi', 'name': 'nombre', 'family': 'familia', 'is': 'es', 'apples': 'manzanas', 'us': 'nos', 'believe': 'creer', 'in': 'en', 'bye': 'adios', 'week': 'semana', 'can': 'poder', 'do': 'hacer', 'use': 'usar', 'good': 'bueno',
        'beautiful': 'hermoso', ' beer': 'cerveza', 'career': 'carrera', 'students': 'estudiantes', 'school': 'colegio', 'car': 'coche', 'computer': 'computadora', 'night': 'noche', 'truth': 'verdad', 'she': 'ella', 'eat': 'comer', 'drink': 'beber', 'sleep': 'dormir', 'because': 'porque', 'never': 'nunca', 'travel': 'viajar', 'life': 'vida', 'homework': 'deberes', 'chores': 'quehaceres', 'and': 'y', 'brother': 'hermano', 'sister': 'hermana', 'money': 'dinero', 'hate': 'odio', 'kitchen': 'cocina', 'clothes': 'ropa'}

StoF = {'pan': 'pain', 'vino': 'vin', 'con': 'avec', 'yo': 'Je', 'comer': 'mange', 'beber': 'bois', 'Juan': 'Jean', 'amigos': 'amis', 'y': 'et', 'de': 'du', 'rojo': 'rouge',  'hola': 'bonjour', 'house': 'maison', 'casa': 'deux', 'tiempo': 'temps', 'dios': 'dieu', 'si': 'oui', 'tu': 'votre', 'comida': 'nourriture', 'amor': 'amour', 'mi': 'mon', 'nombre': 'nom', 'familia': 'famille', 'es': 'est', 'manzanas': 'pommes', 'nos': 'nous', 'creer': 'croyez', 'en': 'dans', 'adios': 'au revoir',
        'semana': 'semaine', 'poder': 'pouvez', 'hacer': 'faire', 'usar': 'utiliser', 'bueno': 'bien', 'Hermoso': 'beau', 'cerveza': 'biere', 'carrera': 'carrier', 'estudiantes': 'eleves', 'colegio': 'ecole', 'coche': 'voiture', 'computadora': 'ordinateur', 'noche': 'nuit', 'verdad': 'verite', 'ella': 'elle', 'dormir': 'dormir', 'porque': 'car', 'nunca': 'jamais', 'viajar': 'voyage', 'vida': 'vie', 'deberes': 'devoirs', 'quehaceres': 'corvees', 'hermano': 'frere', 'hermana': 'soeur', 'dinero': 'argent', 'odio': 'haine', 'cocina': 'cuisine', 'ropa': 'vetements'}

f = open('output.txt', 'w')


def reverseDictionary(dictionary):
 new = {}
 for i in dictionary:
   new[dictionary[i]] = i
 return new


dicts = {'English to French': EtoF, 'French to English': reverseDictionary(EtoF), 'English to Spanish': EtoS, 'Spanish to English': reverseDictionary(
    EtoS), 'Spanish to French': StoF, 'French to Spanish': reverseDictionary(StoF)}


def translateWord(word, dictionary):
   if word in dictionary.keys():
       return dictionary[word]
   elif word != '':
       return '"' + word + '"'
   return word


def translate(phrase, dicts, direction):
   dictionary = dicts[direction]
   translation = ''
   word = ''

   for character in phrase:
       if character.isalpha():
           word = word + character
       else:
           translation = translation + \
               translateWord(word, dictionary) + character
           word = ''
   translation = translation + translateWord(word, dictionary)
   return translation


sentence = 'I drink good red wine, and eat bread.'
translated = translate(sentence, dicts, 'English to French')

print('--------------------------------------')
print('Input:', sentence)
print('Output:', translated)
print('--------------------------------------')

sentence = 'Je bois du vin rouge.'
translated = translate(sentence, dicts, 'French to English')

print('Input:', sentence)
print('Output:', translated)
print('--------------------------------------')

inputlanguage =int(input("Enter 1 to translate from English to French\nEnter 2 to translate from French to English\nEnter 3 to translate from English to Spanish\nEnter 4 to translate from Spanish to English\nEnter 5 to translate from French to Spanish\nEnter 6 to translate from Spanish to French\nEnter 7 to translate from French to Spanish and English\nEnter 8 to translate from Spanish to French and English\nEnter 9 to translate from English to French and Spanish\nEnter your choice: "))
if inputlanguage == 1:
 print('\n', dicts['English to French'].keys())
 lang = 'English to French'
elif inputlanguage == 2:
 print('\n', dicts['French to English'].keys())
 lang = 'French to English'
elif inputlanguage == 3:
 print('\n', dicts['English to Spanish'].keys())
 lang = 'English to Spanish'
elif inputlanguage == 4:
 print('\n', dicts['Spanish to English'].keys())
 lang = 'Spanish to English'
elif inputlanguage == 5:
 print('\n', dicts['French to Spanish'].keys())
 lang = 'French to Spanish'
elif inputlanguage == 6:
 print('\n', dicts['Spanish to French'].keys())
 lang = 'Spanish to French'
elif inputlanguage == 7:
 print('\n', dicts['French to English'].keys())
 lang = 'French to Spanish'
 lang2 = 'French to English'
elif inputlanguage == 8:
 print('\n', dicts['Spanish to English'].keys())
 lang = 'Spanish to English'
 lang2 = 'Spanish to French'
elif inputlanguage == 9:
 print('\n', dicts['English to Spanish'].keys())
 lang = 'English to Spanish'
 lang2 = 'English to French'
print("")

user = input(
    "Enter the sentence you want to translate (only translates words listed above): ")
f.write("\n")
f.write("Translation from English to Spanish and French")
f.write("\n")
f.write("Input sentence: ")

f.write(user)
print("")

if inputlanguage == 7 or inputlanguage == 8 or inputlanguage == 9:
  translated = translate(user, dicts, lang)
  print("Translation from", lang, ":", translated)
  f.write("\n")
  f.write("Translation from ")
  f.write(lang)
  f.write(": ")
  f.write(translated)
  translated = translate(user, dicts, lang2)
  f.write("\n")
  f.write("Translation from ")
  f.write(lang2)
  f.write(": ")
  f.write(translated)
  print("Translation from", lang2, ":", translated)

else:
  translated = translate(user, dicts, lang)
  print("Translation from", lang, ":", translated)
  f.write("\n")
  f.write("Translation from ")
  f.write(lang)
  f.write(": ")
  f.write(translated)

f.close()
