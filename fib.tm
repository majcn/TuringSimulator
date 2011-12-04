init: q0
final: q11 q12 q13
q0 a B B -> q0 a a B R R S
q0 a B B -> q1 a B B S S S
q1 a B B -> q1 a B a R S R
q1 B B B -> q2 B B B S L L
q2 B B a -> q10 B B a S S L
q2 B a a -> q3 B a a S L L
q3 B a a -> q3 B a a S L L
q3 B a B -> q3 B a B S L S
q3 B B a -> q3 B B a S S L
q3 B B B -> q4 B B B S R R 
q4 B a a -> q5 B a a S R R 
q5 B B B -> q12 B B B S S S
q5 B a a -> q6 B a a S L L
q5 B B a -> q6 B B a S L L
q5 B a B -> q6 B a B S L L
q6 B a a -> q7 B B a S R R
q7 B a a -> q7 B B a S R R
q7 B a B -> q31 B a B S S L
q31 B a a -> q31 B a a S L L
q31 B a B -> q31 B a B S L S
q31 B B a -> q31 B B a S S L
q31 B B B -> q41 B B B S R R 
q41 B a a -> q51 B a a S R R 
q51 B B B -> q13 B B B S S S
q51 B a a -> q61 B a a S L L
q51 B B a -> q61 B B a S L L
q51 B a B -> q61 B a B S L L
q61 B a a -> q8 B a B S R R
q8 B a a -> q8 B a B S R R
q8 B B a -> q3 B B a S L S
q10 B B B -> q11 B B B S S S


