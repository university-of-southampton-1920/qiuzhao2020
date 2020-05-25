data = []
while(True):
    data.append(int(input()))
    if len(data)==(data[0]+1):
        break

def permutation(nums_all,position,end):
        if position==end:
            #print(nums_all)
            result.append(nums_all[:])
            #print(result)
        else:
            for i in range(position,end):
                nums_all[i],nums_all[position] = nums_all[position],nums_all[i]
                permutation(nums_all,position+1,end)
                nums_all[i],nums_all[position] = nums_all[position],nums_all[i]

def cal(arr):
    get = arr[0]
    maximum = 0
    minimum = 0
    for i in range(1,len(arr)):
        get = abs(get-arr[i])
        if get>maximum:
            maximum = get
        elif get<minimum:
            minimum = get
    return maximum,minimum
for d in data[1:]:
    result = []
    mx = 0
    mi = 0
    nums = [i for i in range(1,d+1)]
    permutation(nums,0,len(nums))
    print(result)
    for arr in result:
        maximum,minimum = cal(arr)
        if maximum>mx:
            mx = maximum
        elif minimum<mi:
            mi = minimum
    print(maximum,minimum)