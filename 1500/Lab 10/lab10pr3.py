"""Marc Ojalvo and Daniel Licht
CMPS 1500
Thursday 3:30-4:45
Lab 10 Part 3
04/26/2018"""

def isClique(G,X,k):
    """ finds if the given vertices are a clique
        Args:
            G (dic): a graph
            X (list): a list of vertices being tested
            k (int): number of vertices in the clique
        Returns:
            bool: True if is clique, False if not.
    """
    count = 0
    if G == {}:
        return False 
    if len(X) == k:
            for i in X:
                for j in X:
                    if i != j:
                        if not (i in G[j] and j in G[i]):
                            return False
            return True
    return False

"""THE RUNNING TIME OF THE ALGORITHM IS O(N^2). THIS IMPLIES THAT
THIS PROBLEMIS AN NP PROBLEM BECAUSE IT IS CHECKABLE IN POLYNOMIAL
TIME, BUT NOT SOLVABLEIN POLYNOMIAL TIME. IT IS NP BECAUSE THE
ONLY WAY TO FIND A CLIQUEIS TO CHECK EACH VERTEX AND ITS EDGES."""
