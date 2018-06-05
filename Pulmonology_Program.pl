notice:-
write('This is an Example of an Expert System for Diagnosing some Lung Diseases'),nl,

nl,
write('To use it, just answer the quizes the systems asks you.'),nl,
nl.


%hypothesises

disease(tuberculosis):-
						symptom(persistent_cough),
						symptom(constant_fatigue),
						symptom(weight_loss),
						symptom(lack_of_appetite),
						symptom(fever),
						symptom( coughing_blood),
						symptom( night_sweats).
								
disease(pneumonia):-
						symptom( cough),
						symptom( fever),
						symptom( shaking_chills),
						symptom( shortness_of_breath).
							
disease(byssinosis):-
						symptom( chest_tightness),
						symptom( cough),
						symptom( wheezing).
						
disease(pertusis):-
						symptom( runny_nose),
						symptom( mild_fever).
						
disease(pneumoconiosis):-
						symptom(chronic_cough),
						symptom(shortness_of_breath).
						
disease(sarcoidosis):-
						symptom( dry_cough),
						symptom( shortness_of_breath),
						symptom( mild_chest_pain),
						symptom( scaly_rash),
						symptom( fever),
						symptom( red_bumps_on_legs),
						symptom( sore_eyes),
						symptom( swollen_ankles).
						
disease(asbestosis):-
						symptom( chest_tightness),
						symptom( shortness_of_breath),
						symptom( chest_pain),
						symptom( lack_of_appetite).
						

disease(asthma):-
						symptom( wheezing),
						symptom( cough),
						symptom( chest_tightness),
						symptom( shortness_of_breath).
						
disease(bronchiolitis):-
						symptom( wheezing),
						symptom( fever),
						symptom( blue_skin),
						symptom( rapid_breath).
						
disease(influenza):-
						symptom( headache),
						symptom( fever),
						symptom( shaking_chills),
						symptom( nasal_congestion),
						symptom( runny_nose),
						symptom( sore_throat).
						
disease(lung_cancer):-
						symptom( cough),
						symptom( fever),
						symptom( hoarseness),
						symptom( chest_pain),
						symptom( wheezing),
						symptom( weight_loss),
						symptom( lack_of_appetite),
						symptom( coughing_blood),
						symptom( headache),
						symptom( shortness_of_breath).
						

/*Ask rules*/

symptom(Val) :- ask('Does the Patient have',Val).

ask(Obj, Val) :- known(Obj, Val, true),!.

ask(Obj, Val) :- known(Obj, Val, false), !,fail.

ask(Obj, Val):-	nl,write(Obj),write(' '),
				write( Val) , write('?(y/n)'), read(Ans), !,
				((Ans=y, assert(known(Obj, Val, true)));(assert(known(Obj, Val, false)) , fail )).
			
diagnose :- nl,write('Diagnosing a lung disease..........'),nl,disease(Disease) ,!,nl,
			write('That lung disease could be '), write(Disease).

diagnose :- nl, write('Sorry,we may not be able to diagnose the desease!!').

start :- notice,repeat, abolish(known/3),dynamic(known/3), diagnose,nl,nl, write('Try again ? (y/n)'),read(Resp),Resp=n,
		 nl,write('Bye ! Thanks for using this system'),abolish(known,3) .