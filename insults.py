from random import randint
from liste_insultes import Liste_insultes


class INSULT:
    def __init__(self, adv):
        # les faiblesses des caractères(faut mettre la faiblesse de chacun dans son tableau) et vaut mieux de copier coller des tableaux des insultes
        # car ca peut causer des problèmes si les mots de faiblesse ne sont pas identiques à celle des tableaux d'insultes
        # faiblesses du dame
        if adv == "Dame":
            self.faiblesse = ["ton chien","trop vieux","ton chat","ton mari"]

        # faiblesse du gentleman
        elif adv == "gentleman":
            self.faiblesse = ["ta femme", "Ton chapeau",
                              "l'honneur", "es(t) lent comme", "ton habillage","ton enfant"]

        # faiblesse du king
        elif adv == "king":
            self.faiblesse = ["ta femme", "grand",
                              "l'honneur", "ton père", "star wars","la/de vie","La casa del papel","Prison Break"]

        # faiblesse du poor
        elif adv == "poor":
            self.faiblesse = ["la/de vie", "grand",
                              "l'honneur", "tu", "Ta famille","ton habillage","toi"]

        # faiblesse du gangster
        elif adv == "gangster":
            self.faiblesse = ["ta femme", "ton garage",
                              "l'honneur", "ton père", "Ta famille","ta voiture"]

        # faiblesse du master ocean
        elif adv == "master ocean":
            self.faiblesse = ["ta femme", "ton dauphin",
                              "l'honneur", "un petit con","es(t) con comme", "ton habillage"]

