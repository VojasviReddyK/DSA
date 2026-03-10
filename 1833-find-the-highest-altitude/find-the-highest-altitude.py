class Solution(object):
    def largestAltitude(self, gain):
        altitude_array = [0]
        current_altitude = 0
        for i in gain:
            current_altitude += i
            altitude_array.append(current_altitude)
        return max(altitude_array)
obj=Solution()
print(obj.largestAltitude([-5,1,5,0,-7]))
            

