from svg.path import Path, Line, Arc, CubicBezier, QuadraticBezier, parse_path
from svgpathtools import svg2paths, wsvg

from turtle2gif import *
import turtle

from LogoSbrikki import sbrikki

option=1 


#--------- Lettura immagine vettoriale -------------------------------
if option==1:
    paths, attributes = svg2paths('Logo.svg')
if option==2:
    paths, attributes = svg2paths('Logotipo.svg')

#--------- Preparazione per intepolazione tracciato ------------------
n = 100  # numero di segmenti in cui dividere un tracciato
pts=[]


#--------- Calcolo dimensioni riquadro -------------------------------
min_xs=[]
min_ys=[]
max_xs=[]
max_ys=[]
for i in range(len(paths)):
    path=paths[i]
    ptsx = [ p.real for p in (path.point(i/n) for i in range(0, n+1))]
    ptsy = [ p.imag for p in (path.point(i/n) for i in range(0, n+1))]
    min_xs.append(min(ptsx))
    min_ys.append(min(ptsy))
    max_xs.append(max(ptsx))
    max_ys.append(max(ptsy))
min_x=min(min_xs)
min_y=min(min_ys)
max_x=max(max_xs)
max_y=max(max_ys)
altezza=max_y-min_y
larghezza=max_x-min_x


max_frame=1000 # dimensione massima immagine (il risultato deve essere sempre stampabile in un quadrato max_frame*max_frame)

#--------- Eventuale riscalamento ------------------------------------
if max((altezza,larghezza))>max_frame:
    if altezza>larghezza:
        nuova_larghezza=(larghezza/altezza)*max_frame
    else:
        nuova_altezza=(altezza/larghezza)*max_frame

s = turtle.Screen()
s.screensize(larghezza,altezza)
s.setup(larghezza+50,altezza+50,None,0)



convert2gif(sbrikki)
