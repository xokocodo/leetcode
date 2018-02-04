class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1_major_str, v1_minor_str = version1.split('.')
        v2_major_str, v2_minor_str = version2.split('.')

        v1_major = int(v1_major_str)
        v2_major = int(v2_major_str)

        # Remove trailing 0's on minor
	v1_minor = v1_minor_str.split('0')[0]
	v2_minor = v2_minor_str.split('0')[0]

        if v1_minor == '':
	    v1_minor = 0
        else:
            v1_minor = int(v1_minor)

        if v2_minor == '':
	    v2_minor = 0
        else:
            v2_minor = int(v2_minor)

        if v1_major > v2_major: return 1
        elif v1_major < v2_major: return -1
        else:
            if v1_minor > v2_minor: return 1
            elif v1_minor < v2_minor: return -1
            else: return 0          

A = Solution()

print A.compareVersion('1.12', '3.4') == -1
print A.compareVersion('1.9999', '1.100000') == 1
print A.compareVersion('3.1200', '03.4') == 1
print A.compareVersion('900.12', '3.99999') == 1
print A.compareVersion('1.0', '0.0') == 1
print A.compareVersion('1.12', '1.12') == 0