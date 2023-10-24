#helper.py
""" pour notre premier projet"""

from PIL import Image
import numpy as np

def suite(z, c) -> complex:
    """Générateur des éléments de la suite $z_{n+1}=z_n^2+c$"""
    while True:
        yield z
        z = z ** 2 + c

def suite_mandelbrot(c):
    """Renvoie la suite de Mandelbrot"""
    return suite(0, c)

def suite_julia(zandidat,carametre)-> complex:
    """Renvoie la suite de julia pour candidat et parametre"""
    return suite(zandidat,carametre)


def is_in_Mandelbrot(c=0.251, max_iter=100):
    """
    Renvoie si un complexe appartient à l'ensemble de Mandelbrot
    >>> is_in_Mandelbrot(c=0.251)
    False
    """
    compteur = 0
    for elem in suite_mandelbrot(c):
        if np.abs(elem) > 10:
            return False
        if compteur == max_iter:
            return True
        compteur += 1

def is_in_Julia(z=0.25+0.25j,c=0.25,max_iter=200):
    """
    Renvoie si un complexe z appartient à l'ensemble de Julia pour c fixé
    >>> is_in_Julia(z=0.25+0.25j,c=0.25)
    True
    """
    eps = 10**(-2)
    i=0
    converge = True
    for z in suite_julia(z,c):
        if i < max_iter :
            if abs(z) > 2 : 
                return(not converge)
            else:
                i+=1
        if i == max_iter :
            return(converge)


def plot_mandelbrot(
        zmin=complex(-0.7440 + 0.1305j),
        zmax=complex(-0.7425 + 0.1320j),
        pixel_size=5e-6,
        max_iter=200,
        figname="Mandelbrot.png"): 
    """Affiche les nombres complexes compris entre zmin et zmax qui appartiennent à l'ensemble de Mandelbrot"""

    xmin = zmin.real
    xmax = zmax.real
    ymin = zmin.imag
    ymax = zmax.imag

    X = np.arange(xmin, xmax, pixel_size)
    Y = np.arange(ymin, ymax, pixel_size)
    Matrice = X[:, np.newaxis] + Y[np.newaxis, :] * 1j

    g = np.vectorize(is_in_Mandelbrot)

    mask = g(Matrice, max_iter)  # étape la plus couteuse du code...
    im = Image.fromarray(True ^ mask)

    im.show()
    im.save(figname)


def plot_julia(c=-0.8 + 0.156j,
                zmin=-2-1j,
                zmax=2+1j,
                pixel_size=5e-3,
                max_iter=100,
                figname="Julia.png"): 
    """Affiche les nombres complexes compris entre zmin et zmax qui appartiennent à l'ensemble de Julia pour c fixé"""

    xmin = zmin.real
    xmax = zmax.real
    ymin = zmin.imag
    ymax = zmax.imag

    X = np.arange(xmin, xmax, pixel_size)
    Y = np.arange(ymin, ymax, pixel_size)
    Matrice = X[:, np.newaxis] + Y[np.newaxis, :] * 1j

    g = np.vectorize(is_in_Julia)

    mask = g(Matrice,c,max_iter)  # étape la plus couteuse du code...
    im = Image.fromarray(True ^ mask)

    im.show()
    im.save(figname)
