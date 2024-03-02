# <<<<<<< Updated upstream
def max_solar_bulbs_sliding_window(bulb_sequence):
    # Add a '0' at the beginning and at the end of the sequence
    bulbs = ['0'] + list(bulb_sequence) + ['0']
    length = len(bulbs)
    
    # Use a sliding window of size 3 to find consecutive '0's and replace the middle one
    for i in range(1, length - 1):  # Start from 1 and end at length - 1 because of the added '0's
        if bulbs[i-1] == '0' and bulbs[i] == '0' and bulbs[i+1] == '0':
            bulbs[i] = '1'
    
    # Remove the added '0's at the beginning and the end
    bulbs = bulbs[1:-1]
    
    # Count the number of '1's in the final sequence
    return bulbs.count('1')

# Testing the function with the provided input
input_sequence = '0001'
result_count = max_solar_bulbs_sliding_window(input_sequence)
print(result_count)
# =======
def findminTrips(packageweight):
    weight_count={}
    for weight in packageweight:
        if weight in weight_count:
            weight_count[weight] +=1
        else:
            weight_count[weight] =1
    # print(weight_count)
    trips = 0
    for count in weight_count.values():
        if count == 1:
            return -1
        elif count %3 == 0:
            trips += count//3
        else:
            if count %2 == 0:
                trips += count//2
            else:
                trips +=1
                trips +=(count-2)//3
    return trips

# packageweight = [1,8,5,8,5,1,1]
# packageweight = [3,4,4,3,1]
# packageweight = [2,4,6,6,4,2,4]
packageweight = [4,4,6,6,4,4,4]
res = findminTrips(packageweight)
print(res)
# findminTrips([1,8,5,8,5,1,1])
# findminTrips([3,4,4,3,1])
# findminTrips([2,4,6,6,4,2,4])
# findminTrips([4,4,6,6,4,4,4])
