#!/usr/bin/env python

import os
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

os.chdir(sys.argv[1])

student_files = [doc for doc in os.listdir() if doc.endswith('.txt')]
student_notes =[open(File, encoding='utf-8').read() for File in student_files]

vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()
similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])

vectors = vectorize(student_notes)
s_vectors = list(zip(student_files, vectors))

def check_plagiarism():
    plagiarism_results = set()
    global s_vectors
    for student_a, text_vector_a in s_vectors:
        new_vectors = s_vectors.copy()
        current_index = new_vectors.index((student_a, text_vector_a))
        del new_vectors[current_index]
        for student_b , text_vector_b in new_vectors:
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
            student_pair = sorted((student_a, student_b))
            score = (sim_score, student_pair[0], student_pair[1])
            plagiarism_results.add(score)
    return plagiarism_results


result_set = check_plagiarism()
sorted_result = sorted(result_set, key=lambda x: x[0])

for data in sorted_result:
    print(f'{100 * data[0]:.1f}%  {data[1]:<60} {data[2]}')
    
    