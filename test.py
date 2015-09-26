def test_subset(candidates):
    length = len(candidates)
    for i in xrange(length):
        idx_list = [candidates[k] for k in xrange(length) if k != i]
        print idx_list
        

def is_match_apriori_property(subset):
        pre_fp_itemset = [[1,2,3], [2,4,5], [0, 7, 8]]
        for item in pre_fp_itemset:
            if cmp(item, subset) == 0:
                return True
                
        return False
        
def compute_support(candidate, data):
        support = 0
        len_candidate = len(candidate)
        for trans in data:
            len_trans = len(trans)
            i = 0
            j = 0
            while i < len_candidate and j < len_trans:
                if candidate[i] == trans[j]:
                    i = i + 1
                    j = j + 1
                else:
                    j = j + 1
            if i == len_candidate:
                '''
                print i
                print candidate
                print trans
                '''
                support = support + 1   
                
        return support

def _get_all_subsets(collection):
    length = len(collection)
    
    if length == 0:
        return
    
    if length == 1:
        print collection
        return 
    
    for i in xrange(length):
        cur_collection = [collection[k] for k in xrange(length) if k != i]
        print cur_collection
        _get_all_subsets(cur_collection)
        
# test 1       
# test_subset([9, 5, 1, 0, 3])

# test 2
'''
print is_match_apriori_property([0,7,8])
print is_match_apriori_property([0,7,9])
print is_match_apriori_property([11, 22, 33])
print is_match_apriori_property([1,2,3])
print is_match_apriori_property([2,4,5])
'''

# test 3
'''
data = [[1,4,5], [1], [2,3,7], [1,2,6], [1,5], [1,3,5,7],[],[5],[0,1,3,5],[7]]
candidate = [1, 5]
print compute_support(candidate, data) # 4
print compute_support(candidate, [[1,4,5]]) # 4
print compute_support(candidate, [[1]]) # 4
print compute_support(candidate, [[2,3,7]]) # 4
print compute_support(candidate, [[1,2,6]]) # 4
print compute_support(candidate, [[1,5]]) # 4
print compute_support(candidate, [[1,3,5,7]]) # 4
print compute_support(candidate, [[]]) # 4
print compute_support(candidate, [[5]]) # 4
print compute_support(candidate, [[0,1,3,5]]) # 4
print compute_support(candidate, [[7]]) # 4
'''
# test 4
_get_all_subsets([1, 2, 4, 6, 9])
