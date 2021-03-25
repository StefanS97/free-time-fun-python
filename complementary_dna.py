def DNA_strand(dna):
    dns = dna.lower()
    lists = list(dns)
    helper = ''
    for i in range(len(lists)):
        if lists[i] == 'a':
            helper += 't'
        if lists[i] == 't':
            helper += 'a'
        if lists[i] == 'c':
            helper += 'g'
        if lists[i] == 'g':
            helper += 'c'

    return helper.upper()