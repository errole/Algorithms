class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # This will store indices of the temperatures list

        for i in range(n - 1, -1, -1):
            current_temp = temperatures[i]
            # Pop elements from the stack until we find a warmer temperature
            while stack and temperatures[stack[-1]] <= current_temp:
                stack.pop()

            if stack:
                answer[i] = stack[-1] - i  # Calculate the number of days to wait
            else:
                answer[i] = 0  # No warmer temperature found

            stack.append(i)  # Push the current index onto the stack

        return answer
    
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1  # On day 1, one person knows the secret
        total_sharers = 0  # Total number of people who can share the secret

        for day in range(2, n + 1):
            # New people who learn the secret today
            if day - delay >= 1:
                total_sharers = (total_sharers + dp[day - delay]) % MOD
            # People who forget the secret today
            if day - forget >= 1:
                total_sharers = (total_sharers - dp[day - forget] + MOD) % MOD
            
            dp[day] = total_sharers

        # Sum up all people who still remember the secret on day n
        result = sum(dp[max(1, n - forget + 1):n + 1]) % MOD
        return result
    
class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()