# pour ajouter un mot à la liste faut juste appeler Listes_insultes et mettre l'insulte et sa dégat
# vous pouvez copier ca et le mettre ou vous voulez ajouter l'insulte : , Liste_insultes("insulte", 0)
        self.Sujet = [Liste_insultes("tu", 6), Liste_insultes("ton père", 14), Liste_insultes("ta mère", 20), Liste_insultes(
            "ton mari", 8), Liste_insultes("ta femme", 8), Liste_insultes("ta soeur", 10),
             Liste_insultes("ton frère", 10), Liste_insultes("ton habillage", 12), Liste_insultes("ton chien", 6), Liste_insultes("ton chat", 6),
              Liste_insultes("ton hamster", 6), Liste_insultes("ton voisin", 6), Liste_insultes("ton enfant", 15),
               Liste_insultes("ta voiture", 12), Liste_insultes("ton garage", 10), Liste_insultes("ton dauphin", 15), Liste_insultes("Ta famille", 18), Liste_insultes("Ton chapeau", 18)]
        self.Verbe = [Liste_insultes("es(t)", 7), Liste_insultes("n'es(t) pas", 8), Liste_insultes(
            "n'es(t) pas", 9), Liste_insultes("a(s)", 10), Liste_insultes("n'a(s) pas", 10), Liste_insultes("n'a(s) pas regardé", 6), Liste_insultes("rassemble(s) à", 6), Liste_insultes("ne connait pas", 6), Liste_insultes("ne sait pas", 7), Liste_insultes("n'a(s) jamais regardé", 8)]
        self.Verbe_adj = [Liste_insultes("es(t) lent comme", 13), Liste_insultes(
            "es(t) stupide comme", 14), Liste_insultes("es(t) con comme", 14), Liste_insultes("est bete comme", 16), Liste_insultes("n'a(s) pas de vie comme", 10), Liste_insultes("es(t) trop fine comme", 12), Liste_insultes("est aveugle comme", 15), Liste_insultes("es(t) idiot comme", 13), Liste_insultes("es(t) pauvre comme", 10)]
        self.Adj = [Liste_insultes("une stupide", 10), Liste_insultes("un(e) con", 8), Liste_insultes("un(e) bete", 14), Liste_insultes(
            "intelligent(e)", 6), Liste_insultes("un petit con", 5), Liste_insultes("un grand con", 7), Liste_insultes("un(e) idiot", 7), Liste_insultes("un(e) pauvre", 7), Liste_insultes("un vieux", 12)]
        self.COD = [Liste_insultes("star wars", 9), Liste_insultes("le train", 7), Liste_insultes("l'intelligence", 5), Liste_insultes("l'honneur", 7), Liste_insultes("Prison Break", 9), Liste_insultes("La casa del papel", 9), Liste_insultes(
            "la maison", 8), Liste_insultes("la merde", 7), Liste_insultes("une pyramide", 12), Liste_insultes("toi", 9), Liste_insultes("la/de vie", 10), Liste_insultes("la vache", 12)]

        self.liaison = ["et", "et", "et", "et", "et", "et",
                        "et", "et", "et", "et", "et", "et", "et", "et", "et", "et", "et", "et", "et", "et", "et"]

    def generate_random_list(self):
        Random_List = []
        if len(self.Sujet) > 0:
            sujet = randint(4, 5) # combien de fois on aura un sujet dans la liste
            suj_val = randint(0, len(self.Sujet)-1)
            for j in range(0, sujet, 1):
                Random_List.append(self.Sujet[suj_val].name)
                suj_val = randint(0, len(self.Sujet)-1)
            while self.Sujet[suj_val].name in Random_List:
                suj_val=randint(0,len(self.Sujet)-1)
        if len(self.Verbe) > 0:
            verbe = randint(2, 3)# combien de fois on aura un verbe dans la liste
            ver_val = randint(0, len(self.Verbe)-1)
            for vb in range(0, verbe, 1):
                Random_List.append(self.Verbe[ver_val].name)
                ver_val = randint(0, len(self.Verbe)-1)
            while self.Verbe[ver_val].name in Random_List:
                ver_val=randint(0,len(self.Verbe)-1)
        if len(self.Verbe_adj) > 0:
            verbe_adj = randint(2, 3)# combien de fois on aura un verbe_adj dans la liste
            ver_adj_val = randint(0, len(self.Verbe_adj)-1)
            for vb_adj in range(0, verbe_adj, 1):
                Random_List.append(self.Verbe_adj[ver_adj_val].name)
                ver_adj_val = randint(0, len(self.Verbe_adj)-1)
            while self.Verbe[ver_adj_val].name in Random_List:
                ver_adj_val=randint(0,len(self.Verbe_adj)-1)
        if len(self.Adj) > 0:
            adjective = randint(2, 3)# combien de fois on aura un adjectif dans la liste
            adj_val = randint(0, len(self.Adj)-1)
            for adj in range(0, adjective, 1):
                Random_List.append(self.Adj[adj_val].name)
                adj_val = randint(0, len(self.Adj)-1)
                while self.Adj[adj_val].name in Random_List:
                    adj_val=randint(1,len(self.Adj)-1)
        if len(self.COD) > 0:
            cod_rep = randint(2, 3)# combien de fois on aura un COD dans la liste
            cod_val = randint(0, len(self.COD)-1)
            for cod_i in range(0, cod_rep, 1):
                Random_List.append(self.COD[cod_val].name)
                cod_val = randint(0, len(self.COD)-1)
                while self.COD[cod_val].name in Random_List:
                    cod_val=randint(0,len(self.COD)-1)
        if len(self.liaison) > 0:
            lie_rep = randint(2, 3)# combien de fois on aura une liaison dans la liste
            lie_val = randint(0, len(self.liaison)-1)
            for lie_i in range(0, lie_rep, 1):
                Random_List.append(self.liaison[lie_val])
                self.liaison.remove(self.liaison[lie_val])
                lie_val = randint(0, len(self.liaison)-1)
        return Random_List

    def generate_insults_list(self):
        print("\n")
        List = self.generate_random_list()
        if List != []:
            n = len(List)
            displayed_list = []
            for index in range(0, n, 1):
                List_random_element = randint(0, len(List)-1)
                displayed_list.append(List[List_random_element])
                List.remove(List[List_random_element])
        return displayed_list
