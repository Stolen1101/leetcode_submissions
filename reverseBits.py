class Solution:
    def reverseBits(self, n: int) -> int:
        n = format(n, 'b').zfill(32) #Turn into binary string, padded to 32 bits as specified
        n = n[::-1] #Reverse string of bits
        n = int(n, base = 2) #return to integer
        return n
        