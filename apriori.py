# from dataset import Dataset
from dataset import load_from_file

class Apriori(object):
    
    
    def __init__(self, data_path=None, min_support=0.2, min_confidence=0.2):
        self.min_support = min_support
        self.min_confidence = min_confidence
        # self.dataset = Dataset()
        if data_path == None:
            raise ValueError("data path should be specifed!")
        # self.dataset.load_from_file(data_path)
        self.data = dataset.load_from_file(data_path)
        self.num_trans = len(data)
        # frequent patterns
        self.fp_itemsets = []
        # current candidates 
        self.cur_candidates = []
        
    def run(self):
        # generate 1-itemset frequent pattern
        self._gen_one_itemset_fp()
        k = 0
        # main loop
        while True:
            k += 1
            self._gen_candidates(k)
            self._prune_by_apriori_property()
            self._prune_by_support()
            
        return ...
        
    def _gen_candidates(self, k):
        self.cur_candidates = []
        pre_itemset = self.fp_itemsets[k-1]
        # self join operation
        # assume fp itemset are sorted
        for idx1, item1 in enumerate(pre_itemset):
            for idx2, item2 in enumerate(pre_itemset):
                # same item, skip
                if idx1 == idx2:
                    continue
                if cmp(item1[:k-1], item2[:k-1]) == 0 and
                   item1[k-1] < item2[k-1]:
                    self.cur_candidates.append(item1[:k-1] + item2[k-1])
                    
    def _prune_by_apriori_property(self):
        for candidate in self.cur_candidates:
            
            
    
    def _gen_one_itemset_fp(self):
        one_candidates = {}
        for trans in self.data:
            for elem in trans:
                if one_candidates.has_key(elem):
                    one_candidates[elem] = one_candidates[elem] + 1
                else:
                    one_candidates[elem] = 1
                    
        # prune by min_support
        one_itemset = []
        for key, value in one_candidates.items():
            if value / float(self.num_trans) >= self.min_support:
                trans = [key]
                one_itemset.append(trans)
        self.fp_itemsets.append(one_itemset)        
        
