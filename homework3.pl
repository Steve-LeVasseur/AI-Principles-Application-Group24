% Student exercise profile
:- set_prolog_flag(occurs_check, error).        % disallow cyclic terms
:- set_prolog_stack(global, limit(8 000 000)).  % limit term space (8Mb)
:- set_prolog_stack(local,  limit(2 000 000)).  % limit environment space

/*swap the first two elements if they are not in order*/
 swap([X, Y|T], [Y, X | T]):- 
 	Y =< X. 

/*swap elements in the tail*/
 swap([H|T], [H|T1]):-
 	swap(T, T1). 

/*  BUBBLESORT -  
    The predicate calls the swap() predicate on the input list L, 
    the swap() predicate will swap the first 2 elements in the array if they are not in order, then recursively call the swap() predicate on the elements in the tail T
    one call of the swap from the bubbleSort level will run 1 pass of sorting all of the elements.
    bubbleSort then calls itself on the list that has been sorted once.
*/
bubbleSort(L,SL):- 
	swap(L, L1), % at least one swap is needed 
    !, 
    bubbleSort(L1, SL). 
bubbleSort(L, L). % here, the list is already sorted

/*  ORDERED - 
    In the cases of an empty or single element list: return true.
    In the case of a list of 2 or more elements, check if the first element in the list is less than or equal to the second element. 
        Then, call the ordered predicate on the list containing the second element and the tail
    If in any single recursive state, the first element is not less than or equal to the second element, the entire predicate will return false. Otherwise true.
*/
ordered([]).
ordered([_X]).
ordered([H1, H2|T]):-
    H1 =< H2, 
    ordered([H2|T]).

/*Comment describing insert(E, SL, SLE) ...*/

/*Comment describing the 1st clause of insert ...*/

insert(X, [],[X]). 
insert(E, [H|T], [E,H|T]):- 
	ordered(T),
	ordered([E, H]),  %  <<< SHOT IN THE DARK, NEEDS TO BE TESTED >>>
    !. 

/*Comment describing the 2nd clause of insert ...*/

insert(E, [H|T], [H|T1]):- 
	ordered(T),
    insert(E, T, FILLINHERE). 

/* Comment describing insertionSort */
insertionSort([], []). 
insertionSort([H|T], SORTED) :- 
	insertionSort(T, T1), 
    insert(H, T1, FILLINHERE).

/* Comment to describe mergeSort... */
mergeSort([], []).    %the empty list is sorted 
mergeSort([X], [X]):-!.
mergeSort(L, SL):- 
	split_in_half(L, L1, L2), 
	mergeSort(L1, FILLINHERE), 
    mergeSort(L2, S2),
    merge(S1, FILLINHERE, SL).

/* Comment to describe split_in_half...*/
intDiv(N,N1, R):- R is div(N,N1).
split_in_half([], _, _):-!, fail.
split_in_half([X],[],[X]).
split_in_half(L, L1, L2):- 
	length(L,N), 
    intDiv(N,2,N1),
    length(L1, FILLINHERE), 
    append(L1, L2, L).

/* Comment describing merge(S1, S2, S) */
merge([], L, L). % comment
merge(L, [],L).  % comment 
merge([H1|T1],[H2|T2],[H1| FILLINHERE]):-
	H1 FILLINHERE  H2,
	merge(T1,[H2|T2],T).

merge([H1|T1], [H2|T2], [H2|T]):-
	H2 =< H1, % << EDITED IN FROM LECTURE; NEEDS TESTING INCASE PROF IS WRONG ??? >>
	merge([H1|T1], T2, FILLINHERE).
   
/* Comment describing split for quickSort */
split(_, [],[],[]). 
	split(X, [H|T], [H|SMALL], BIG):- 
	H =< X, 
    split(X, T, SMALL, BIG).    
 split(X, [H|T], SMALL, [H|BIG]):-
    X =< H,
    split(X, T, SMALL, BIG). 
/* Comment describing quickSort */
quickSort([], []).
quickSort([H|T], LS):-
        split(H, T, SMALL, BIG), 
        quickSort(SMALL, S), 
        quickSort(BIG, B), 
        append(S, [H|B], LS). 


/* Comment describing hybridSort */
hybridSort(LIST, bubbleSort, BIGALG, T, SLIST):-
length(LIST, N), N=<T,      
      bubbleSort(LIST, FILLINHERE).
hybridSort(LIST, insertionSort, BIGALG, T, SLIST):-
length(LIST, N), N=<T,
      insertionSort(LIST, SLIST).
hybridSort(LIST, SMALL, mergeSort, T, SLIST):-
length(LIST, N), N>T,      
split_in_half(LIST, L1, L2),
    hybridSort(L1, SMALL, mergeSort, T, S1),
    hybridSort(L2, SMALL, mergeSort, T, S2),
    merge(S1,S2, SLIST).
hybridSort([H|T], SMALL, quickSort, T, SLIST):-
length(LIST, N), N>T,      
split(H, T, L1, L2),
    FILLINHERE several lines in the body of this clause
    append(S1, [H|S2], SLIST).
hybridSort([H|T], SMALL, quickSort, T, SLIST):-
FILLINHERE the full body of this clause