def find_longest_consecutive_sequence(nums):
    nums_set = set(nums)
    longest_sequence = 0
    first_num = 0

    for num in nums:
        if num - 1 not in nums_set:
          current_num = num
          sequence_length = 1

        while current_num + 1 in nums_set:
            current_num += 1
            sequence_length += 1

            if longest_sequence < sequence_length:
                longest_sequence = sequence_length
                first_num = num
        
    return longest_sequence

array = [100,4,200,1,3,2]
print(find_longest_consecutive_sequence(array))
