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
        self.cur_flag_list = []
        
    def run(self):
        # generate 1-itemset frequent pattern
        self._gen_one_itemset_fp()
        k = 0
        # main loop
        while True:
            k += 1
            self._gen_candidates(k)
            self._prune_by_apriori_property(k)
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
                    
        # 标识这个candidate是否要去除
        self.cur_flag_list = [True for i in xrange(len(self.cur_candidates))] 
                    
    def _prune_by_apriori_property(self, k):
        cur_len = len(self.cur_candidates[0])
        # traverse candidate of this iteration
        for idx,candidate in enumerate(self.cur_candidates):
            # get all subsets of this candidate
            for i in xrange(cur_len):
                subset = [candidate[j] for j in xrange(cur_len) if j != i]
                if not self._is_match_apriori_property(k, subset):
                    self.cur_flag_list[idx] = False
                    break
                
    def _prune_by_support(self):
        # traverse candidate of this iteration
        for idx, candidate in enumerate(self.cur_candidates):
            # only consider current avaliable candidate
            if self.cur_flag_list[idx]:
                support = self._compute_support(candidate)
        # get count
        
    def _compute_support(self, candidate):
        for 
                
    def _is_match_apriori_property(self, k, subset):
        pre_fp_itemset = self.fp_itemsets[k-1]
        for item in pre_fp_itemset:
            if cmp(item, subset) == 0:
                return True
                
        return False
    
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
        
