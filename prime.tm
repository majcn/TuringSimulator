init: q0
final: qF
q0 a B -> q1 a B R S
q1 a B -> q2 a a L R
q2 a B -> q3 a a S S
q3 a a -> q3 a a S L
q3 a B -> q4 a B S R
q4 a a -> q4 a a R R
q4 a B -> q3 a B S L
q4 B a -> q5 B a L S
q5 a a -> q5 a a L S
q5 B a -> q6 B a R R
q6 a a -> q6 a a S R
q6 a B -> q3 a a S L
q4 B B -> q7 B B L L
q7 a a -> q7 a a L L
q7 B B -> qF B B S S
