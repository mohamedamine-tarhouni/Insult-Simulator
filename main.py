from Player import PLAYER
from insults import INSULT
from random import randint
characters = ["Dame", "gentleman", "poor", "gangster", "king", "master ocean"]

# cette fonction affiche les insultes disponibles


def Display_insult_list(list):
    for index in range(0, len(list), 1):
        print("                ", index+1, "-->", list[index])
    print("\n")

# cette fonction affiche les caractères disponibles


def character_select(arr):
    for i in range(0, len(arr), 1):
        print(i+1, "-->", arr[i])


# cette fonction prend une valeur et verifie si le caractère saisie est numerique ou pas
# après elle la compare avec cette valeur maximale (cette fonction est utilisée dans les choix avec les nums)
def saisie_char_num(length, msg):
    verif = False
    while verif == False:
        c = input(msg)
        while c.isnumeric() == False:
            c = input(msg)
        character = int(c)
        if character >= 1 and character <= length:
            verif = True
    return character


# cette fonction permet de gérer les informations de chaque joueur(pseudo et caractère préféré)
def Player_input():
    # le 1er joueur(ca ne marchera pas si sa valeur est vide)
    player1 = input("Pseudo de joueur 1 :")
    while player1 == "":
        player1 = input("Pseudo de joueur 1 :")
    # après avoir saisi le pseudo le joueur peut choisir son caractère
    # par saisir le nombre correspondant avec ce caractère
    character_select(characters)
    character1 = saisie_char_num(len(characters), "choisir un caractère : ")
    # character1_selected c'est la valeur final qui sera retournée par la fonction
    character1_selected = characters[character1-1]
    # on enlève le caractère selectionné de la liste(les deux joueurs ne peuvent pas avoir le meme caractère)
    characters.remove(characters[character1-1])
    # le pseudo du 2éme joueur(ca ne marchera pas si vide ou egal au celui du 1er joueur)
    player2 = input("Pseudo de joueur 2 :")
    while player2.upper() == player1.upper() or player2 == "":
        if player2 != "":
            print("les pseudos doivent être differents")
        player2 = input("Pseudo de joueur 2 :")
    character_select(characters)
    character2 = saisie_char_num(len(characters), "choisir un caractère : ")
    character2_selected = characters[character2-1]
    return player1, player2, character1_selected, character2_selected


name_player1, name_player2, character1, character2 = Player_input()
# on affiche le caractère de chaque joueur
print(name_player1, "-->", character1)
print(name_player2, "-->", character2)
PLAYER1 = PLAYER(name_player1, character1)
PLAYER2 = PLAYER(name_player2, character2)
insult = INSULT("")
insult1 = INSULT(character2)
insult2 = INSULT(character1)


def display_array_in_string(arr):
    str = ""
    for i in range(0, len(arr), 1):
        str = str+arr[i]+" "
    return str


def display_messages(player1name, player1msg, player2name, player2msg):
    print("message de ", player1name, " = ", player1msg)
    print("message de ", player2name, " = ", player2msg)

# cette fonction permet de calculer le totalle des points depend des insultes


def sum_insults(arr, insult):
    sum = 0
    for i in range(0, len(arr), 1):
        for insult_index in insult.Sujet:
            if insult_index.name == arr[i]:
                sum += insult_index.damage
        for insult_index in insult.Verbe:
            if insult_index.name == arr[i]:
                sum += insult_index.damage
        for insult_index in insult.Verbe_adj:
            if insult_index.name == arr[i]:
                sum += insult_index.damage
        for insult_index in insult.Adj:
            if insult_index.name == arr[i]:
                sum += insult_index.damage
        for insult_index in insult.COD:
            if insult_index.name == arr[i]:
                sum += insult_index.damage
    return sum


# cette fonction verifie sile mot ajoutée est une faiblesse du caractère adversaire
def verif_weakness(str, ins):
    for weak in ins.faiblesse:
        if weak == str:
            return True
    return False


# cette fonction forme un tableau avec que les insultes sans les points des degats
def form_array_insults(key):
    list = []
    for subkey in key:
        list.append(subkey.name)
    return list

