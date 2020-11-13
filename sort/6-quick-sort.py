#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

def quickSort(arr):
	def sort(arr, left, right):
		if left < right:
			pivotIndex = partition(arr, left, right)
			print(pivotIndex, arr, sep='=')
			sort(arr, left, pivotIndex - 1)
			sort(arr, pivotIndex + 1, right)
		return arr

	def partition(arr, left, right):
		"""经典分区：遍历数组元素，将小于 pivot 的元素放到左边，将大于 pivot 的元素放到右边"""
		pivot = left #左边为分区点
		j = pivot + 1
		for i in range(j, right + 1):
			if arr[i] < arr[pivot]: # >降序
				arr[i], arr[j] = arr[j], arr[i]
				j += 1
		# 最后交换基准数与指针停留位置(piovt在左边不用-1)
		arr[pivot], arr[j-1] = arr[j-1], arr[pivot]
		return j - 1

	return sort(arr, 0, len(arr)-1)

def quickSort_sft(arr):
	"""
	快速排序的基本思想：通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。
	"""
	if len(arr) < 2:
		return arr
	else:
		pivot = arr[0]
		# Space for time，数组比索引容易处理
		less = [i for i in arr[1:] if i <= pivot]
		greater = [i for i in arr[1:] if i > pivot]
	return quickSort_sft(less) + [pivot] + quickSort_sft(greater)

def main():
	# arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50 ,48]
	arr = [30, 40, 60, 10, 20, 50]
	ret = quickSort(arr)
	print(ret)

if __name__ == '__main__':
	main()
