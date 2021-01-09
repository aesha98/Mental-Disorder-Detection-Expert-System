import pickle

import pandas as pd


def predicts(inputs):
    header = ['bloody_stools','fecal_leakage','swelling','dizziness',
              'confusion','fatigue','itching','vomiting','arm_pain','cough','muscle_pain','depression',
              'fever','painful_bowel_moments','urine_blood','sweating','nausea','stiff_neck','decreased_appetite',
              'weak','wheezing','bleeding']

    df = pd.read_csv("Disorder_Symptom.csv")
    disease = set(df.iloc[:, 0])
    disease = list(disease)
    disease.sort()

    model_inputs5 = []
    for x in range(0, len(header)):
        model_inputs5.append(0)


    for element in range(0, len(header)):
        for symptom in inputs:
            if symptom == header[element]:
                model_inputs5[element] = 1


    with open("DecisionTreeModel", "rb") as f:
        Model_Decision_Tree = pickle.load(f)

    pred = Model_Decision_Tree.predict([model_inputs5])

    print(disease[pred[0]])
    return disease[pred[0]]


if __name__ == '__main__':

    pass