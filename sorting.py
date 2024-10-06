nums1 = [3,6,9,8,7,2]
nums2 = [3,6,9,8,7,2]

def bubble_sort(nums1):
    for i in range(len(nums1)-1, 0, -1):
        for j in range(i):
            if nums1[j]>nums1[j+1]:
                temp = nums1[j]
                nums1[j] = nums1[j+1]
                nums1[j+1] = temp

def selection_sort(nums2):
    for i in range(len(nums2)-1):
        minPos = i
        for j in range(i, len(nums2)):
            if nums2[j]<nums2[minPos]:
                minPos = j

        temp = nums2[i]
        nums2[i] = nums2[minPos]
        nums2[minPos] = temp

# Selection sorting  is better than bubble sorting in performance

bubble_sort(nums1)
print(nums1)
selection_sort(nums2)
print(nums2)