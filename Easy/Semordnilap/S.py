def semordnilap(words):
    res = []
    seen = []
    for word in words:
        rev = word[::-1]
        if rev in words and word not in seen and rev != word:
            res.append([word, rev])
            seen.append(rev)
    return res