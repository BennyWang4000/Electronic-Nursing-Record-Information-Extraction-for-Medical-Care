from ltp import LTP
from core.health_ner import HealthNER
from core.sentence_unit import SentenceUnit


class HealthDep:
    '''object to get dependency word
    param
        hner: core.ner.HealthNER
        ltp: ltp.LTP
    '''

    def __init__(self, hner: HealthNER, ltp: LTP):
        self.ltp = ltp
        self.hner = hner

    def get_dep(self, content):
        '''get dependency word by typed dependency tree
        param
            content: str
        return 
            body_lst: list<tuple<str>>
            symp_lst: list<str>
            dise_lst: list<str>
        '''
        body_lst = []
        symp_lst = []
        dise_lst = []

        content = '。' + content + '。'
        nes = self.hner.get_ne(content, type=['BODY', 'DISE', 'SYMP'])
        seg, hidden = self.ltp.seg([content])
        seg, hidden, _ = self.hner.ne_seg(content, self.ltp)

        pos = self.ltp.pos(hidden)
        dep = self.ltp.dep(hidden)
        sdp = self.ltp.sdp(hidden)

        ne_idx_lst = self.hner.get_ne_idx(seg[0], nes)

        sentence = SentenceUnit(
            seg_lst=seg[0],
            pos_lst=pos[0],
            dep_lst=dep[0],
            sdp_lst=sdp[0],
            ne_idx_lst=ne_idx_lst,
            ne_dct=nes,
        )

        dep_used_idx_lst = []

        for idx, ne_idx in enumerate(ne_idx_lst):
            dep_tup = ()
            ne_word = sentence.get_word_by_idx(ne_idx)
            # print('0', ne_word.word)
            ne_dep_idx = ne_word.dep_idx
            ne_dep_word = sentence.get_word_by_idx(ne_word.dep_idx)

            # * =================================================================

            if ne_word.type == 'BODY' and ne_word.idx not in dep_used_idx_lst:
                dep_used_idx_lst.append(ne_word.idx)
                dep_tup += (ne_word.word,)

                while ne_dep_word.type == 'BODY':
                    # print('1', ne_dep_word.word)
                    if ne_dep_word.idx not in dep_used_idx_lst:
                        # print('2', ne_dep_word.word)
                        dep_tup += (ne_dep_word.word,)
                        dep_used_idx_lst.append(ne_dep_word.idx)
                    ne_dep_word = sentence.get_word_by_idx(ne_dep_word.dep_idx)
                # print('3', ne_dep_word.word)
                dep_used_idx_lst.append(ne_dep_word.idx)
                dep_tup += (ne_dep_word.word,)

            # * =================================================================

            if ne_dep_word.dep_type == 'CMP':
                ne_dep_idx = ne_dep_word.dep_idx
            if ne_dep_word.dep_type == 'HED' and ne_dep_word.pos == 'v':
                for word in sentence.words:
                    if word.dep_idx == ne_dep_word.idx and word.dep_type == 'VOB':
                        ne_dep_idx = word.idx
                        break
            if ne_dep_word.dep_type == 'HED' and ne_dep_word.pos == 'p':
                for word in sentence.words:
                    if word.dep_idx == ne_dep_word.idx and word.dep_type == 'SBV':
                        ne_dep_idx = word.idx
                        break
            if ne_dep_word.dep_type == 'ADV' and ne_dep_word.pos == 'nb':
                ne_dep_idx= ne_dep_word.dep_idx

            # * =================================================================

            ne_dep_word = sentence.get_word_by_idx(ne_dep_idx)

            if ne_word.type == 'SYMP':
                if ne_word.idx not in dep_used_idx_lst:
                    symp_lst.append(ne_word.word)
            if ne_word.type == 'DISE':
                dise_lst.append(ne_word.word)
            if ne_word.type == 'BODY':
                body_lst.append(dep_tup)

        return body_lst, symp_lst, dise_lst

    def get_sdp(self, content):
        body_lst = []
        symp_lst = []
        dise_lst = []

        content = '。' + content + '。'
        nes = self.hner.get_ne(content, type=['BODY', 'DISE', 'SYMP'])
        seg, hidden = self.ltp.seg([content])
        seg, hidden, _ = self.hner.ne_seg(content, self.ltp)

        pos = self.ltp.pos(hidden)
        dep = self.ltp.dep(hidden)
        sdp = self.ltp.sdp(hidden)

        ne_idx_lst = self.hner.get_ne_idx(seg[0], nes)

        sentence = SentenceUnit(
            seg_lst=seg[0],
            pos_lst=pos[0],
            dep_lst=dep[0],
            sdp_lst=sdp[0],
            ne_idx_lst=ne_idx_lst,
            ne_dct=nes,
        )

        print('===========')
        sentence.print_words()
        print('===========')

        body_sdp_lst = []
        symp_sdp_lst = []
        dise_sdp_lst = []

        body_set = set()
        symp_set = set()
        dise_set = set()

        dep_used_idx_lst = []

        for idx, ne_idx in enumerate(ne_idx_lst):
            sdp_tup = ()
            # * SDP
            ne_word = sentence.get_word_by_idx(ne_idx)
            # if ne_word.type == 'BODY':
            #     body_set.add(ne_word['word'])
            # elif ne_word.type == 'DISE':
            #     dise_set.add(ne_word['word'])
            # elif ne_word.type == 'SYMP':
            #     symp_set.add(ne_word['word'])

            ne_sdp_idx = ne_word.sdp_idx
            ne_sdp_word = sentence.get_word_by_idx(ne_word.sdp_idx)

            if ne_word.type == 'BODY':
                sdp_tup += (ne_word.word, ne_sdp_word.word,)

            sdp_on_ne_lst = sentence.get_depend(ne_idx, 'sdp')
            for word in sdp_on_ne_lst:
                if word.sdp_type == 'mNEG':
                    sdp_tup += (word.word,)

            ne_sdp_word = sentence.get_word_by_idx(ne_sdp_idx)

            print(ne_word.word + '\t' + ne_word.type, '\t--->\t',
                  ne_sdp_word.word + '\t' + ne_sdp_word.type)

            if ne_word.type == 'SYMP':
                sdp_tup += (ne_word.word,)
                symp_sdp_lst.append(sdp_tup)
            if ne_word.type == 'DISE':
                sdp_tup += (ne_word.word,)
                dise_sdp_lst.append(sdp_tup)
            if ne_word.type == 'BODY':
                body_sdp_lst.append(sdp_tup)

        return body_lst, symp_lst, dise_lst
