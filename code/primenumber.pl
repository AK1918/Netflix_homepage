is_prime(2).

is_prime(X) :-
    X > 2,
    X mod 2 =\= 0,
    not(has_factor(X,3)).

has_factor(X,F) :-
    X mod F =:= 0.

has_factor(X,F) :-
    F * F < X,
    F2 is F + 2,
    has_factor(X,F2).