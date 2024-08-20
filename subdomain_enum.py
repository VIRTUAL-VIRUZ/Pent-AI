
from sublist3r import sublist3r

class SubdomainEnumerator:
    def enumerate(self, url):
        subdomains = sublist3r.main(url, 40, savefile=None, ports=None, silent=True, verbose=False, enable_bruteforce=False, engines=None)
        return subdomains
