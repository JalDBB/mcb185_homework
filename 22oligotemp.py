def calculate_tm(oligo):
    # nucleotides
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0

    for nucleotide in oligo:
        if nucleotide == 'A':
            a_count += 1
        elif nucleotide == 'C':
            c_count += 1
        elif nucleotide == 'G':
            g_count += 1
        elif nucleotide == 'T':
            t_count += 1

    if a_count + t_count <= 13:
        tm = (a_count + t_count) * 2 + (g_count + c_count) * 4
    else:
        tm = 64.9 + 41 * (g_count + c_count - 16.4) / (a_count + t_count + g_count + c_count)

    return tm

# Example
oligo1 = "AGTCGTTAAGTAC"
oligo2 = "AAAAGGGGGTTTTCCCCCCCGGGGGTTTTT"
oligo3 = "TTTTTTTTCGCGCGCATATATAT"

print(calculate_tm(oligo1))
print(calculate_tm(oligo2))
print(calculate_tm(oligo3))