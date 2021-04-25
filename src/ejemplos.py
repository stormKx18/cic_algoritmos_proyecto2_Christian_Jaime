import datetime
x = datetime.datetime.now()
print(x)
#******************************************************************************
nodo_raiz=7
print('nodo_raiz: ',nodo_raiz)
#******************************************************************************
from grafoMalla import grafoMalla
#******************************************************************************
#grafoMalla - 30 nodos
gfMalla = grafoMalla(6,5,dirigido=False)
gfMalla.display()
gfMalla.graphviz()
gfMalla_BFS=gfMalla.BFS(nodo_raiz) #BFS
gfMalla_BFS.display()
gfMalla_BFS.graphviz()
gfMalla_DFS_R=gfMalla.DFS_R(nodo_raiz) #DFS recursivo
gfMalla_DFS_R.display()
gfMalla_DFS_R.graphviz()
gfMalla_DFS_I=gfMalla.DFS_I(nodo_raiz) #DFS iterativo
gfMalla_DFS_I.display()
gfMalla_DFS_I.graphviz()

#grafoMalla - 100 nodos
gfMalla = grafoMalla(25,4,dirigido=False)
gfMalla.display()
gfMalla.graphviz()
gfMalla_BFS=gfMalla.BFS(nodo_raiz) #BFS
gfMalla_BFS.display()
gfMalla_BFS.graphviz()
gfMalla_DFS_R=gfMalla.DFS_R(nodo_raiz) #DFS recursivo
gfMalla_DFS_R.display()
gfMalla_DFS_R.graphviz()
gfMalla_DFS_I=gfMalla.DFS_I(nodo_raiz) #DFS iterativo
gfMalla_DFS_I.display()
gfMalla_DFS_I.graphviz()

#grafoMalla - 500 nodos
gfMalla = grafoMalla(50,10,dirigido=False)
gfMalla.display()
gfMalla.graphviz()
gfMalla_BFS=gfMalla.BFS(nodo_raiz) #BFS
gfMalla_BFS.display()
gfMalla_BFS.graphviz()
gfMalla_DFS_R=gfMalla.DFS_R(nodo_raiz) #DFS recursivo
gfMalla_DFS_R.display()
gfMalla_DFS_R.graphviz()
gfMalla_DFS_I=gfMalla.DFS_I(nodo_raiz) #DFS iterativo
gfMalla_DFS_I.display()
gfMalla_DFS_I.graphviz()
#******************************************************************************

from grafoErdosRenyi import grafoErdosRenyi
#******************************************************************************
#grafoErdosRenyi - 30 nodos
gfErdosReny = grafoErdosRenyi(n=30, m=30, dirigido=False, auto=False)
gfErdosReny.display()
gfErdosReny.graphviz()
gfErdosReny_BFS=gfErdosReny.BFS(nodo_raiz) #BFS
gfErdosReny_BFS.display()
gfErdosReny_BFS.graphviz()
gfErdosReny_DFS_R=gfErdosReny.DFS_R(nodo_raiz) #DFS recursivo
gfErdosReny_DFS_R.display()
gfErdosReny_DFS_R.graphviz()
gfErdosReny_DFS_I=gfErdosReny.DFS_I(nodo_raiz) #DFS iterativo
gfErdosReny_DFS_I.display()
gfErdosReny_DFS_I.graphviz()

#grafoErdosRenyi - 100 nodos
gfErdosReny = grafoErdosRenyi(n=100, m=100, dirigido=False, auto=False)
gfErdosReny.display()
gfErdosReny.graphviz()
gfErdosReny_BFS=gfErdosReny.BFS(nodo_raiz) #BFS
gfErdosReny_BFS.display()
gfErdosReny_BFS.graphviz()
gfErdosReny_DFS_R=gfErdosReny.DFS_R(nodo_raiz) #DFS recursivo
gfErdosReny_DFS_R.display()
gfErdosReny_DFS_R.graphviz()
gfErdosReny_DFS_I=gfErdosReny.DFS_I(nodo_raiz) #DFS iterativo
gfErdosReny_DFS_I.display()
gfErdosReny_DFS_I.graphviz()

