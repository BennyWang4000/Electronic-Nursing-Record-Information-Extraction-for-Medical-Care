# %%
# from ltp import LTP

from core.utils import ids_dict, label_dict
import torch
from transformers import BertTokenizerFast


class HealthNER:
    def __init__(self, model_path, is_cpu=True, is_debug=False):
        '''
        params
            model_path: str, path of bert ner model
            is_cpu: bool, use cpu or not
            is_debug: bool, print log or not
        '''
        self.tokenizer = BertTokenizerFast.from_pretrained(
            'bert-base-chinese')

        self.is_debug= is_debug

        if is_cpu:
            self.model = torch.load(
                model_path, map_location=torch.device('cpu'))
        else:
            self.model = torch.load(model_path)

        self.model.eval()

    def _get_model_output(self, sentence):
        '''get output of model after decode
        params
            sentence: str
        returns
            labels: list<str>
                types of each token
            ids: list<int>
                tokenizer ids of each token
        '''
        encoding = self.tokenizer(sentence,
                                  return_offsets_mapping=True,
                                  padding='max_length',
                                  truncation=True,
                                  max_length=128,)

        item = {key: torch.as_tensor(val) for key, val in encoding.items()}

        outputs = self.model(item['input_ids'].unsqueeze(
            0), attention_mask=item['attention_mask'].unsqueeze(0))

        sent_len= encoding['input_ids'].index(102)
        
        logits = outputs[0]

        active_logits = logits.view(-1, self.model.num_labels)
        flattened_predictions = torch.argmax(active_logits, axis=1)
        flt_pre_np = flattened_predictions.cpu().numpy()
        labels = [ids_dict[label] for label in flt_pre_np]
        
        return labels[1:sent_len + 1], encoding['input_ids'][1:sent_len + 1]

    def _get_decoding(self, sentence: str) -> list:
        '''**DUPLICATED**
        get list of setence chunk. Devivde by sigle character and numbers
        there's a [UNK] prob occured while encoding and decoding 

        params
            setence: str, sentence 
        return
            list<str>
        '''
        encoding = self.tokenizer.encode(sentence, return_offsets_mapping=True,
                                         padding='max_length',
                                         truncation=True,
                                         max_length=128,)

        unk_lst = [i for i, x in enumerate(encoding) if x == 100]

        decoding = self.tokenizer.decode(
            encoding[1:encoding.index(102)]).split(' ')
        count = 0
        for idx_words, words in enumerate(decoding):
            if words == '[UNK]':
                decoding[idx_words] = sentence[count]
                count += 1
                continue
            count += len(str(words))

        return decoding

    def get_ne_long(self, param, type=None):
        '''get named entity from sentence that length over 127
        params
            param: str
                source sentence.
            type: list<str>
                assert in ['BODY', 'SYMP', 'INST', 'EXAM', 'CHEM', 'DISE', 'DRUG', 'SUPP', 'TREAT', 'TIME']
                a list of entity types that you want.

        return
            list<tuple<str, str>>
                list of entity token and type tuples
        '''
        ents= []
        if len(param)> 127:
            for sentence in param.split('。'):
                ents.extend(self.get_ne(sentence))
        else:
            ents= self.get_ne(param)
        return ents

    def get_ne(self, sentence, type=None):
        '''get named entity from sentence
        params
            sentence: str
                source sentence, less than 128 character.
            type: list<str> 
                assert in ['BODY', 'SYMP', 'INST', 'EXAM', 'CHEM', 'DISE', 'DRUG', 'SUPP', 'TREAT', 'TIME']
                a list of entity types that you want.

        return
            list<tuple<str, str>>
            list of entity token and type tuples
        '''
        
        # * replace character
        # for r in self.replace_tup:
        #     sentence= sentence.replace(*r)

        ent_types, ent_ids = self._get_model_output(sentence)
        ent_lst= []
        curr_type= ''
        ent_begin= 0
        try:
            for idx, ent_type in enumerate(ent_types):
                if ent_type[0]== 'B':
                    ent_begin= idx
                    curr_type= ent_type[2:]
                if ent_type[0]== 'I':
                    if ent_type[2:]!= curr_type:
                        if curr_type!= '':
                            ent_lst.append((self.tokenizer.decode(ent_ids[ent_begin:idx]).replace(' ', ''), curr_type))
                        ent_begin= idx
                        curr_type= ent_type[2:]
                if ent_type[0]== 'O':
                    if curr_type!= '':
                        ent_lst.append((self.tokenizer.decode(ent_ids[ent_begin:idx]).replace(' ', ''), curr_type))
                    curr_type= ''
            if curr_type!= '':
                ent_lst.append((self.tokenizer.decode(ent_ids[ent_begin:idx]), curr_type))

        except:
            print('--- err ---')
            print(ent_types)
            print(self.tokenizer.decode(ent_ids).split(' '))

        return ent_lst

    def get_ne_idx(self, sent_lst, ne_lst, ignore=None):
        '''**DUPLICATED**
        '''
        if self.is_debug:
            print('seg:\t', sent_lst)
            print('ne_lst:\t', ne_lst)
        pos_lst = []
        ne_idx = 0
        for idx, word in enumerate(sent_lst):
            if ne_lst[ne_idx]['word'] in word:
                pos_lst.append(idx)
                ne_idx += 1
                if ne_idx >= len(ne_lst):
                    break

        return pos_lst

    # def ne_seg(self, sentence, ltp: LTP):
    #     '''**DUPLICATED**
    #     segment entity in ltp for dependency tree. required ltp
    #     params
    #         setence: str
    #         ltp: ltp.LTP()
    #     return
    #         seg: list<str>
    #         hidden: ?
    #         ignore: list<ne>

    #     known issue: 


    #     '''
    #     nes = self.get_ne(sentence)
    #     seg, _ = ltp.seg([sentence])

    #     for ne in nes:
    #         # * ne_word = sentence[ne['pos'][0]:ne['pos'][1]]
    #         # if ne['word'] not in seg[0]:
    #         isSet0 = False
    #         isSet1 = False
    #         count = 0
    #         for idx_w, word in enumerate(seg[0]):

    #             isSet0 = False
    #             for idx_c, word in enumerate(word):
    #                 if (word == '@' and word[-1 if idx_c + 1 >= len(word) else idx_c + 1] == '@') or (word == '@' and word[idx_c - 1] == '@'):
    #                     continue
    #                 if count == ne['pos'][0] or count == ne['pos'][1]:
    #                     if isSet0:
    #                         seg[0][idx_w] = seg[0][idx_w][:idx_c + 2] + \
    #                             '@@' + seg[0][idx_w][idx_c + 2:]
    #                         isSet1 = True
    #                     else:
    #                         seg[0][idx_w] = seg[0][idx_w][:idx_c] + \
    #                             '@@' + seg[0][idx_w][idx_c:]
    #                         isSet0 = True
    #                 count += 1
    #                 if isSet1:
    #                     break
    #             isSet0 = False

    #     seg_preseg = '@@'.join(seg[0])
    #     seg_preseg = seg_preseg.replace('@@@@@@@@@@@@', '@@')
    #     seg_preseg = seg_preseg.replace('@@@@@@@@@@', '@@')
    #     seg_preseg = seg_preseg.replace('@@@@@@@@', '@@')
    #     seg_preseg = seg_preseg.replace('@@@@@@', '@@')
    #     seg_preseg = seg_preseg.replace('@@@@', '@@')
    #     seg, hidden = ltp.seg([seg_preseg.split('@@')], is_preseged=True)

    #     ignore = []
    #     for ne in nes:
    #         if ne['word'] not in seg[0]:
    #             ignore.append(ne)

    #     return seg, hidden, ignore
# %%
