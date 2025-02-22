# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = defaultdict(int)
        for d in cpdomains :
            amount, domain = d.split()
            amount, n = int(amount), len(domain)
            for i in range(n-1,-1,-1) :
                if i ==0 :
                    domains[domain[i:]] += amount
                if domain[i] == ".":
                    domains[domain[i+1:]] += amount
        ans = []
        for i in domains :
            ans.append(f"{domains[i]} {i}")
        return ans