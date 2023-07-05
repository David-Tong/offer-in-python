class MaxQueue(object):

    def __init__(self):
        from collections import deque
        self.queue = deque()
        self.mono_queue = deque()

    def max_value(self):
        """
        :rtype: int
        """
        return self.mono_queue[0] if self.mono_queue else -1

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.queue.append(value)

        while self.mono_queue and self.mono_queue[-1] < value:
            self.mono_queue.pop()
        self.mono_queue.append(value)

    def pop_front(self):
        """
        :rtype: int
        """
        if not self.queue:
            return -1

        if self.queue[0] == self.mono_queue[0]:
            self.mono_queue.popleft()
        return self.queue.popleft()


"""
mq = MaxQueue()
mq.push_back(1)
mq.push_back(2)
print(mq.max_value())
print(mq.pop_front())
print(mq.max_value())
"""

"""
mq = MaxQueue()
print(mq.pop_front())
print(mq.max_value())
"""

mq = MaxQueue()
mq.push_back(1)
mq.push_back(2)
mq.push_back(3)
mq.push_back(5)
mq.push_back(3)
mq.push_back(1)
print(mq.max_value())
print(mq.pop_front())
print(mq.max_value())
print(mq.pop_front())
print(mq.pop_front())
print(mq.pop_front())
print(mq.pop_front())
print(mq.max_value())