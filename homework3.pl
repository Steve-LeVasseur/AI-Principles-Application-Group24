% Student exercise profile
:- set_prolog_flag(occurs_check, error).        % disallow cyclic terms
:- set_prolog_stack(global, limit(8 000 000)).  % limit term space (8Mb)
:- set_prolog_stack(local,  limit(2 000 000)).  % limit environment space
:- dynamic list/1. % Used to create a list
:- randomList(10, L), assertz(list(L)).

% Implementation of randomList
randomList(0, []).
randomList(N, LIST):-
    N > 0,
    random(0,100,X),
    LIST = [X|T],
    Y is N - 1,
    randomList(Y, T).

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

/*Comment describing insert(E, SL, SLE) ...
 * Given inputs element E and ordered short list SL, insert E into short list L in the ordered position
 */

/*Comment describing the 1st clause of insert ...
 * If X is being inserted into an empty list, return a list containing only X if E is smaller  
 */

lessThanOrEqual(A, B):-
    A =< B.

insert(X, [],[X]). 
insert(E, [H|T], [E,H|T]):- 
    ordered(T),
    lessThanOrEqual(E, H),
    !. 

/*Comment describing the 2nd clause of insert ...
 * If The tail of the list is ordered, insert E into T then append the head to the new tail (T1) and return it.
 */

insert(E, [H|T], [H|T1]):- 
    ordered(T),
    insert(E, T, T1). 

/*
 * Test query insertionSort([301, 24, 345, 65, 6, 789, 2, 23, 2, 12, 346, 86, 45, 90, 23, 56], X)
 * insertionSort sorts a list by incrementally removing the leftmost element and re-inserting it so that all elements to it's left are smaller than it.
 */
insertionSort([], []). 
insertionSort([H|T], SORTED) :- 
    insertionSort(T, T1), 
    insert(H, T1, SORTED).

/* 
Splits input list then calls mergeSort on both split lists
Once splits are finished, they are remerged in sorted order
 */
mergeSort([], []).    %the empty list is sorted 
mergeSort([X], [X]):-!.
mergeSort(L, SL):- 
	split_in_half(L, L1, L2), 
	mergeSort(L1, S1), 
    mergeSort(L2, S2),
    merge(S1, S2, SL).

/* 
Uses the length of the list to calculate the index of the halfway point
then splits the list on that index and outputs the two halves
*/
intDiv(N,N1, R):- R is div(N,N1).
split_in_half([], _, _):-!, fail.
split_in_half([X],[],[X]).
split_in_half(L, L1, L2):- 
	length(L,N), 
    intDiv(N,2,N1),
    length(L1, N1), 
    append(L1, L2, L).

/*
Merges a smaller list and a larger list, placing the smaller list to the left
*/
merge([], L, L). 
merge(L, [],L).   
merge([H1|T1],[H2|T2],[H1| T]):-
	H1 < H2,
	merge(T1,[H2|T2],T).

merge([H1|T1], [H2|T2], [H2|T]):-
	H2 =< H1,
	merge([H1|T1], T2, T).
   
/*
Splits input lists for quickSort algorithm
*/
split(_, [],[],[]). 
	split(X, [H|T], [H|SMALL], BIG):- 
	H =< X, 
    split(X, T, SMALL, BIG).    
 split(X, [H|T], SMALL, [H|BIG]):-
    X =< H,
    split(X, T, SMALL, BIG). 
/* 
Splits input list then calls quickSort on both split lists
Once splits are finished, they are recombined in sorted order
*/
quickSort([], []).
quickSort([H|T], LS):-
        split(H, T, SMALL, BIG), 
        quickSort(SMALL, S), 
        quickSort(BIG, B), 
        append(S, [H|B], LS). 


/* 
If the input list is smaller in length than the input threshold,
the SMALL sorting algorithm is called, either bubbleSort or insertionSort.
If the input list is larger in length than the input threshold,
hybridSort acts like the sorting algorithm declared as BIGALG,
either mergeSort or quickSort
 */
hybridSort(LIST, bubbleSort, BIGALG, T, SLIST):- % bubbleSort and any big algorithm
length(LIST, N), N=<T,      
      bubbleSort(LIST, SLIST).
hybridSort(LIST, insertionSort, BIGALG, T, SLIST):- % insertionSort and any big algorithm
length(LIST, N), N=<T,
      insertionSort(LIST, SLIST).
hybridSort(LIST, SMALL, mergeSort, T, SLIST):- % mergeSort and any small algorithm
length(LIST, N), N>T,      
split_in_half(LIST, L1, L2),
    hybridSort(L1, SMALL, mergeSort, T, S1),
    hybridSort(L2, SMALL, mergeSort, T, S2),
    merge(S1,S2, SLIST).
hybridSort([H|T], SMALL, quickSort, Thresh, SLIST):- % quickSort and any small algorithm
	length([H|T], N), N>Thresh,      
	split(H, T, L1, L2),
    hybridSort(L1, SMALL, quickSort, Thresh, S1),
    hybridSort(L2, SMALL, quickSort, Thresh, S2),
    append(S1, [H|S2], SLIST).

