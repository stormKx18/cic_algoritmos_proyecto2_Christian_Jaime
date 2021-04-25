# Proyecto 2 - Algoritmos BFS y DFS

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

**INSTITUTO POLITÉCNICO NACIONAL**

**Centro de Investigación en Computación**

**PRESENTA** Victor Christian Jaime Tamayo

**BOLETA** A210232

**ASIGNATURA** Diseño y Análisis de Algoritmos

**PROFESOR** Dr. Rolando Quintero Téllez

**SEMESTRE** A21

**FECHA** 25 de abril de 2021

---

## Instrucciones

Utilizando la biblioteca de grafos desarrollada en el proyecto 1, implementar los algoritmos BFS y DFS (recursivo e iterativo) de tal forma que dado un nodo fuente (s), calculen el árbol inducido por los algoritmos mencionados; es decir, desarrollar los métodos en la clase Grafo:
- def BFS(self, s):
- def DFS_R(self, s):
- def DFS_I(self, s):

Entregables:
1. Repositorio GIT (distinto al del primer proyecto)
2. Archivos de grafos generados. Tres por cada generador (con **30**, **100** y **500** nodos).
3. Archivos de grafos calculados. Tres por cada grafo generado (un **BFS** y dos **DFS**).
4. Imágenes de la visualización de cada grafo (generados y calculados).

---

## Resultados

- **Archivos GV generados:** [graphviz](/graphviz)

- **Código fuente:** [src](/src)

- **Imágenes:** [img](/img)

- Se utilizó el siguiente script para generar todos los grafos de este proyecto: [ejemplos.py](/src/ejemplos.py)

---

## Modelo Gm,n de malla
- m: número de columnas 
- n: número de filas
- dirigido: el grafo es dirigido

##

### 30 nodos
**m = 6, n = 5, dirigido = False**

<img src="/img/grafoMalla_m_6_n_5.png" width="500" />

> 30 Nodos y 49 Aristas

##

### 30 nodos - BFS
**m = 6, n = 5, dirigido = False**

<img src="/img/grafoMalla_m_6_n_5_BFS_7.png" width="500" />

> 30 Nodos y 29 Aristas

##

### 30 nodos - DFS recursivo
**m = 6, n = 5, dirigido = False**

<img src="/img/grafoMalla_m_6_n_5_DFS_R_7.png" width="500" />

> 30 Nodos y 29 Aristas

##

### 30 nodos - DFS iterativo
**m = 6, n = 5, dirigido = False**

<img src="/img/grafoMalla_m_6_n_5_DFS_I_7.png" width="500" />

> 30 Nodos y 29 Aristas

##

### 100 nodos
**m = 25, n = 4, dirigido = False**

<img src="/img/grafoMalla_m_25_n_4.png" width="500" />

> 100 Nodos y 171 Aristas
 
##

### 100 nodos - BFS
**m = 25, n = 4, dirigido = False**

<img src="/img/grafoMalla_m_25_n_4_BFS_7.png" width="500" />

> 100 Nodos y 99 Aristas
 
##

### 100 nodos- DFS recursivo
**m = 25, n = 4, dirigido = False**

<img src="/img/grafoMalla_m_25_n_4_DFS_R_7.png" width="500" />

> 100 Nodos y 99 Aristas
 
##

### 100 nodos - DFS iterativo
**m = 25, n = 4, dirigido = False**

<img src="/img/grafoMalla_m_25_n_4_DFS_I_7.png" width="500" />

> 100 Nodos y 99 Aristas
 
##

### 500 nodos
**m = 50, n = 10, dirigido = False**

<img src="/img/grafoMalla_m_50_n_10.png" width="500" />

> 500 Nodos y 940 Aristas
 
##

### 500 nodos - BFS
**m = 50, n = 10, dirigido = False**

<img src="/img/grafoMalla_m_50_n_10_BFS_7.png" width="500" />

> 500 Nodos y 499 Aristas
 
##

### 500 nodos - DFS recursivo
**m = 50, n = 10, dirigido = False**

<img src="/img/grafoMalla_m_50_n_10_DFS_R_7.png" width="500" />

> 500 Nodos y 499 Aristas
 
##

### 500 nodos - DFS iterativo
**m = 50, n = 10, dirigido = False**

<img src="/img/grafoMalla_m_50_n_10_DFS_I_7.png" width="500" />

