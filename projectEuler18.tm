init: q0
final: qf
q0 I B B B -> q0 I B B B R S S S
q0 a B B B -> q0 a B B B R S S S v q0 se premikamo do konca desno na prvem traku
q0 B B B B -> q1 B B B B L S S S 
q1 I B B B -> q2 B B B B L L S S 
q2 I B B B -> q3 B B B B L L S S
q3 a B B B -> q3 B a B B L L S S
q3 I B B B -> q4 B I B B L L S S
q4 a B B B -> q3 B a B B L L S S prepisujemo zadnji del na drugi trak
q4 I B B B -> q5 B I B B L L S S kocali smo z prepisovanjem na drugi trak
q5 a B B B -> q6 a B B B S R S S gremo v q6 kjer se na drugem traku pomaknemo do konca desno
q6 a a B B -> q6 a a B B S R S S
q6 a I B B -> q6 a I B B S R S S
q6 a B B B -> q7 a B B B S L S S koncali pomik do konca desno
q7 a a B B -> q7 a B a B S L R S prepisujemo zadnjo cifro na tretji trak
q7 a I B B -> q8 a B B B S L L S
q8 a a a B -> q8 B a a a L S S L prepisemo iz prvega traka cifro na zadni
q8 I a a B -> q8 I a B a S L L L prepisemo vecjo od spodnih dveh cifer zravn tiste na zgornem traku
q8 I a B B -> q8 I a B a S L S L
q8 I I a B -> q8 I I B a S S L L
q8 I I B B -> q9 I I B I S R S L
q9 I a B B -> q9 I a B B S R S S
q9 I B B B -> q7 B B B B L L S S
q7 I a B B -> q10 I B B B S L S S 
q10 I a B B -> q10 I B B B S L S S
q10 I I B B -> q10 I B B B S L S S
q10 I B B B -> q11 I B B B R S S R
q11 B B B I -> q11 I B B B R S S R
q11 B B B a -> q11 a B B B R S S R
q11 B B B B -> q12 I B B B R S S S
q12 B B B B -> q13 I B B B L S S S v q13 bomo preverili ce smo na koncu .. ali pa ce se vrnemo v q1
q13 I B B B -> q14 I B B B L S S S
q14 a B B B -> q14 a B B B L S S S
q14 I B B B -> q15 I B B B L S S S
q15 I B B B -> qf I B B B L S S S
q15 a B B B -> q0 a B B B S S S S
