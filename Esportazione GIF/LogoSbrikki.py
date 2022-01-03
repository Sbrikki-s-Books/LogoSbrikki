from __future__ import division 
from svg.path import Path, Line, Arc, CubicBezier, QuadraticBezier, parse_path
import turtle
from svgpathtools import svg2paths, wsvg


option=1

svgpath = """m 76,232.24998 c 81.57846,-49.53502 158.19366,-20.30271 216,27 61.26714,59.36905 79.86223,123.38417 9,156
-80.84947,31.72743 -125.19991,-53.11474 -118,-91 v 0 """ #random path
path = parse_path(svgpath)
altezza = 1
larghezza = 1

def draw(t,pts): # funzione che, dato un cursore ed una collezione di punti esegue il disegno (da richiamare per ogni tracciato) 
    t.penup()
    t.setpos(pts[0])
    t.down()
    for x,y in pts[1:]:
        t.setpos(x,y)

def riscalamento(nuova_altezza, nuova_larghezza): #funzione di riscalamento dell'immagine
    global paths
    global altezza
    global larghezza
    for i in range(len(paths)):# calcolo l'interpolazione dei tracciati 
        path=paths[i]
        pts.append( [ (((p.real-min_x-larghezza/2)/larghezza)*nuova_larghezza,-((p.imag-min_y-altezza/2)/altezza)*nuova_altezza) for p in (path.point(i/n) for i in range(0, n+1))])
    altezza=nuova_altezza
    larghezza=nuova_larghezza    

def sbrikki():
    global paths
    global altezza
    global larghezza
    
#----------------------------------------------------------------------------------------
# OPERAZIONI PRELIMINARI    
#----------------------------------------------------------------------------------------

    t = turtle.Turtle() # cursore

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

#----------------------------------------------------------------------------------------
# INTERPOLAZIONE DEI TRACCIATI    
#----------------------------------------------------------------------------------------

    max_frame=1000 # dimensione massima immagine (il risultato deve essere sempre stampabile in un quadrato max_frame*max_frame)

#--------- Eventuale riscalamento ------------------------------------
    if max((altezza,larghezza))>max_frame:
        if altezza>larghezza:
            nuova_larghezza=(larghezza/altezza)*max_frame
            riscalamento( max_frame,nuova_larghezza)
        else:
            nuova_altezza=(altezza/larghezza)*max_frame
            riscalamento( nuova_altezza,max_frame)
    else:           # se non c'è riscalamento viene semplicemente calcolata l'interpolazione
        for i in range(len(paths)):
            path=paths[i]
            pts.append ( [ ((p.real-min_x-larghezza/2),-(p.imag-min_y-altezza/2)) for p in (path.point(i/n) for i in range(0, n+1))])


#----------------------------------------------------------------------------------------
# STAMPA    
#----------------------------------------------------------------------------------------

#--------- Creazione schermo -----------------------------------------
    s = turtle.Screen()
    #s.screensize(larghezza,altezza)
    #s.setup(larghezza+50,altezza+50)

#--------- Stampa ----------------------------------------------------
    for i in range(len(paths)):
        draw(t,pts[i])

#--------- Posizionamento cursore ad angolo -----------------------------------------
    t.penup()
    t.setpos((-larghezza/2,-altezza/2))
