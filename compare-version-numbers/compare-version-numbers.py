class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1_list = version1.split('.')
        v2_list = version2.split('.')

        # Pad lists to be equal length
        if len(v1_list) > len(v2_list):
            v2_list += ['0']*(len(v1_list) - len(v2_list))
        if len(v2_list) > len(v1_list):
            v1_list += ['0']*(len(v2_list) - len(v1_list))

        # process list
        for i in range(len(v1_list)):

            if v1_list[i] == '':
                v1 = 0
            else:
                v1 = int(v1_list[i])

            if v2_list[i] == '':
                v2 = 0
            else:
                v2 = int(v2_list[i])

            if v1 > v2:
                return 1
            if v2 > v1:
                return -1

        return 0
 

A = Solution()

print A.compareVersion('1.2.1', '3.4') == -1
print A.compareVersion('1.9999', '1.100000') == -1
print A.compareVersion('3.1200', '03.4') == 1
print A.compareVersion('900.12', '3.99999') == 1
print A.compareVersion('1.0', '0.0') == 1
print A.compareVersion('1.12', '1.12') == 0
print A.compareVersion('1', '0') == 1
print A.compareVersion('1', '') == 1
print A.compareVersion('', '') == 0
print A.compareVersion('0', '0') == 0
print A.compareVersion('1.2.1', '1.2.1.0') == 0
print A.compareVersion('1.2.1', '1.2.1.0.1') == -1