class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        "We only need one variable for this easy question, lets turn it into a string since we are doing symbolic swaps"
        if x[0] == '-':
            """If it has a negative sign, we need to get rid of it"""
            x = x[1:]
            x = x[::-1]
            """ Then we need to reverse the numbers"""
            x = '-'+ x
            """Then add the negative sign back to the front"""
        else:
            x = x[::-1]
        x = int(x)
        if (x < -2147483648) or (x > 2147483647):
            """Double check it is actually an integer, and return nothing if not"""
            return 0
        return x
