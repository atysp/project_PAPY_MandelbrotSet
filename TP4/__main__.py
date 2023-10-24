#Contenu de __main__.py
"""Main call to TP4. Mostly a parser."""
import argparse
from TP4.helper import plot_mandelbrot
from TP4.helper import plot_julia

def mandelbrot():
    """Fonction principale"""

    parser = argparse.ArgumentParser(description='Représente l ensemble de Mandelbrot')
    parser.add_argument('--zmin', metavar='zmin', type=complex,
                        default=-0.7440 + 0.1305j,
                        help='nombre complexe situé en bas à gauche pour le test')
    parser.add_argument('--zmax', metavar='zmax', type=complex,
                        default=-0.7425 + 0.1320j,
                        help='nombre complexe situé en haut à droite pour le test') 
    parser.add_argument('--pixel_size', metavar='pixel_size', type=float,
                        default=5e-6,
                        help="taille d'un pixel")   
    parser.add_argument('--max-iter', metavar='max_iter', type=int,
                        default=200,
                        help="nombre d'itérations de la fonction d'appartenance à l'ensemble de Mandelbrot")          
    parser.add_argument('-o', '--figname', metavar='figname', type=str,
                        default="Mandelbrot.png",
                        help="nom du fichier dans lequel on sauvegarde la figure")
    args = parser.parse_args()
    
    zmin=args.zmin
    zmax=args.zmax
    pixel_size=args.pixel_size
    max_iter=args.max_iter
    figname=args.figname

    plot_mandelbrot(
    zmin=zmin,
    zmax=zmax,
    pixel_size=pixel_size,
    max_iter=max_iter,
    figname=figname)

def julia():
    """Fonction principale"""

    parser = argparse.ArgumentParser(description='Représente l ensemble de Julia')
    parser.add_argument('-c', metavar='c', type=complex,
                        default=-0.8+0.156j,
                        help='incrémentation complexe de la suite de Julia')  
    parser.add_argument('--zmin', metavar='zmin', type=complex,
                        default=-2-1j,
                        help='nombre complexe situé en bas à gauche pour le test')
    parser.add_argument('--zmax', metavar='zmax', type=complex,
                        default=2+1j,
                        help='nombre complexe situé en haut à droite pour le test')      
    parser.add_argument('--pixel_size', metavar='pixel_size', type=float,
                        default=5e-3,
                        help="taille d'un pixel")   
    parser.add_argument('--max-iter', metavar='max_iter', type=int,
                        default=100,
                        help="nombre d'itérations de la fonction d'appartenance à l'ensemble de Mandelbrot")          
    parser.add_argument('-o', '--figname', metavar='figname', type=str,
                        default="Julia.png",
                        help="nom du fichier dans lequel on sauvegarde la figure")
    args = parser.parse_args()
    
    c=args.c
    zmin=args.zmin
    zmax=args.zmax
    pixel_size=args.pixel_size
    max_iter=args.max_iter
    figname=args.figname

    plot_julia(
    c=c,
    zmin=zmin,
    zmax=zmax,
    pixel_size=pixel_size,
    max_iter=max_iter,
    figname=figname)

if __name__=="__main__":
    julia()

