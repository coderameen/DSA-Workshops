#Sort the array element by decreasing frequency
'''
Given an array of integer arr. sort the array according to the freqency/occrence of element i.e. element that have higher frequency comes first, if elment frequencies of two elements are same the smaller number comes fisrt


input:
arr = [5,5,4,6,4,5]
oput: [5,5,5,4,4,6]

input: arr = [5,5,4,6,4]
output: [4,4,5,5,6]


input: arr = [9,9,9,2,5]
ouput:[9,9,9,2,5]
'''
from collections import Counter
def sortByFrequency(arr):
    freq = Counter(arr)
    #sort by frequency(descending) and the element value (Ascending)
    sorted_arr = sorted(arr, key= lambda x:(-freq[x],x))
    return sorted_arr


arr = [5,5,4,6,4]
print(sortByFrequency(arr))#[4, 4, 5, 5, 6]


print("-----------------")
number = [1,2,3,4,5]
#each number double in a list [2, 4, 6, 8, 10]
# l = [] 
# for i in number:
#     l.append(i*2)
# print(l)
lst = [1,2,3,4,5]
double_arr = list(map(lambda x:x*2,lst))
print(double_arr)#[2, 4, 6, 8, 10]


l2 = [1,2,3,4,5,6,7]
#print only even elment
evens = list(filter(lambda x:x%2==0,l2))
print(evens)#[2, 4, 6]