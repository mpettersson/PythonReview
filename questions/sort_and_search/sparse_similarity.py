"""
    SPARSE SIMILARITY

    The similarity of two documents (each with distinct words) is defined to be the size of the intersection divided by
    the size of the union.  For example, if the documents consisted of integers, the similarity of {1, 5, 3} and
    {1, 7, 2, 3} is 0.4, because the intersection has size 2 and the union has size 5.

    We have a long list of documents (with distinct values and each with an associated ID) where the similarity is
    believed to be "sparse".  That is, any two arbitrarily selected documents are very likely to have similarity 0.
    Design an algorithm that returns a list of paris of document IDs and the associated similarity.

    Print only the pairs with similarity greater than 0.  Empty documents should not be printed at all.  For simplicity,
    you may assume each document is represented as an array of distinct integers.

    Example
        Input:  13: {14, 15, 100, 9, 3}
                16: {32, 1, 9, 3, 5}
                19: {15, 29, 2, 6, 8, 7}
                24: {7, 10}

        Output: ID1, ID2 : SIMILARITY
                13,  19  : 0.1
                13,  16  : 0.25
                19,  24  : 0.14285714285714285
"""
import random


# Approach 1: Naive Brute Force; has a runtime of O(D**2 * W**2), where D is the number of documentss and W is the most
# number of words in each document.
def get_sparse_similarity_naive(doc_dict):
    candidates = []
    results = {}
    for k, v in doc_dict.items():
        if v is not None and len(v) > 0:
            candidates.append(k)
    if len(candidates) > 1:
        for i in range(len(candidates) - 1):
            for j in range(i + 1, len(candidates)):
                len_a = len(doc_dict[candidates[i]])
                len_b = len(doc_dict[candidates[j]])
                len_intersect = len(doc_dict[candidates[i]].intersection(doc_dict[candidates[j]]))

                # NOTE: This is one optimization; use len of intersect to compute len of union (preventing union call).
                len_union = len_a + len_b - len_intersect

                sim = len_intersect / len_union

                if sim > 0:
                    results[(candidates[i], candidates[j])] = sim
    return results


# Approach 2: Optimized--Use dict for a list of docs, and a dict that maps from doc pairs to integers (which will
# indicate the size of the intersection), runtime is O(PW + DW) where PW is the Pair of Words that overlap in each DW,
# or Document of Words.
def get_sparse_similarity(doc_dict):
    word_to_docs = group_words(doc_dict)
    similarities = compute_intersections(word_to_docs)
    adjust_to_similarities(doc_dict, similarities)
    return similarities


# Create a dict from each word to where it appears
def group_words(doc_dict):
    word_to_docs = {}
    for k, v in doc_dict.items():
        for i in v:
            if i in word_to_docs:
                word_to_docs[i].append(k)
            else:
                word_to_docs[i] = [k]
    return word_to_docs


# Compute intersections of docs, Iterate through each list of docs and then each pair within that list, incrementing the
# intersection of each page.
def compute_intersections(word_to_docs):
    similarities = {}
    for word in word_to_docs.keys():
        docs = word_to_docs[word]
        docs.sort()
        for i in range(len(docs)):
            for j in range(i + 1, len(docs)):
                increment(similarities, docs[i], docs[j])
    return similarities


# Increment the intersection size of each doc pair.
def increment(similarities, doc_one, doc_two):
    pair = (doc_one, doc_two)
    if pair not in similarities:
        similarities[pair] = 1.0
    else:
        similarities[pair] += 1


# Adjust the intersection value to become the similarity.
def adjust_to_similarities(doc_dict, similarities):
    for (doc_one, doc_two), intersection in similarities.items():
        union = len(doc_dict[doc_one]) + len(doc_dict[doc_two]) - intersection
        similarities[(doc_one, doc_two)] = intersection / union


lil_d = {13: {14, 15, 100, 9, 3}, 16: {32, 1, 9, 3, 5}, 19: {15, 29, 2, 6, 8, 7}, 24: {7, 10}}
big_d = {k: {random.randint(0, 1000) for _ in range(random.randint(0, 100))} for k in range(100)}
print("lil_d:", lil_d)
print("big_d:", big_d)
print()

print("get_sparse_similarity_naive(lil_d):", get_sparse_similarity_naive(lil_d))
print("get_sparse_similarity_naive(big_d):", get_sparse_similarity_naive(big_d))
print()

print("get_sparse_similarity(lil_d):", get_sparse_similarity(lil_d))
# Sorting get_sparse_similarity(big_d) so it'll be easier to compare to get_sparse_similarity_naive(big_dict)
print("get_sparse_similarity(big_d):", {k: v for k, v in sorted(get_sparse_similarity(big_d).items(), key=lambda i: i[0])})

