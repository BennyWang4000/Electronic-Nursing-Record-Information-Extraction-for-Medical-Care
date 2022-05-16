from ltp import LTP
from ner import HealthNER
from sentence_unit import SentenceUnit


class Dep:
    def __init__(self, hner: HealthNER, ltp: LTP):
        self.ltp = ltp
        self.hner = hner

    def get_dep(self, content):
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
            sdp_tup = ()
            dep_tup = ()
            ne_word = sentence.get_word_by_idx(ne_idx)

            ne_dep_idx = ne_word.dep_idx
            ne_dep_word = sentence.get_word_by_idx(ne_word.dep_idx)
            # * =================================================================

            if ne_word.type == 'BODY' and ne_word.idx not in dep_used_idx_lst:
                sdp_tup += (ne_word.word, ne_dep_word.word,)
                dep_used_idx_lst.append(ne_dep_word.idx)
                dep_tup += (ne_word.word,)

                while ne_dep_word.type == 'BODY':
                    if ne_dep_word.idx not in dep_used_idx_lst:
                        dep_tup += (ne_dep_word.word,)
                        dep_used_idx_lst.append(ne_dep_word.idx)
                    ne_dep_word = sentence.get_word_by_idx(ne_dep_word.dep_idx)
                dep_tup += (ne_dep_word.word,)

            # * =================================================================
            if ne_dep_word.dep_type == 'CMP':
                print('CMP:')
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
            # * =================================================================

            ne_dep_word = sentence.get_word_by_idx(ne_dep_idx)

            if ne_word.type == 'SYMP':
                dep_tup += (ne_word.word,)
                symp_lst.append(dep_tup)
            if ne_word.type == 'DISE':
                dep_tup += (ne_word.word,)
                dise_lst.append(sdp_tup)
                dise_lst.append(dep_tup)
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
        body_dep_lst = []
        symp_dep_lst = []
        dise_dep_lst = []

        body_set = set()
        symp_set = set()
        dise_set = set()

        dep_used_idx_lst = []

        for idx, ne_idx in enumerate(ne_idx_lst):
            sdp_tup = ()
            dep_tup = ()
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

            ne_dep_idx = ne_word.dep_idx
            ne_dep_word = sentence.get_word_by_idx(ne_word.dep_idx)

            if ne_word.type == 'BODY':
                sdp_tup += (ne_word.word, ne_sdp_word.word,)
                dep_used_idx_lst.append(ne_dep_word.idx)

                dep_tup += (ne_word.word,)
                while ne_dep_word.type == 'BODY':
                    # if ne_dep_word.idx not in dep_used_idx_lst:
                    dep_tup += (ne_dep_word.word,)
                    dep_used_idx_lst.append(ne_dep_word.idx)
                    ne_dep_word = sentence.get_word_by_idx(ne_dep_word.dep_idx)
                dep_tup += (ne_dep_word.word,)

            sdp_on_ne_lst = sentence.get_depend(ne_idx, 'sdp')
            for word in sdp_on_ne_lst:
                if word.sdp_type == 'mNEG':
                    sdp_tup += (word.word,)

            if ne_dep_word.dep_type == 'CMP':
                print('CMP:')
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

            ne_sdp_word = sentence.get_word_by_idx(ne_sdp_idx)
            ne_dep_word = sentence.get_word_by_idx(ne_dep_idx)

            print(ne_word.word + '\t' + ne_word.type, '\t--->\t',
                  ne_sdp_word.word + '\t' + ne_sdp_word.type)

            if ne_word.type == 'SYMP':
                sdp_tup += (ne_word.word,)
                dep_tup += (ne_word.word,)
                symp_sdp_lst.append(sdp_tup)
                symp_dep_lst.append(dep_tup)
            if ne_word.type == 'DISE':
                sdp_tup += (ne_word.word,)
                dep_tup += (ne_word.word,)
                dise_sdp_lst.append(sdp_tup)
                dise_dep_lst.append(dep_tup)
            if ne_word.type == 'BODY':
                body_sdp_lst.append(sdp_tup)
                body_dep_lst.append(dep_tup)

        return body_lst, symp_lst, dise_lst
