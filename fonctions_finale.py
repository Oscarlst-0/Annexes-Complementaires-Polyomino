from case_finale import Case, Polyo
from PIL import Image, ImageDraw
import pyglet

##################################################
#                 Cas Symétrie                   #
##################################################

paterne_m = [1, 0, 1, 1, 1, 1]


def calcul_coordonnées_cas_symétrique(n, largeur=20):
    liste_finale = [
        [(largeur, largeur)]
    ]  # au lieu de (0,0) pour soucis d'affichage (pas pile dans le coin de la fenêtre)
    m = 0
    if n % 2 == 0:
        m = n // 2
    else:
        m = (n + 1) // 2

    dernier_polyo = []

    if n > 9:
        x = n // 6
        y = (n - 10) % 6
        while x > 1:
            m += 1
            x -= 1
        m += x * paterne_m[y]

        if ((n - 10) % 3) == 0:  # test d'un multiple de 3 pour n-10
            m -= 1
            c = 10
            dernier_polyo = [
                (largeur, largeur),
                (40, 20),
                (40, 40),
                (60, 40),
                (60, 60),
                (80, 60),
                (80, 80),
                (100, 80),
                (100, 100),
            ]
            while c != n:
                x = dernier_polyo[-1][0]
                y = dernier_polyo[-1][1]
                dernier_polyo.append((x + 20, y))
                dernier_polyo.append((x + 20, y + 20))
                c += 3

    for i in range(m):
        # problème si je parcours une liste que je modifie à chaque itération
        for liste in liste_finale.copy():
            longueur = len(liste)
            for j in range(longueur):
                x = liste[j][0]
                y = liste[j][1]
                tupple1 = (x + largeur, y)

                # Ajout tupple 1 possible ou non:
                if tupple1[1] <= tupple1[0]:
                    liste_inter1 = liste.copy()
                    if tupple1 not in liste_inter1:
                        liste_inter1.append(tupple1)
                        liste_inter1.sort()
                        if liste_inter1 not in liste_finale and compteur_inf_egal(
                            n, liste_inter1
                        ):
                            liste_finale.append(liste_inter1)

                tupple2 = (x, y + largeur)

                # Ajout tupple 2 possible ou non:
                if tupple2[1] <= tupple2[0]:
                    liste_inter2 = liste.copy()
                    if tupple2 not in liste_inter2:
                        liste_inter2.append(tupple2)
                        liste_inter2.sort()
                        if liste_inter2 not in liste_finale and compteur_inf_egal(
                            n, liste_inter2
                        ):
                            liste_finale.append(liste_inter2)

    liste_finale.append(dernier_polyo)
    return liste_finale


def compteur_inf_egal(n, liste):
    compteur_n = 0
    for element in liste:
        if element[0] == element[1]:
            compteur_n += 1
        else:
            compteur_n += 2
    if compteur_n <= n:
        return True


def selection_solutions_n_cas_symétrique(n, largeur=20):
    liste_coordonnées = calcul_coordonnées_cas_symétrique(n, largeur)
    liste_solutions = []
    for liste in liste_coordonnées:
        compteur = 0
        for element in liste:
            if element[0] == element[1]:
                compteur += 1  # on vérifie si c'est une case centrale
            else:
                compteur += 2  # si c'est un case non centrale, elle compte double en terme de carré par symétrie lorsqu'on construira le polyomino
        if compteur == n:
            liste_solutions.append(liste)

    return liste_solutions


def liste_polyo_cas_symétrique(liste, largeur=20):
    liste_polyo = []
    for sous_liste in liste:
        polyo = Polyo()
        for coord in sous_liste:
            # on ajoute une case pour chaque couple de coordonnée de la sous_liste
            if coord[0] == coord[1]:
                polyo.cases.append(Case(coord[0], coord[1], largeur))
            else:  # ajout de la case et son symétrique
                polyo.cases.append(Case(coord[0], coord[1], largeur))
                polyo.cases.append(Case(coord[1], coord[0], largeur))
        liste_polyo.append(polyo)

    return liste_polyo


##################################################
#                 Cas Général                    #
##################################################


