
# Ezra Pasha Ramadhansyah - 2006597872

from performance import Performance
from trie_structure.levenshtein_trie import LevenshteinTrie
from trie_structure.damerau_levenshtein_trie import DamerauLevenshteinTrie
from dict_structure.levenshtein_dict import LevenshteinDict
from dict_structure.damerau_levenshtein_dict import DamerauLevenshteinDict
import json
import time


""" 
TODO: Hitung akurasi dan Run-Time dari semua algoritma yang sudah disediakan, seperti 
LevenshteinTrie, DamerauLevenshteinTrie, LevenshteinDict, dan DamerauLevenshteinDict. 
Gunakan SALTIK (https://github.com/ir-nlp-csui/saltik) sebagai dataset 
dan atur parameter MAX_COST untuk setiap algoritma sebesar 2 ketika memanggil 
fungsi untuk pengambilan kandidat.
"""
def main():
    j = open("saltik-revised.json", "r")
    test = Performance(j.read())

    lev_trie = LevenshteinTrie("./kbbi_dataset.txt")
    lev_dict = LevenshteinDict("./kbbi_dataset.txt")
    dalev_trie = DamerauLevenshteinTrie("./kbbi_dataset.txt")
    dalev_dict = DamerauLevenshteinDict("./kbbi_dataset.txt")
    
    waktu_1 = time.time()
    # lev_trie_best_accuracy,  = test.test_model_best_match(lev_trie)
    candidate_accuracy, best_accuracy = test.test_model_candidate_match(lev_trie)
    waktu_2 = time.time()
    waktu = waktu_2 - waktu_1
    print("[ Ezra Pasha Ramadhansyah - 2006597872 ]")
    print("--------lev-trie--------")
    print("Best Accuracy :", best_accuracy)
    print("Candidate Accuracy :", candidate_accuracy)
    print("Total Time :", waktu)

    waktu_1 = time.time()
    # lev_trie_best_accuracy,  = test.test_model_best_match(lev_trie)
    candidate_accuracy, best_accuracy = test.test_model_candidate_match(lev_dict)
    waktu_2 = time.time()
    waktu = waktu_2 - waktu_1
    print("--------lev-dict--------")
    print("Best Accuracy :", best_accuracy)
    print("Candidate Accuracy :", candidate_accuracy)
    print("Total Time :", waktu)

    waktu_1 = time.time()
    # lev_trie_best_accuracy,  = test.test_model_best_match(lev_trie)
    candidate_accuracy, best_accuracy = test.test_model_candidate_match(dalev_trie)
    waktu_2 = time.time()
    waktu = waktu_2 - waktu_1
    print("--------damerau-lev-trie--------")
    print("Best Accuracy :", best_accuracy)
    print("Candidate Accuracy :", candidate_accuracy)
    print("Total Time :", waktu)

    waktu_1 = time.time()
    # lev_trie_best_accuracy,  = test.test_model_best_match(lev_trie)
    candidate_accuracy, best_accuracy = test.test_model_candidate_match(dalev_dict)
    waktu_2 = time.time()
    waktu = waktu_2 - waktu_1
    print("--------damerau-lev-dict--------")
    print("Best Accuracy :", best_accuracy)
    print("Candidate Accuracy :", candidate_accuracy)
    print("Total Time :", waktu)

if __name__ == '__main__':
    main()