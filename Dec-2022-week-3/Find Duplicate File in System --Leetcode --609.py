class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        answer = []
        for path in paths:
            temp = path.split(" ")
            path = temp[0]

            for content in temp[1:]:
                temp2 = content.split("(")
                hashMap[temp2[1][:-1]].append(path + "/" + temp2[0])

        for key in hashMap.keys():
            if len(hashMap[key]) > 1:
                answer.append(hashMap[key])
        return answer
