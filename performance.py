
# Ezra Pasha Ramadhansyah - 2006597872

import json

"""
TODO: Gunakan file performance.py ini untuk membuat class Performance yang 
nantinya akan digunakan untuk menghitung akurasi (Best Match Accuracy & Candidate Match) 
dan run-time
"""

class Performance:
    
    def __init__(self, test_file):
        self.test_dict = dict()
        json_file = json.loads(test_file)
        self.parse_json(json_file)

    def parse_json(self, json_file):
        amount = 800
        num = 0

        for i in json_file:
            num +=1
            self.test_dict[i] = list()
            for j in json_file[i]:
                self.test_dict[i].append(j['typo'])
            
            if num == amount: break

    def test_model_candidate_match(self, model):
        # print("Start Testing Best Candidate...")
        total_non_word = 0
        total_correct_candidate = 0
        total_correct_first = 0

        key_amount = 0
        
        for key in self.test_dict.keys():
            for non_word in self.test_dict[key]:
                total_non_word += 1
                candidate_list = model.get_candidates(non_word, 2)

                if key == candidate_list[0]:
                    total_correct_first += 1

                if key not in candidate_list:
                    continue
                pos = candidate_list.index(key)
                if key != candidate_list[pos]:
                    continue
                total_correct_candidate += 1

            key_amount += 1

            # print("Finished for",key)
            # print("Completeness", (key_amount/len(self.test_dict.keys())) * 100,"%")
        
        return (total_correct_candidate / total_non_word) * 100, (total_correct_first / total_non_word) * 100
    
    '''
    def test_model_best_match(self, model):
        print("Start Testing Best Match...")
        total_non_word = 0
        total_correct_candidate = 0

        key_amount = 0
        
        for key in self.test_dict.keys():
            for non_word in self.test_dict[key]:
                total_non_word += 1
                candidate_list = model.get_candidates(non_word, 5)
                if key == candidate_list[0]:
                    total_correct_candidate += 1
            key_amount += 1
            print("Finished for",key)
            print("Completeness", (key_amount/len(self.test_dict.keys())) * 100,"%")
        
        return (total_correct_candidate / total_non_word) * 100
    '''