> 500 Nodos y 499 Aristas
  
---

## Modelo Gn,m de Erdös y Rényi
- n: número de nodos (> 0)
- m: número de aristas (>= n-1)
- dirigido: el grafo es dirigido?
- auto: permitir auto-ciclos?

##

### 30 nodos
**n = 30, m = 30, dirigido = False, auto=False**

<img src="/img/grafoErdosRenyi_n_30_m_30.png" width="500" />

> 30 Nodos y 30 Aristas

##

### 30 nodos - BFS
**n = 30, m = 30, dirigido = False, auto=False**

<img src="/img/grafoErdosRenyi_n_30_m_30_BFS_7.png" width="500" />

> 24 Nodos y 23 Aristas

##

### 30 nodos - DFS recursivo
**n = 30, m = 30, dirigido = False, auto=False**

<img src="/img/grafoErdosRenyi_n_30_m_30_DFS_R_7.png" width="500" />

> 24 Nodos y 23 Aristas

##

### 30 nodos - DFS iterativo
**n = 30, m = 30, dirigido = False, auto=False**

<img src="/img/grafoErdosRenyi_n_30_m_30_DFS_I_7.png" width="500" />

> 24 Nodos y 23 Aristas

##

### 100 nodos
**n = 100, m = 100, dirigido = False, auto=False**

<img src="/img/grafoErdosRenyi_n_100_m_100.png" width="500" />

> 100 Nodos y 100 Aristas

##

### 100 nodos - BFS
**n = 100, m = 100, dirigido = False, auto=False**

<img src="/img/grafoErdosRenyi_n_100_m_100_BFS_7.png" width="500" />

> 87 Nodos y 86 Aristas

##

### 100 nodos - DFS recursivo
**n = 100, m = 100, dirigido = False, auto=False**

<img src="/img/grafoErdosRenyi_n_100_m_100_DFS_R_7.png" width="500" />

> 87 Nodos y 86 Aristas

##

### 100 nodos - DFS iterativo
**n = 100, m = 100, dirigido = False, auto=False**

<img src="/img/grafoErdosRenyi_n_100_m_100_DFS_I_7.png" width="500" />

> 87 Nodos y 86 Aristas

##

### 500 nodos
**n = 500, m = 500, dirigido = False, auto=False**

<img src="/img/grafoErdosRenyi_n_500_m_500.png" width="500" />

> 500 Nodos y 500 Aristas
 
##

### 500 nodos - BFS
**n = 500, m = 500, dirigido = False, auto=False**

<img src="/img/grafoErdosRenyi_n_500_m_500_BFS_7.png" width="500" />

> 392 Nodos y 391 Aristas
 
##

### 500 nodos - DFS recursivo
**n = 500, m = 500, dirigido = False, auto=False**

<img src="/img/grafoErdosRenyi_n_500_m_500_DFS_R_7.png" width="500" />

> 392 Nodos y 391 Aristas
 
##

### 500 nodos - DFS iterativo
**n = 500, m = 500, dirigido = False, auto=False**

<img src="/img/grafoErdosRenyi_n_500_m_500_DFS_I_7.png" width="500" />

> 392 Nodos y 391 Aristas
 
---

## Modelo Gn,p de **Gilbert**
- n: número de nodos (> 0)
- p: probabilidad de crear una arista (0, 1)
- dirigido: el grafo es dirigido?
- auto: permitir auto-ciclos?

##

### 30 nodos
**n = 30, p = 0.1, dirigido = False, auto=False**

<img src="/img/grafoGilbert_n_30_p_10.png" width="500" />

> 30 Nodos y 81 Aristas

##

### 30 nodos - BFS
**n = 30, p = 0.1, dirigido = False, auto=False**

<img src="/img/grafoGilbert_n_30_p_10_BFS_7.png" width="500" />

> 30 Nodos y 29 Aristas

##


### 30 nodos - DFS recursivo
**n = 30, p = 0.1, dirigido = False, auto=False**

<img src="/img/grafoGilbert_n_30_p_10_DFS_R_7.png" width="500" />

> 30 Nodos y 29 Aristas

##


### 30 nodos - DFS iterativo
**n = 30, p = 0.1, dirigido = False, auto=False**

<img src="/img/grafoGilbert_n_30_p_10_DFS_I_7.png" width="500" />

> 30 Nodos y 29 Aristas

##