def calcul_coordonnées_cas_général(n, largeur=20):
    liste_finale = [
        [(largeur, largeur)]
    ]  # au lieu de (0,0) pour soucis d'affichage (pas pile dans le coin de la fenêtre)

    for i in range(n):
        # problème si je parcours une liste que je modifie à chaque itération
        for liste in liste_finale.copy():
            longueur = len(liste)
            for j in range(longueur):
                x = liste[j][0]
                y = liste[j][1]
                tupple1 = (x + largeur, y)

                # Ajout tupple 1 possible ou non:

                liste_inter1 = liste.copy()
                if tupple1 not in liste_inter1:
                    liste_inter1.append(tupple1)
                    liste_inter1.sort()
                    if liste_inter1 not in liste_finale and compteur_cas_général(
                        n, liste_inter1
                    ):
                        liste_finale.append(liste_inter1)

                tupple2 = (x, y + largeur)

                # Ajout tupple 2 possible ou non:

                liste_inter2 = liste.copy()
                if tupple2 not in liste_inter2:
                    liste_inter2.append(tupple2)
                    liste_inter2.sort()
                    if liste_inter2 not in liste_finale and compteur_cas_général(
                        n, liste_inter2
                    ):
                        liste_finale.append(liste_inter2)

    return liste_finale


def compteur_cas_général(n, liste):
    compteur_n = 0
    for element in liste:
        compteur_n += 1
    if compteur_n <= n:
        return True


def selection_solutions_n_cas_général(n, largeur=20):
    liste_coordonnées = calcul_coordonnées_cas_général(n, largeur)
    liste_solutions = []
    for liste in liste_coordonnées:
        compteur = 0
        for element in liste:
            compteur += 1  # on vérifie si c'est une case centrale
        if compteur == n:
            liste_solutions.append(liste)

    return liste_solutions


def liste_polyo_cas_général(liste, largeur=20):
    liste_polyo = []
    for sous_liste in liste:
        polyo = Polyo()
        for coord in sous_liste:
            polyo.cases.append(Case(coord[0], coord[1], largeur))
        liste_polyo.append(polyo)

    return liste_polyo


##################################################
#                 Conversion Image               #
##################################################


def export_polyominos_png(liste_polyo, largeur_img, hauteur_img, filename="polyominos.png"):
    img = Image.new("RGB", (largeur_img, hauteur_img), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    for polyo in liste_polyo:
        for case in polyo.cases:
            x = int(case.x)
            y = hauteur_img - int(case.y)
            largeur = int(case.largeur)
            draw.rectangle(
                [x, y, x + largeur, y + largeur],
                outline=(150, 150, 150),
                fill=(255, 255, 255),
            )
            draw.rectangle(
                [x + 1, y + 1, x + largeur - 1, y + largeur - 1], fill=(255, 255, 255)
            )
    img.save(filename)


def polyo_dirigés_images(n, taille_case=20):

    window = pyglet.window.Window(visible=False)

    screen = window.screen
    largeur_fenetre = screen.width
    window.close()

    largeur_polyo = n * taille_case

    liste_coordonnées = selection_solutions_n_cas_général(n, taille_case)
    liste_polyo = liste_polyo_cas_général(liste_coordonnées, taille_case)

    espacement = largeur_polyo + taille_case
    nombre_sur_une_rangée = largeur_fenetre // espacement

    for i in range(len(liste_polyo)):
        espacement_x = (i % nombre_sur_une_rangée) * espacement
        espacement_y = (i // nombre_sur_une_rangée) * espacement
        for case in liste_polyo[i].cases:
            case.x += espacement_x
            case.y += espacement_y

    max_y = max(case.y + case.largeur for polyo in liste_polyo for case in polyo.cases)

    filename = f"polyominos_général_{n}_{taille_case}pxl.png"
    export_polyominos_png(liste_polyo, largeur_fenetre, max_y, filename=filename)
    print(f"Fichier image png exporté : {filename}")


def polyo_dirigés_symétriques_images(n, taille_case=20):

    if n == 2:
        print("Il n'y a aucun polyomino dirigé symétrique pour n = 2.")
        return None

    window = pyglet.window.Window(visible=False)

    largeur_polyo = 0
    if n % 2 == 0:
        largeur_polyo = (n // 2) * taille_case
    else:
        largeur_polyo = ((n + 1) // 2) * taille_case

    screen = window.screen
    largeur_fenetre = screen.width
    window.close()

    liste_coordonnées = selection_solutions_n_cas_symétrique(n, taille_case)
    liste_polyo = liste_polyo_cas_symétrique(liste_coordonnées, taille_case)

    espacement = largeur_polyo + taille_case
    nombre_sur_une_rangée = largeur_fenetre // espacement

    for i in range(len(liste_polyo)):
        espacement_x = (i % nombre_sur_une_rangée) * espacement
        espacement_y = (i // nombre_sur_une_rangée) * espacement
        for case in liste_polyo[i].cases:
            case.x += espacement_x
            case.y += espacement_y

    max_y = max(case.y + case.largeur for polyo in liste_polyo for case in polyo.cases)

    filename = f"polyominos_symétrie_{n}_{taille_case}pxl.png"
    export_polyominos_png(liste_polyo, largeur_fenetre, max_y, filename=filename)
    print(f"Fichier image png exporté : {filename}")
