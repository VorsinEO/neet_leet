class MinStack:
    def __init__(self):

        self.min_val = [float("inf")]
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min_val[-1]:
            self.min_val.append(val)

    def pop(self) -> None:
        last = self.stack.pop()
        if last == self.min_val[-1]:
            self.min_val.pop()
        return last

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


def test_solution(my_sol_class):
    s = my_sol_class()
    s.push(-2)
    s.push(0)
    s.push(-3)
    r1 = s.getMin()
    r2 = s.pop()
    r3 = s.top()
    r4 = s.getMin()
    if (r1 == -3) & (r1 == -3) & (r1 == -3) & (r1 == -3):
        print("test success")
    else:
        print("test fail", r1, r2, r3, r4)


if __name__ == "__main__":
    test_solution(MinStack)
