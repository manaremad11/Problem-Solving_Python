import numpy as np

# Example true and predicted labels
y_true = [0, 1, 0, 1, 0, 1, 0, 1, 1, 1]
y_pred = [0, 0, 0, 1, 0, 1, 1, 1, 1, 1]

# Initialize 2x2 confusion matrix
confusion_matrix = [[0, 0], [0, 0]]

# Populate confusion matrix
for true, pred in zip(y_true, y_pred):
    if true == 0 and pred == 0:
        confusion_matrix[0][0] += 1  # TN
    elif true == 0 and pred == 1:
        confusion_matrix[0][1] += 1  # FP
    elif true == 1 and pred == 0:
        confusion_matrix[1][0] += 1  # FN
    elif true == 1 and pred == 1:
        confusion_matrix[1][1] += 1  # TP

# Print confusion matrix
print("Confusion Matrix:")
print(np.array(confusion_matrix))

# Calculate performance metrics
TN = confusion_matrix[0][0]
FP = confusion_matrix[0][1]
FN = confusion_matrix[1][0]
TP = confusion_matrix[1][1]

accuracy = (TP + TN) / (TP + TN + FP + FN)
precision = TP / (TP + FP)
recall = TP / (TP + FN)
f1_score = 2 * (precision * recall) / (precision + recall)

print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1_score}')
