def union(f,i,j):
    fi = find(f,i)
    fj = find(f,j)
    if fi != fj:
        f[fi] = fj

def find(f,i):
    j = i
    while f[j] != j:
        j = f[j]
    while f[i] != j:
        fi = f[i]
        f[i] = j
        i = fi
    
    return j

# check my submission in leetcode. https://leetcode.com/problems/minimize-malware-spread/submissions/
