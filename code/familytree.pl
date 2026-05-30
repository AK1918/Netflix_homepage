parent(a,b).
parent(b,c).
parent(c,d).

grandparent(X,Y):-
    parent(X,Z),
    parent(Z,Y).