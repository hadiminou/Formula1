from f1 import*

def test_lee_carreras(datos:list[Carrera]):
    print("\ntest_lee_carreras")
    print(f"\nnumero de registros leidos: {len(datos)}")
    print(f"\nlos dos primeros: {datos[:2]}")
    print(f"\nlos dos ultimos: {datos[-2:]}")

def test_media_tiempo_boxes(datos:list[Carrera]):
    print("\ntest_media_tiempo_boxes")
    ciudad = "Barcelona"
    print(f"La media de tiempo en boxes en la ciudad de Barcelona es de\
    {media_tiempo_boxes(datos, ciudad)} segundos.")

def test_pilotos_menor_tiempo_medio_vueltas_top(datos:list[Carrera]):
    print("\ntest_pilotos_menor_tiempo_medio_vueltas_top")
    n = 4
    print(f"Los {n} pilotos con menor tiempo medio son: {pilotos_menor_tiempo_medio_vueltas_top(datos, n)}")

def test_ratio_tiempo_boxes_total(datos:list[Carrera]):
    print("\ntest_ratio_tiempo_boxes_total")
    for i in ratio_tiempo_boxes_total(datos):
        print(i)

def test_puntos_piloto_anyos(datos:list[Carrera]):
    print("\ntest_puntos_piloto_anyos")
    for i in puntos_piloto_anyos(datos).items():
        print(f"{i[0]} --> {i[1]}")

def test_mejor_escuderia_anyo(datos:list[Carrera]):
    print("\ntest_mejor_escuderia_anyo")
    a = 2022
    print(f"La mejor escuderia en el anyo {a} ha sido {mejor_escuderia_anyo(datos, a)}")

if __name__ == "__main__":
    datos = lee_carreras("data/f1.csv")
    test_lee_carreras(datos)
    test_media_tiempo_boxes(datos)
    test_pilotos_menor_tiempo_medio_vueltas_top(datos)
    test_ratio_tiempo_boxes_total(datos)
    test_puntos_piloto_anyos(datos)
    test_mejor_escuderia_anyo(datos)