from collections import namedtuple, defaultdict
import csv
from datetime import datetime, date, time

Carrera = namedtuple("Carrera", "nombre,escuderia,fecha_carrera,temperatura_min,vel_max,\
    duracion,posicion_final,ciudad, top_6_vueltas,tiempo_boxes,nivel_liquido")

def parser(cadena:str)->list[float]:
    res = []
    cadena = cadena.replace("[","")
    cadena = cadena.replace("]","")
    for i in cadena.split("/"):
        if i.strip() == "-":
            i = 0
        res.append(float(i))
    return res

def booleano(cadena:str)->bool:
    res = True
    if cadena == "1":
        return res
    elif cadena.lower() == "no":
        res = False
    return res

def lee_carreras(fichero:str)->list[Carrera]:
    res = []
    with open(fichero, 'rt', encoding = 'utf-8')as f:
        lector = csv.reader(f, delimiter=';')
        next (lector)
        for nombre,escuderia,fecha_carrera,temperatura_min,vel_max,\
            duracion,posicion_final,ciudad, top_6_vueltas,tiempo_boxes,nivel_liquido in lector:
            fecha_carrera = datetime.strptime(fecha_carrera, "%d-%m-%y").date()
            temperatura_min = int(temperatura_min)
            vel_max = float(vel_max)
            duracion = float(duracion)
            posicion_final = int(posicion_final)
            top_6_vueltas = parser(top_6_vueltas)
            tiempo_boxes = float(tiempo_boxes)
            nivel_liquido = booleano(nivel_liquido)
            res.append(Carrera(nombre,escuderia,fecha_carrera,temperatura_min,vel_max,\
            duracion,posicion_final,ciudad, top_6_vueltas,tiempo_boxes,nivel_liquido))
        return res

def media_tiempo_boxes(carreras:list[Carrera], ciudad:str, fecha:date = None)->float:
    res, contador = 0, 0
    for i in carreras:
        if i.ciudad == ciudad and (fecha == None or i.fecha_carrera == fecha):
            res+=i.tiempo_boxes
            contador+=1
    if res != 0 :
        return res/contador
    elif res == 0 :
        return 0 

def pilotos_menor_tiempo_medio_vueltas_top(carreras:list[Carrera], n:int)->list[tuple[str, date]]:
    aux = defaultdict(tuple)
    lista = []
    for i in carreras:
        if 0.0 not in i.top_6_vueltas:
            aux[(i.nombre, i.fecha_carrera)]=sum(i.top_6_vueltas)/len(i.top_6_vueltas)
    res = sorted(aux.items(), key = lambda x:x[1])
    for i in res[:n]:
        lista.append(i[0])
    return lista

def ratio_tiempo_boxes_total(carreras:list[Carrera])->list[tuple[str,date, float]]:
    t_dia = defaultdict(float)
    t_piloto = defaultdict(float)
    res = defaultdict(float)
    for i in carreras:
        t_dia[i.fecha_carrera]+=(i.tiempo_boxes)
        t_piloto[(i.nombre, i.fecha_carrera)]+=(i.tiempo_boxes)
    for c,v in t_piloto.items():
        for c2,v2 in t_dia.items():
            if c[1] == c2:
                res[c] = round(v/v2, 3)
    return sorted(res.items(), key = lambda x:x[1], reverse = True)

def calcular_punto(carrera:list[Carrera])->int:
    if carrera.posicion_final == 3:
        res = 10
    elif carrera.posicion_final == 2:
        res = 25
    elif carrera.posicion_final == 1:
        res = 50
    else:
        res = 0
    return res

def puntos_piloto_anyos(carreras:list[Carrera])->dict[str, list[int]]:
    aux = defaultdict(int)
    res = defaultdict(list)
    for i in carreras:
        aux[(i.nombre, i.fecha_carrera.year)]+=(calcular_punto(i))
    aux2 = sorted(aux.items(), key = lambda x:x[0][1])
    for j in aux2:
        res[j[0][0]].append(j[1])
    return res

def mejor_escuderia_anyo(carreras:list[Carrera], a:int)->str:
    res = defaultdict(int)
    for i in carreras:
        if i.fecha_carrera.year == a and i.posicion_final == 1:
            res[i.escuderia]+=1
    return max(res.items(), key = lambda x:x[1])[0]