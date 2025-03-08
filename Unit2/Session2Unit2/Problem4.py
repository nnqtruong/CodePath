def subdomain_visits(cpdomains):
    for entries in cpdomains:
        number_split = entries.split[" "]
        dot_split = entries.split["."]
        for i I




cpdomains1 = ["9001 modern.artmuseum.com"]
cpdomains2 = ["900 abstract.gallery.com", "50 impressionism.com", 
              "1 contemporary.gallery.com", "5 medieval.org"]

print(subdomain_visits(cpdomains1))
print(subdomain_visits(cpdomains2))