### 100 nodos
**n = 100, p = 0.1, dirigido = False, auto=False**

<img src="/img/grafoGilbert_n_100_p_10.png" width="500" />

> 100 Nodos y 889 Aristas

##

### 100 nodos - BFS
**n = 100, p = 0.1, dirigido = False, auto=False**

<img src="/img/grafoGilbert_n_100_p_10_BFS_7.png" width="500" />

> 100 Nodos y 99 Aristas

##

### 100 nodos - DFS recursivo
**n = 100, p = 0.1, dirigido = False, auto=False**

<img src="/img/grafoGilbert_n_100_p_10_DFS_R_7.png" width="500" />

> 100 Nodos y 99 Aristas

##

### 100 nodos - DFS iterativo
**n = 100, p = 0.1, dirigido = False, auto=False**

<img src="/img/grafoGilbert_n_100_p_10_DFS_I_7.png" width="500" />

> 100 Nodos y 99 Aristas

##

### 500 nodos
**n = 500, p = 0.03, dirigido = False, auto=False**

<img src="/img/grafoGilbert_n_500_p_3.png" width="500" />

> 500 Nodos y 7,464 Aristas

##

### 500 nodos - BFS
**n = 500, p = 0.03, dirigido = False, auto=False**

<img src="/img/grafoGilbert_n_500_p_3_BFS_7.png" width="500" />

> 500 Nodos y 499 Aristas

##

### 500 nodos - DFS recursivo
**n = 500, p = 0.03, dirigido = False, auto=False**

<img src="/img/grafoGilbert_n_500_p_3_DFS_R_7.png" width="500" />

> 500 Nodos y 499 Aristas

##

### 500 nodos - DFS iterativo
**n = 500, p = 0.03, dirigido = False, auto=False**

<img src="/img/grafoGilbert_n_500_p_3_DFS_I_7.png" width="500" />

> 500 Nodos y 499 Aristas

##
---

## Modelo Gn,r **geográfico simple**
- n: número de nodos (> 0)
- r: distancia máxima para crear un nodo (0, 1)
- dirigido: el grafo es dirigido?
- auto: permitir auto-ciclos?

##

### 30 nodos
**n = 30, r = 0.3, dirigido = False, auto=False**

<img src="/img/grafoGeografico_n_30_r_3.png" width="500" />

> 30 Nodos y 104 Aristas

##

### 100 nodos
**n = 100, r = 0.3, dirigido = False, auto=False**

<img src="/img/grafoGeografico_n_100_r_3.png" width="500" />

> 100 Nodos y 1086 Aristas

##

### 500 nodos
**n = 500, r = 0.1, dirigido = False, auto=False**

<img src="/img/grafoGeografico_n_500_r_1.png" width="500" />

> 500 Nodos y 3,768 Aristas

---

## Variante del modelo Gn,d **Barabási-Albert**
- n: número de nodos (> 0)
- d: grado máximo esperado por cada nodo (> 1)
- dirigido: el grafo es dirigido?
- auto: permitir auto-ciclos?

##

### 30 nodos
**n = 30, d = 4, dirigido = False, auto=False**

<img src="/img/grafoBarabasiAlbert_n_30_d_4.png" width="500" />

> 30 Nodos y 58 Aristas

##

### 100 nodos
**n = 100, d = 4, dirigido = False, auto=False**

<img src="/img/grafoBarabasiAlbert_n_100_d_4.png" width="500" />

> 100 Nodos y 198 Aristas

##

### 500 nodos
**n =500, d = 4, dirigido = False, auto=False**

<img src="/img/grafoBarabasiAlbert_n_500_d_4.png" width="500" />

> 500 Nodos y 999 Aristas

---

## Modelo Gn **Dorogovtsev-Mendes**
- n: número de nodos (≥ 3)
- dirigido: el grafo es dirigido?

##

### 30 nodos
**n = 30, dirigido = False**

<img src="/img/grafoDorogovtsevMendes_n_30.png" width="500" />

> 30 Nodos y 57 Aristas

##

### 100 nodos
**n = 100, dirigido = False**

<img src="/img/grafoDorogovtsevMendes_n_100.png" width="500" />

> 100 Nodos y 197 Aristas

##

### 500 nodos
**n = 500, dirigido = False**

<img src="/img/grafoDorogovtsevMendes_n_500.png" width="500" />

> 500 Nodos y 997 Aristas

---

