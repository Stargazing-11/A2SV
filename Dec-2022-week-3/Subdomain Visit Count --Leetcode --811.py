from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashMap = defaultdict(int)
        answer = []
        for domain in cpdomains:
            visit = int(domain.split(" ")[0])
            temp = domain.split(" ")[1].split(".")

            for index, subD in enumerate(temp):
                hashMap[".".join(temp[index:])] += visit

        for key in hashMap.keys():
            answer.append(str(hashMap[key]) + " " + key)
        return answer
