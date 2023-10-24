from TP4.helper import *

# Tester l'appartenance d'un point à l'ensemble de Mandelbrot:
def test_is_in_Mandelbrot():
    assert is_in_Mandelbrot(c=0.251,max_iter=90)==True

# Dont on peut augmenter le nombre d'itérations pour les points près de la frontière:
def test_is_in_Mandelbrot1():
    assert is_in_Mandelbrot(c=0.251,max_iter=100)==False

# Tester l'appartenance d'un point à l'ensemble de Julia:
def test_is_in_Julia():
    assert is_in_Julia(z=0.25+0.25j,c=0.25,max_iter=100)==True

# Tester l'affichage de l'ensemble de Mandelbrot:
def test_plot_mandelbrot():
    plot_mandelbrot()

# Tester l'affichage de l'ensemble de Julia:
def test_plot_mandelbrot():
    plot_julia()





