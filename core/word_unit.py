class WordUnit:
    '''all information of word
    param
        word: str, chinese word
        pos: str, parts of speech
        type: str, named entity type
        dep_idx: int
        dep_type: str
    '''

    def __init__(self, word, pos, type, idx, dep_idx, dep_type, sdp_idx, sdp_type):
        self.word = word
        self.pos = pos
        self.type = type
        self.idx = idx
        self.dep_idx = dep_idx
        self.dep_type = dep_type
        self.sdp_idx = sdp_idx
        self.sdp_type = sdp_type

    def print_word(self):
        print(self.word + '\t' + self.pos + '\t' + self.type + '\t' + str(self.idx) + '\t'
              + str(self.dep_idx) + '\t' + self.dep_type + '\t'
              + str(self.sdp_idx) + '\t' + self.sdp_type)
