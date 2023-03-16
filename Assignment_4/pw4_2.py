import os
os.chdir(os.path.dirname(__file__))

filename = input("Enter filename: ")
with open(filename, "r") as f:
    domains = {}
    for line in f:
        if (line.startswith("From") and not line.startswith("From:")):
            domain = line.split('@')[1].split()[0]
            domains[domain] = domains.get(domain, 0) + 1

    sorted_domains = sorted(domains.items())
    max_len = max([len(domain) for domain, count in sorted_domains]) #get the longest domains character count
    print("SORTED:")
    for k,v in sorted_domains:
        print(' ' * (max_len - len(k)), k + ':', v, '*' * v)
    f.close()