#grafoErdosRenyi - 500 nodos
gfErdosReny = grafoErdosRenyi(n=500, m=500, dirigido=False, auto=False)
gfErdosReny.display()
gfErdosReny.graphviz()
gfErdosReny_BFS=gfErdosReny.BFS(nodo_raiz) #BFS
gfErdosReny_BFS.display()
gfErdosReny_BFS.graphviz()
gfErdosReny_DFS_R=gfErdosReny.DFS_R(nodo_raiz) #DFS recursivo
gfErdosReny_DFS_R.display()
gfErdosReny_DFS_R.graphviz()
gfErdosReny_DFS_I=gfErdosReny.DFS_I(nodo_raiz) #DFS iterativo
gfErdosReny_DFS_I.display()
gfErdosReny_DFS_I.graphviz()
#******************************************************************************


from grafoGilbert import grafoGilbert
#******************************************************************************
#grafoGilbert - 30 nodos
gfGilbert = grafoGilbert(n=30, p=0.1, dirigido=False, auto=False)
gfGilbert.display()
gfGilbert.graphviz()
gfGilbert_BFS=gfGilbert.BFS(nodo_raiz) #BFS
gfGilbert_BFS.display()
gfGilbert_BFS.graphviz()
gfGilbert_DFS_R=gfGilbert.DFS_R(nodo_raiz) #DFS recursivo
gfGilbert_DFS_R.display()
gfGilbert_DFS_R.graphviz()
gfGilbert_DFS_I=gfGilbert.DFS_I(nodo_raiz) #DFS iterativo
gfGilbert_DFS_I.display()
gfGilbert_DFS_I.graphviz()

#grafoGilbert - 100 nodos
gfGilbert = grafoGilbert(n=100, p=0.1, dirigido=False, auto=False)
gfGilbert.display()
gfGilbert.graphviz()
gfGilbert_BFS=gfGilbert.BFS(nodo_raiz) #BFS
gfGilbert_BFS.display()
gfGilbert_BFS.graphviz()
gfGilbert_DFS_R=gfGilbert.DFS_R(nodo_raiz) #DFS recursivo
gfGilbert_DFS_R.display()
gfGilbert_DFS_R.graphviz()
gfGilbert_DFS_I=gfGilbert.DFS_I(nodo_raiz) #DFS iterativo
gfGilbert_DFS_I.display()
gfGilbert_DFS_I.graphviz()


#grafoGilbert - 500 nodos
gfGilbert = grafoGilbert(n=500, p=0.03, dirigido=False, auto=False)
gfGilbert.display()
gfGilbert.graphviz()
gfGilbert_BFS=gfGilbert.BFS(nodo_raiz) #BFS
gfGilbert_BFS.display()
gfGilbert_BFS.graphviz()
gfGilbert_DFS_R=gfGilbert.DFS_R(nodo_raiz) #DFS recursivo
gfGilbert_DFS_R.display()
gfGilbert_DFS_R.graphviz()
gfGilbert_DFS_I=gfGilbert.DFS_I(nodo_raiz) #DFS iterativo
gfGilbert_DFS_I.display()
gfGilbert_DFS_I.graphviz()

#******************************************************************************

from grafoGeografico import grafoGeografico
#******************************************************************************
#grafoGeografico - 30 nodos
gfGeografico = grafoGeografico(n=30, r=0.3, dirigido=False, auto=False)
gfGeografico.display()
gfGeografico.graphviz()
gfGeografico_BFS=gfGeografico.BFS(nodo_raiz) #BFS
gfGeografico_BFS.display()
gfGeografico_BFS.graphviz()
gfGeografico_DFS_R=gfGeografico.DFS_R(nodo_raiz) #DFS recursivo
gfGeografico_DFS_R.display()
gfGeografico_DFS_R.graphviz()
gfGeografico_DFS_I=gfGeografico.DFS_I(nodo_raiz) #DFS iterativo
gfGeografico_DFS_I.display()
gfGeografico_DFS_I.graphviz()


