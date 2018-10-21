class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Setup mask of bits, can't use tilde as python uses signed :-/
        mask = (1 << num.bit_length()) - 1
        return num ^ mask
