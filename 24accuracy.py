def calculate_metrics(tp, fp, tn, fn):
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * ((precision * recall) / (precision + recall))
    accuracy = (tp + tn) / (tp + fp + tn + fn)
    return f1_score, accuracy

print(calculate_metrics(50,10,90,5))
print(calculate_metrics(3,7,9,1))
print(calculate_metrics(7,8,9,5))
