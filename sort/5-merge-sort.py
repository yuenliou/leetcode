#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

def mergeSort(arr):

	def mergeSortUp2Down(arr, left, right):
		"""递归从上往下"""
		if left >= right: return
		middle = (left + right) // 2
		mergeSortUp2Down(arr, left, middle)
		mergeSortUp2Down(arr, middle+1, right)
		merge(arr, left, middle, right)

	def mergeSortDown2Up(arr, left, right):
		"""循环从下往上"""
		def mergeGroups(arr, gap):
			length = len(arr)
			i = 0
			while i + 2*gap - 1 < length:
				# print(gap, i, i + gap - 1, i + 2*gap - 1, sep='=')
				merge(arr, i, i + gap - 1, i + 2*gap - 1)
				i += 2*gap
			if i + gap - 1 < length - 1:
				merge(arr, i, i + gap - 1, length - 1)

		gap = 1
		while gap < len(arr):
			mergeGroups(arr, gap)
			gap *= 2

	# mergeSortUp2Down(arr, 0, len(arr)-1)
	mergeSortDown2Up(arr, 0, len(arr)-1)

	return arr

def merge(arr, left, middle, right):
	"""C/C++ 思维编码"""
	result = [0] * (right - left + 1)
	i, j, k = left, middle + 1, 0
	while i <= middle and j <= right:
		if arr[i] <= arr[j]:
			result[k] = arr[i]
			i += 1
		else:
			result[k] = arr[j]
			j += 1
		k += 1
	while i <= middle:
		result[k] = arr[i]
		i += 1
		k += 1

	while j <= right:
		result[k] = arr[j]
		j += 1
		k += 1

	# print(result, i, j)
	for idx in range(k):
		arr[left + idx] = result[idx]

def mergeSort_sft(arr):
	"""
	工作原理：归并排序是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为2-路归并。
    编码要素：1.自上而下的递归，合并有序列表，2.从下往上的归并排序
	"""
	length = len(arr)
	if length < 2: return arr

	middle = length // 2
	left = arr[:middle]
	right = arr[middle:]
	# Space for time，数组比索引容易处理
	return merge_sft(mergeSort_sft(left), mergeSort_sft(right))

def merge_sft(left, right):
	"""合并有序列表"""
	result = []
	while len(left) > 0 and len(right) > 0:
		if left[0] <= right[0]:
			result.append(left.pop(0))
		else:
			result.append(right.pop(0))
	while len(left):
		result.append(left.pop(0))
	while len(right):
		result.append(right.pop(0))
	return result

def main():
	arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50 ,48]
	# arr = [10, 5, 2, 3]
	ret = mergeSort(arr)
	print(ret)

if __name__ == '__main__':
	main()