#grafoGeografico - 100 nodos
gfGeografico = grafoGeografico(n=100, r=0.3, dirigido=False, auto=False)
gfGeografico.display()
gfGeografico.graphviz()
gfGeografico_BFS=gfGeografico.BFS(nodo_raiz) #BFS
gfGeografico_BFS.display()
gfGeografico_BFS.graphviz()
gfGeografico_DFS_R=gfGeografico.DFS_R(nodo_raiz) #DFS recursivo
gfGeografico_DFS_R.display()
gfGeografico_DFS_R.graphviz()
gfGeografico_DFS_I=gfGeografico.DFS_I(nodo_raiz) #DFS iterativo
gfGeografico_DFS_I.display()
gfGeografico_DFS_I.graphviz()

#grafoGeografico - 500 nodos
gfGeografico = grafoGeografico(n=500, r=0.1, dirigido=False, auto=False)
gfGeografico.display()
gfGeografico.graphviz()
gfGeografico_BFS=gfGeografico.BFS(nodo_raiz) #BFS
gfGeografico_BFS.display()
gfGeografico_BFS.graphviz()
gfGeografico_DFS_R=gfGeografico.DFS_R(nodo_raiz) #DFS recursivo
gfGeografico_DFS_R.display()
gfGeografico_DFS_R.graphviz()
gfGeografico_DFS_I=gfGeografico.DFS_I(nodo_raiz) #DFS iterativo
gfGeografico_DFS_I.display()
gfGeografico_DFS_I.graphviz()
#******************************************************************************

from grafoBarabasiAlbert import grafoBarabasiAlbert
#******************************************************************************
#grafoBarabasiAlbert - 30 nodos
gfBarabasiAlbert = grafoBarabasiAlbert(n=30, d=4, dirigido=False, auto=False)
gfBarabasiAlbert.display()
gfBarabasiAlbert.graphviz()
gfBarabasiAlbert_BFS=gfBarabasiAlbert.BFS(nodo_raiz) #BFS
gfBarabasiAlbert_BFS.display()
gfBarabasiAlbert_BFS.graphviz()
gfBarabasiAlbert_DFS_R=gfBarabasiAlbert.DFS_R(nodo_raiz) #DFS recursivo
gfBarabasiAlbert_DFS_R.display()
gfBarabasiAlbert_DFS_R.graphviz()
gfBarabasiAlbert_DFS_I=gfBarabasiAlbert.DFS_I(nodo_raiz) #DFS iterativo
gfBarabasiAlbert_DFS_I.display()
gfBarabasiAlbert_DFS_I.graphviz()

#grafoBarabasiAlbert - 100 nodos
gfBarabasiAlbert = grafoBarabasiAlbert(n=100, d=4, dirigido=False, auto=False)
gfBarabasiAlbert.display()
gfBarabasiAlbert.graphviz()
gfBarabasiAlbert_BFS=gfBarabasiAlbert.BFS(nodo_raiz) #BFS
gfBarabasiAlbert_BFS.display()
gfBarabasiAlbert_BFS.graphviz()
gfBarabasiAlbert_DFS_R=gfBarabasiAlbert.DFS_R(nodo_raiz) #DFS recursivo
gfBarabasiAlbert_DFS_R.display()
gfBarabasiAlbert_DFS_R.graphviz()
gfBarabasiAlbert_DFS_I=gfBarabasiAlbert.DFS_I(nodo_raiz) #DFS iterativo
gfBarabasiAlbert_DFS_I.display()
gfBarabasiAlbert_DFS_I.graphviz()

