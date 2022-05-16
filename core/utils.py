label_dict = {'O': 0,
              'B-BODY': 1, 'I-BODY': 2,
              'B-SYMP': 3, 'I-SYMP': 4,
              'B-INST': 5, 'I-INST': 6,
              'B-EXAM': 7, 'I-EXAM': 8,
              'B-CHEM': 9, 'I-CHEM': 10,
              'B-DISE': 11, 'I-DISE': 12,
              'B-DRUG': 13, 'I-DRUG': 14,
              'B-SUPP': 15, 'I-SUPP': 16,
              'B-TREAT': 17, 'I-TREAT': 18,
              'B-TIME': 19, 'I-TIME': 20,
              }

ids_dict = {label_dict[k]: k for idx, k in enumerate(label_dict)}
