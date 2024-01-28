import math

def shannon_entropy(a, c, g, t):
    total_count = a + c + g + t

    # Calculate probabilities
    prob_a = a / total_count
    prob_c = c / total_count
    prob_g = g / total_count
    prob_t = t / total_count

    # Calculate Shannon entropy
    if prob_a != 0 and prob_c != 0 and prob_g != 0 and prob_t != 0:
        entropy = - (prob_a * math.log2(prob_a) + prob_c * math.log2(prob_c)
                 + prob_g * math.log2(prob_g) + prob_t * math.log2(prob_t))

        return entropy

# Print results
print(shannon_entropy(0, 2, 13, 7))
print(shannon_entropy(12, 2,9,8))