#grafoBarabasiAlbert - 500 nodos
gfBarabasiAlbert = grafoBarabasiAlbert(n=500, d=4, dirigido=False, auto=False)
gfBarabasiAlbert.display()
gfBarabasiAlbert.graphviz()
gfBarabasiAlbert_BFS=gfBarabasiAlbert.BFS(nodo_raiz) #BFS
gfBarabasiAlbert_BFS.display()
gfBarabasiAlbert_BFS.graphviz()
gfBarabasiAlbert_DFS_R=gfBarabasiAlbert.DFS_R(nodo_raiz) #DFS recursivo
gfBarabasiAlbert_DFS_R.display()
gfBarabasiAlbert_DFS_R.graphviz()
gfBarabasiAlbert_DFS_I=gfBarabasiAlbert.DFS_I(nodo_raiz) #DFS iterativo
gfBarabasiAlbert_DFS_I.display()
gfBarabasiAlbert_DFS_I.graphviz()
#******************************************************************************

from grafoDorogovtsevMendes import grafoDorogovtsevMendes
#******************************************************************************
#grafoBarabasiAlbert - 30 nodos
gfDorogovtsevMendes = grafoDorogovtsevMendes(30,dirigido=False)
gfDorogovtsevMendes.display()
gfDorogovtsevMendes.graphviz()
gfDorogovtsevMendes_BFS=gfDorogovtsevMendes.BFS(nodo_raiz) #BFS
gfDorogovtsevMendes_BFS.display()
gfDorogovtsevMendes_BFS.graphviz()
gfDorogovtsevMendes_DFS_R=gfDorogovtsevMendes.DFS_R(nodo_raiz) #DFS recursivo
gfDorogovtsevMendes_DFS_R.display()
gfDorogovtsevMendes_DFS_R.graphviz()
gfDorogovtsevMendes_DFS_I=gfDorogovtsevMendes.DFS_I(nodo_raiz) #DFS iterativo
gfDorogovtsevMendes_DFS_I.display()
gfDorogovtsevMendes_DFS_I.graphviz()

#grafoBarabasiAlbert - 100 nodos
gfDorogovtsevMendes = grafoDorogovtsevMendes(100,dirigido=False)
gfDorogovtsevMendes.display()
gfDorogovtsevMendes.graphviz()
gfDorogovtsevMendes_BFS=gfDorogovtsevMendes.BFS(nodo_raiz) #BFS
gfDorogovtsevMendes_BFS.display()
gfDorogovtsevMendes_BFS.graphviz()
gfDorogovtsevMendes_DFS_R=gfDorogovtsevMendes.DFS_R(nodo_raiz) #DFS recursivo
gfDorogovtsevMendes_DFS_R.display()
gfDorogovtsevMendes_DFS_R.graphviz()
gfDorogovtsevMendes_DFS_I=gfDorogovtsevMendes.DFS_I(nodo_raiz) #DFS iterativo
gfDorogovtsevMendes_DFS_I.display()
gfDorogovtsevMendes_DFS_I.graphviz()

#grafoBarabasiAlbert - 500 nodos
gfDorogovtsevMendes = grafoDorogovtsevMendes(500,dirigido=False)
gfDorogovtsevMendes.display()
gfDorogovtsevMendes.graphviz()
gfDorogovtsevMendes_BFS=gfDorogovtsevMendes.BFS(nodo_raiz) #BFS
gfDorogovtsevMendes_BFS.display()
gfDorogovtsevMendes_BFS.graphviz()
gfDorogovtsevMendes_DFS_R=gfDorogovtsevMendes.DFS_R(nodo_raiz) #DFS recursivo
gfDorogovtsevMendes_DFS_R.display()
gfDorogovtsevMendes_DFS_R.graphviz()
gfDorogovtsevMendes_DFS_I=gfDorogovtsevMendes.DFS_I(nodo_raiz) #DFS iterativo
gfDorogovtsevMendes_DFS_I.display()
gfDorogovtsevMendes_DFS_I.graphviz()
#******************************************************************************
