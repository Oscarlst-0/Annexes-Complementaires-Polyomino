from fonctions_finale import (
    selection_solutions_n_cas_symétrique,
    liste_polyo_cas_symétrique,
    export_polyominos_png,
)
import pyglet
import time

start = time.time()

n = 16  # int(input("Entrez le nombre de carrés voulus : "))

window = pyglet.window.Window(visible=False)

screen = window.screen
largeur_fenetre = screen.width
hauteur_fenetre = screen.height
window.close()


taille_case = 20
largeur_polyo = 0
if n % 2 == 0:
    largeur_polyo = (n // 2) * taille_case
else:
    largeur_polyo = ((n + 1) // 2) * taille_case

liste_coordonnées = selection_solutions_n_cas_symétrique(n, taille_case)
# print(liste_coordonnées)

print(f"Il y a : {len(liste_coordonnées)} polyominos différents pour n = {n}.")

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

end = time.time()
print(f"Temps d'exécution : {end - start:.2f} secondes")


class Screen(pyglet.window.Window):
    def __init__(self):
        super().__init__(fullscreen=True)
        self.decalage = 0

    def on_draw(self):
        self.clear()
        for polyo in liste_polyo:
            for case in polyo.cases:
                case.draw(decalage=self.decalage)

    def on_key_press(self, symbol):
        if symbol == pyglet.window.key.ESCAPE:
            self.close()
        if symbol == pyglet.window.key.UP:
            self.decalage -= espacement
        elif symbol == pyglet.window.key.DOWN:
            self.decalage += espacement


fen = Screen()
pyglet.app.run()


filename = f"polyominos_symétrie_{n}_{taille_case}pxl.png"
export_polyominos_png(liste_polyo, largeur_fenetre, max_y, filename=filename)
print(f"Fichier image png exporté : {filename}")
