from word_unit import WordUnit


class SentenceUnit:
    '''composed of WordUnit
    param
        seg_lst: list<str>
        dep_lst: list<tuple<int, int, str>>
        ne_idx_lst: list<int>
        ne_dct: list<dict<'word': str, 'type': str, 'pos': tuple<int, int>>>

    '''

    def __init__(self, seg_lst, pos_lst, dep_lst, ne_idx_lst, ne_dct, sdp_lst):
        self.words = []
        ne_idx = 0
        for i in range(len(seg_lst)):
            word_type = 'O'
            if ne_idx < len(ne_idx_lst):
                if i == ne_idx_lst[ne_idx]:
                    word_type = ne_dct[ne_idx]['type']
                    ne_idx += 1
            self.words.append(WordUnit(
                word=seg_lst[i],
                pos=pos_lst[i],
                type=word_type,
                idx=dep_lst[i][0] - 1,
                dep_idx=dep_lst[i][1] - 1,
                dep_type=dep_lst[i][2],
                sdp_idx=sdp_lst[i][1] - 1,
                sdp_type=sdp_lst[i][2]))

    def get_word_by_idx(self, idx) -> WordUnit:
        '''
        param
            idx: int
        return
            word_unit.WordUnit
        '''
        return self.words[idx]

    def print_words(self):
        for word in self.words:
            word.print_word()

    def get_depend(self, idx, dep_type):
        assert dep_type in ['sdp', 'dep']

        dp_lst = []
        if dep_type == 'sdp':
            for word in self.words:
                if word.sdp_idx == idx:
                    dp_lst.append(word)
        else:
            for word in self.words:
                if word.dep_idx == idx:
                    dp_lst.append(word)

        return dp_lst
