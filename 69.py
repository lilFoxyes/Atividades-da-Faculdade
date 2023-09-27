
import random


resultados = [random.randint(1, 6) for _ in range(16)]


contador_faces = [0, 0, 0, 0, 0, 0]


for resultado in resultados:
    contador_faces[resultado - 1] += 1


for i, contador in enumerate(contador_faces):
    print("A face {} saiu {} vezes.".format(i + 1, contador))