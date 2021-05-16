def findMedianSortedArrays(nums1, nums2):
    median = 0.0
                
    if not nums1 :
        if len(nums2) == 1 :
            median = float(nums2[0])

            return median

        if (len(nums2) % 2 == 0) :
            middle_num = len(nums2) // 2 - 1
            middle_num2 = middle_num + 1
            median = (nums2[middle_num] + nums2[middle_num2]) / 2
        else :
            middle_num = len(nums2) // 2 
            median = nums2[middle_num]
                        
    elif not nums2 :
        if len(nums1) == 1 :
            median = float(nums1[0])

            return median

        if (len(nums1) % 2 == 0) :
            middle_num = len(nums1) // 2 - 1
            middle_num2 = middle_num + 1
            median = (nums1[middle_num] + nums1[middle_num2]) / 2
            
        else :
            middle_num = len(nums1) // 2
            median = nums1[middle_num]
                        
    else :
        merged_list = nums1 + nums2
        merged_list.sort()
        
        if len(merged_list) == 1 :
            median = float(merged_list[0])

            return median
                    
        if (len(merged_list) % 2 == 0) :
            middle_num = len(merged_list) // 2 - 1
            middle_num2 = middle_num + 1
            median = (merged_list[middle_num] + merged_list[middle_num2]) / 2
        else :
            middle_num = len(merged_list) // 2
            median = merged_list[middle_num]
                        
    return median

print(findMedianSortedArrays([1,2],[3,4]))
print(findMedianSortedArrays([4,5,6,8,9], []))