class FreqStack:

    def __init__(self):
        self.freq_map = {}
        self.freq_group = {}
        self.max_freq = 0

    def push(self, val: int) -> None:

        cur_freq = 1
        if val in self.freq_map:
            cur_freq = self.freq_map[val] + 1
        self.freq_map[val] = cur_freq

        self.max_freq = max(self.max_freq, cur_freq)

        if cur_freq in self.freq_group:
            self.freq_group[cur_freq].append(val)
        else:
            self.freq_group[cur_freq] = [val]

    def pop(self) -> int:

        num = self.freq_group[self.max_freq].pop()
        self.freq_map[num] -= 1

        if len(self.freq_group[self.max_freq]) == 0:
            self.max_freq -= 1

        return num


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
