# Electronic Nursing Record Information Extraction for Medical Care

## Frontend
MVVM pattern\
tkinter python ui\
PyMySQL mysql connector\
Data Access Object


## Bert NER Core Package Usage
```python
from emr_ie.core.health_ner import HealthNER

hner_model_path = 'emr_ie/data/model/model_ner_adam_1e-06_2.pt'
hner = HealthNER(hner_model_path)

print(hner.get_ne_long('長期服用超大劑量會引起肝毒性。若有發疹、發紅、噁心、嘔吐、食慾不振、頭暈、耳鳴等症狀時，應停藥就醫。'))
#[('肝', 'DISE'), ('發疹', 'SYMP'), ('發紅', 'SYMP'), ('噁心', 'SYMP'), ('嘔吐', 'SYMP'), ('食慾不振', 'SYMP'), ('頭暈', 'SYMP'), ('耳鳴', 'SYMP')]
```


## Reference:
- (Sonit Singh, 2018) Natural Language Processing for Information Extraction
- (CHANG, WAN-YU, 2020)  Developing the Predictive Model for Violence in Psychiatric Inpatients by Using Data from Electronic Medical Record: A Text Mining Approach
- (H Yang, 2019) Pipelines for Procedural Information Extraction from Scientific Literature: Towards Recipes using Machine Learning and Data Science
- pdfminer.six https://github.com/pdfminer/pdfminer.six
- CkipTagger https://github.com/ckiplab/ckiptagger
- gensim – Topic Modelling in Python https://github.com/RaRe-Technologies/gensim
- Natural Language Toolkit (NLTK) https://github.com/nltk/nltk
- scikit-learn https://github.com/scikit-learn/scikit-learn
- Chinese medical dialogue data 中文医疗对话数据集 https://github.com/Toyhom/Chinese-medical-dialogue-data
- Chinese HealthNER Corpus https://github.com/NCUEE-NLPLab/Chinese-HealthNER-Corpus
- cMedQA2 https://github.com/zhangsheng93/cMedQA2
- LTP 4 https://github.com/HIT-SCIR/ltp
- open-entity-relation-extraction https://github.com/lemonhu/open-entity-relation-extraction
- tkmvvm https://github.com/Joklost/tkmvvm
- python-dao-mysql-example https://github.com/bdekk/python-dao-mysql-example
