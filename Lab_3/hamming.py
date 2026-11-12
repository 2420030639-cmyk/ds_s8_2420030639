def hamming_dist(str1, str2) :
    if (len(str1) != len(str2)):
        raise ValueError("Strings must be equal")
    return sum (ch1 != ch2 for ch1, ch2 in zip(str1, str2))

s1 = "Hi, Im Kundana"
s2 = "Hi, Im Keerthi"

dist = hamming_dist(s1, s2)
print("Hamming distance: ", dist) 
