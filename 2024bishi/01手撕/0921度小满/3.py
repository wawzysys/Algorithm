class MyQueue:
    def __init__(self):
        # 初始化两个栈，stack1用于入队操作，stack2用于出队操作
        self.stack1, self.stack2 = [], []

    def push(self, node) -> None:
        # 将元素压入stack1，所有入队操作都在stack1中进行
        self.stack1.append(node)

    def pop(self):
        # 调用peek方法获取队列前端的元素，并从stack2中弹出
        # 这样做是为了确保弹出的元素是"最早"加入的元素，即队列的前端
        peek = self.peek()
        self.stack2.pop()
        return peek

    def peek(self):
        # 如果stack2非空，说明之前已有元素从stack1转移到了stack2中
        # 因此直接返回stack2的栈顶元素，即队列的前端元素
        if self.stack2:
            return self.stack2[-1]
        # 如果stack2为空，首先检查stack1是否也为空
        if not self.stack1:
            return -1  # 如果两个栈都为空，返回-1（可以视为队列为空的标志）
        # 将stack1中所有元素弹出并压入stack2，使得最早加入stack1的元素位于stack2的栈顶
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        # 返回stack2的栈顶元素，即队列的前端元素
        return self.stack2[-1]