# cette fonction fait la verification du toute la phrase formée par les joueurs


def verif_longue_phrases(arr, ins):

    # une liste auxiliaire pour ne pas changer les tableaux des joueurs
    aux_list = arr

    # la valeur de v sera faut s'il ya une faute dans la phrase du joueur
    v = True

    #s'il ya des "et" alors la phrase doit etre verifié plusieurs fois alors on appelle une boucle
    if "et" in aux_list and aux_list.index("et") % 3 == 0 and aux_list.index("et") != 0:
        while "et" in aux_list and aux_list.index("et") < len(aux_list)-1 and v == True:

            # on verifie la phrase partie par partie
            v = verif_forme(aux_list[slice(0, aux_list.index("et"))], ins)
            if v == True:
                aux_list = aux_list[slice(
                    aux_list.index("et")+1, len(aux_list))]
                v = verif_forme(aux_list, ins)
    else:

        #si c'est une phrase simple on fait qu'une seule verification
        v = verif_forme(aux_list, ins)
    return v


# cette fonction verifie la forme d'une partie de la phrase (les phrases doivent etre sous forme de sujet+verbe+adj+cod ou sujet+verbe/adj + sujet ou cod)
def verif_forme(arr, ins):


    # c'est les des insultes mais sans la classe listes_insultes ou les dégats juste les insultes
    # pour verifier le bon emplacement des mots choisis
    sujet_array = form_array_insults(ins.Sujet)

    verbe_array = form_array_insults(ins.Verbe)

    verbe_adj_array = form_array_insults(ins.Verbe_adj)

    adj_array = form_array_insults(ins.Adj)

    cod_array = form_array_insults(ins.COD)

    v1 = True  # verifie l'emplacement du sujet
    v2 = True  # verifie l'emplacement du verbe
    v3 = True  # verifie l'emplacement du cod ou adj
    v4 = True  # verifie l'emplacement du "et"
# on parcour le tableau du joueur
    for i in range(0, len(arr), 1):
        # la premiere case doit etre un sujet
        if i == 0:
            if (arr[i] in sujet_array) == False:
                v1 = False

        # la deuxieme case doit etre un verbe
        if i == 1:
            if (arr[i] in verbe_array or arr[i] in verbe_adj_array) == False:
                v2 = False

        # la troisieme case doit etre un adj ou cod dependant du verbe selectionné
        if i == 2:
            if ((arr[i-1] in verbe_array[slice(2)] and arr[i] in adj_array) or ((arr[i-1] in verbe_adj_array or arr[i-1] in verbe_array[slice(3, len(verbe_array))]) and (arr[i] in adj_array or arr[i] in cod_array)) or (arr[i-1] in verbe_adj_array and arr[i] in sujet_array and arr[i] != "tu")) == False:
                v3 = False

        # la quatrieme case doit etre un "et"
        if i == 3:
            if arr[i] != "et":
                v4 = False

        # si une des conditions n'est pas bonne ca donnera false
        if (v1 == False or v2 == False or v3 == False or v4 == False):
            return False
    return True


