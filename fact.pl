symptom(john, fever).
symptom(john, cough).
symptom(john, fatigue).

symptom(mary, fever).
symptom(mary, rash).

symptom(jim, headache).
symptom(jim, nausea).

disease(Patient, flu):-
    symptom(Patient, fever),
    symptom(Patient, cough),
    symptom(Patient, fatigue).

disease(Patient,measles):-
    symptom(Patient, fever),
    symptom(Patient, rash).

disease(Patient,migraine):-
    symptom(Patient, headache),
    symptom(Patient, nausea).
