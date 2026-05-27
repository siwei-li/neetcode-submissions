class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        n = len(s)
        cnt = 0
        t_counter = Counter(t)
        s_counter = defaultdict(int)
        ans = s + s

        for r_idx in range(n):
            if s[r_idx] in t_counter:
                c = s[r_idx]
                s_counter[c] += 1
                if s_counter[c] == t_counter[c]:
                    cnt += 1
                    while cnt == len(t_counter):
                        if len(s[l:r_idx + 1]) < len(ans):
                            ans = s[l:r_idx + 1]
                        if s[l] in s_counter:
                            s_counter[s[l]] -= 1
                            if s_counter[s[l]] < t_counter[s[l]]:
                                cnt -= 1
                        l += 1

        return ans if ans != s + s else ""