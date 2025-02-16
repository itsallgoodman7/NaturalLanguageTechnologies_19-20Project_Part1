from numpy.lib.function_base import append
from node import Node
import pandas as p
import numpy as np
from getGrammar import *

#frasi di esempio da parsificare (con grammatica L1 o Dothraki)
e1 = ['book','the','flight','through','Houston'] # l1
e2 = ['does', 'she', 'prefer', 'a', 'morning', 'flight'] #l1
e3 = ['anha', 'zhilak', 'yera'] #I love you #dothraki
e4 = ['hash', 'yer', 'astoe', 'ki', 'Dothraki'] #Do you speak Dothraki? #dothraki
e5 = ['anha','gavork'] #I'm hungry #dothraki (0-copula, 2 NP di seguito)

def parser_gs(grammar,sentence): #metodo richiamato nel main

    syntax_tree,cky_matrix = CKY(grammar,sentence)
    print_CKY_Matrix(cky_matrix)
    print_Tree_Nodes(syntax_tree)

#implementazione algoritmo CKY
def CKY(R,s):
    #cky_matrix matrice del cky (diagonale T, sopra NT)
    #tree_nodes matrice di copia per tener traccia dei sottoalberi collegati della cky_matrix
    n = len(s) # LENGHT(words)
    cky_matrix = [[[] for j in range(n + 1)] for i in range(n + 1)]
    tree_nodes = [[[] for i in range(n + 1)] for j in range(n + 1)]

    for j in range(1, len(s)+1): # scorro sulla diagonale (range da 1 a n, cioè scorro su tutte le parole del parametro s)
            
        for left, rule in R.items(): # Itera su tutte le regole della grammatica passata (parametro R)
            # left chiavi, rule lista valori a destra delle regole
            # right la singola parola della lista
            for right in rule: # ciclo sulla lista dei right (conseguenti/produzioni delle regole)
                #nella diagonale inserisci tutti i termini sinistri delle regole interessanti:
                # A (NT) -> alpha (T)
                #cerco regole terminali (= che hanno un solo termine destro, data una grammatica in Chomsky Normal Form) 
                if len(right) == 1 and right[0] == s[j - 1]:  # regole terminali il cui termine destro è uguale al terminale target                                             ## { A -> words[j] in grammar}
                    cky_matrix[j - 1][j].append(left) # inserisco il left (l'antecedente della regola trovata) nella matrice                                                              ## {cky_matrix[j - 1, j] = A}
                    tree_nodes[j - 1][j].append(Node(left, None, None, s[j - 1]))
                    # inserisco nella matrice tree_nodes il Nodo con radice left e sottoalberi sinistro e destro None,
                    # in quanto le regole non sono di lunghezza 2 essendo in un terminale
                    # l'ultimo parametro contiene l'informazione (il terminale vero e proprio) 
                   
        for i in reversed(range(0, j - 1)):                
            for k in range(i + 1, j):      
                # left chiavi
                # rule lista valori a destra delle regole)
                # right la singola parola della lista

                #cerco regole non terminali : A (NT) -> B (NT) C (NT)
                for left, rule in R.items(): 
                    for right in rule: 
                                # {A | A -> BC, B in cky_matrix[i,k], C in cky_matrix [k,j]}
                                if len(right) == 2 and right[0] in cky_matrix[i][k] and right[1] in cky_matrix[k][j]:        
                                    cky_matrix[i][j].append(left) # inseriamo il termine left (A) della regola non terminale trovata in posizione ij della matrice

                                #riempiamo la tabella che tiene traccia della struttura sintattica dell'albero
                                #ogni casella contiene i sottoalberi (nodi) della matrice CKY risultante
                                    # controlliamo analogamente nella matrice tree_nodes l'esistenza dei 2 sottoalberi B e C 
                                    # (nodi con radici i due termini NT trovati)
                                    # se esistono aggiungiamo come fatto per la cky_matrix un nuovo
                                    # Node (con root il NT A e come sottoalberi figli left e right i due NT B e C)
                                    for b in tree_nodes[i][k]: # ho dei nodi (sottoalberi) -> controllo tutti i sottoalberi in B e in C
                                        for c in tree_nodes[k][j]:
                                            if b.root == right[0] and c.root == right[1]:
                                                tree_nodes[i][j].append(Node(left, b, c, None))

    #ritorno la matrice dei nodi [0][n] perché corrisponde all'albero completo, 
    #(con il nodo S che tiene traccia di A B C, i quali avranno i vari sottoalberi collegati)                  
    return tree_nodes[0][n], cky_matrix 
    # restituiamo le radici di tutti i vari alberi risultanti (dalla radice ritrovo i collegamenti a tutti i sottoalberi)
    # e
    # l'intera matrice del CKY costruita

def print_CKY_Matrix(result):  # stampa matrice CKY tramite dataframe, controllando se la frase è valida
    n = len(result[0])-1
    if len(result[0][n]) != 0:
        if result[0][n].__contains__('S'): # controllo se nell'elemento in alto a destra della matrice CKY è presente 'S' (= frase valida)
            print(f"\n| Valid sentence |\n\n")
            #stampa dataframe risultante con frase valida
            a = np.array(result, dtype=object)
            df = p.DataFrame(a[:-1,1:],columns=list(range(1,n+1)))
            print(df)
    else: 
        print(f"\n| Invalid sentence |\n\n")


def print_Tree_Nodes(nodes_back):
	for node in nodes_back:
		if node.root == 'S':
			print(build_String_Tree(node, 3))
    # controlla che la radice sia S, in tal caso stampa il nodo relativo
    # chiamando il metodo di print dell'albero (build_String_Tree)

def build_String_Tree(root, indent):
	"""
	build_String_Tree() takes a root and constructs the tree in the form of a
	string (in form of S-expression). 
	"""
	if root.status: # stato terminale (caso base ricorsione)
		return '(' + root.root + ' ' + root.terminal + ')'

    # caso di nodo non terminale (su cui fare ricorsione)
	# Calcolo i fattori di indentazione per la stampa ricorsiva dei nodi figli left e right.
	new1 = indent + 2 + len(root.left.root) 
	new2 = indent + 2 + len(root.right.root)
	left = build_String_Tree(root.left, new1) # ricorsione sul nodo figlio left
	right = build_String_Tree(root.right, new2) # ricorsione sul nodo figlio right
	return '(' + root.root + ' ' + left + '\n' \
			+ ' '*indent + right + ')'
    # stampo una S-espressione con tutte le produzioni dei sottoalberi del tipo: root -> left right

if __name__ == '__main__':
    parser_gs(L1,e1) #l1
    #parser_gs(Dothraki, e3) #dothraki

