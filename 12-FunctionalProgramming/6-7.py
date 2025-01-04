ratings = [(17,15,16,17,15),
 (16,18,19,17,19),
 (19,15,15,19,18),
 (18,17,19,15,16)]

# def calculatin_final_scores(scores):
#     return sum(scores)-min(scores)-max(scores)

# result = list(map(calculatin_final_scores, ratings))
# print(result)

final_results = list(map(lambda scores: sum(scores)-min(scores)-max(scores), ratings))
print(final_results)