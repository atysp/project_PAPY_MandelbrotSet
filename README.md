## README

Bonjour ! 
On vous met à disposition le script qu'on utilise pour afficher l'ensemble de Mandelbrot et de Julia :)

# Fonctionnement:

La commande **MandelbrotPlot -o mandelbrot.png** affiche l'ensemble de Mandelbrot et l'enregistre dans une image nommée "mandelbrot". 
La commande **MandelbrotPlot --zmin=-0.7440+0.1305j --zmax=-0.7425+0.1320j --pixel_size=5e-6 --max-iter=50 -o Mandelbrot_tentacle.png** affiche les nombres complexes compris entre zmin et zmax qui appartiennent à l'ensemble de Mandelbrot et l'enregistre dans une image nommée Mandelbrot_tentacle.

Les mêmes commande sont accessible pour l'ensemble de Julia, seulement vous pourrez préciser si vous le souhaitez le paramètre c (-c 0.251 par exemple).

# Aide:

La commande **MandelbrotPlot -h** ainsi que la commande **JuliaPlot -h** vous permettent d'obtenir plus d'informations.

Pour que le temps d'attente ne soit pas trop long, on recommande de choisir une taille de pixel adaptée.
Par exemple:
 -- une taille de pixel de l'ordre de 5e-6 conviendra pour afficher l'ensemble de Mandelbrot. 
 -- une taille de pixel de l'ordre de 5e-3 conviendra pour afficher l'ensemble de Julia.

La biblipthèque utilise numpy, Pillow et des tests unitaires peuvent être fait avec Pytest.