# cette fonction permet de gérer le combat
def Combat(PLAYER1, insult1, PLAYER2, insult2):
    # le nombre de mots ajoutés par joueur1 (sans compter les "et")
    words_P1 = 0

    # le nombre de mots ajoutés par joueu21 (sans compter les "et")
    words_P2 = 0

    list = []  # la liste des mots

    tabP1 = []  # la liste des mots du joueur 1

    tabP2 = []  # la liste des mots du joueur 2

    alt_list = ""  # liste qui va arreter le jeu dans le cas y'a plus du mots dans la liste

    s1 = 0  # nombre de dégats fait par joueur 1

    s2 = 0  # nombre de dégats fait par joueur 2

    multi_P1 = 1  # en cas de coup critique ca va multiplier le dégat

    multi_P2 = 1  # en cas de coup critique ca va multiplier le dégat

    # on arrete dès que la liste est vide ou un des deux joueurs est morts
    while PLAYER1.pv > 0 and PLAYER2.pv > 0 and alt_list != []:

        # l'affichage des messages de chaque joueur
        display_messages(PLAYER1.name, display_array_in_string(
            tabP1), PLAYER2.name, display_array_in_string(tabP2))

        # l'affichage des points de vie de chaque joueur
        print(PLAYER1.name, " HP = ", PLAYER1.pv)
        print(PLAYER2.name, " HP = ", PLAYER2.pv)

        # lorsque la liste est vide on génére d'autre mots
        if list == []:
            list = insult.generate_insults_list()
            alt_list = list

        if list != []:

            # l'affichage des mots disponibles
            Display_insult_list(list)

            # choix du joueur 1
            choix1 = saisie_char_num(
                len(list), "Le choix de "+PLAYER1.name+" : ")

            # on ajout le mot selectionné dans le tableau du joueur 1
            tabP1.append(list[choix1-1])

            # si le mot choisi est bonne on l'ajoute au tableau sinon on affiche "veuillez apprendre le grammaire"
            if verif_longue_phrases(tabP1, insult1) == True:
                if list[choix1-1] != "et":
                    words_P1 = words_P1+1
                if verif_weakness(list[choix1-1], insult1):
                    multi_P1 = randint(2, 4)
                    print("WEAKNESS !! * ", multi_P1)
            else:
                print("veuillez apprendre la grammaire !! ")
                tabP1.pop(len(tabP1)-1)

            display_messages(PLAYER1.name, display_array_in_string(
                tabP1), PLAYER2.name, display_array_in_string(tabP2))

            # le joueur a la possibilité d'attaquer s'il a une bonne phrase dans son tableau
            if words_P1 % 3 == 0 and words_P1 > 0 and tabP1[len(tabP1)-1] != "et":
                choixattack1 = saisie_char_num(
                    2, PLAYER1.name+" Tu veux attaquer?:\n\n1-->oui\n\n2-->non  ")
                if choixattack1 == 1:

                    # on fait la somme des degats des insultes choisis
                    s1 = (sum_insults(tabP1, insult1)*multi_P1)
                    print(PLAYER1.name, "a fait ", s1,
                          " de dégats à ", PLAYER2.name)

                    # on diminue les points de vie du joueur adversaire
                    PLAYER2.pv -= s1

                    multi_P1 = 1
                    tabP1 = []
                    words_P1 = 0

            print(PLAYER1.name, " HP = ", PLAYER1.pv)
            print(PLAYER2.name, " HP = ", PLAYER2.pv)

            # on enlève le mot selectionné de la liste
            list.remove(list[choix1-1])

            # on fait les memes etapes pour le deuxième joueur
            if list == []:
                list = insult.generate_insults_list()
                alt_list = list
            Display_insult_list(list)
            choix2 = saisie_char_num(
                len(list), "Le choix de "+PLAYER2.name+" : ")
            tabP2.append(list[choix2-1])
            if verif_longue_phrases(tabP2, insult2) == True:
                if list[choix2-1] != "et":
                    words_P2 = words_P2+1
                if verif_weakness(list[choix2-1], insult2):
                    multi_P2 = randint(2, 4)
                    print("WEAKNESS !! * ", multi_P2)
            else:
                print("veuillez apprendre la grammaire !! ")
                tabP2.pop(len(tabP2)-1)
            if words_P2 % 3 == 0 and words_P2 > 0 and tabP2[len(tabP2)-1] != "et":
                choixattack2 = saisie_char_num(
                    2, PLAYER2.name+" Tu veux attaquer?:\n\n1-->oui\n\n2-->non  ")
                if choixattack2 == 1:
                    s2 = (sum_insults(tabP2, insult2)*multi_P2)
                    print(PLAYER2.name, "a fait ", s2,
                          " de dégats à ", PLAYER1.name)
                    PLAYER1.pv -= s2
                    multi_P2 = 1
                    tabP2 = []
                    words_P2 = 0
            list.remove(list[choix2-1])
            if list == []:
                list = insult.generate_insults_list()
                alt_list = list
    if(PLAYER1.pv<PLAYER2.pv):
        print(PLAYER2.name," est gagnant!!!")
    else:
        print(PLAYER1.name," est gagnant!!!")


Combat(PLAYER1, insult1, PLAYER2, insult2)
