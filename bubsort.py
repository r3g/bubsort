def bubbleSort(arr):
  n = len(arr)

  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
          arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [62, 14, 256, 332, 2, 118, 63, 4, 600, 30, 77, 28, 99, 17, 333, 105, 25, 94, 90]

print("Pre-sorted array is: ")
for i in range(len(arr)):
  print ("{}".format(arr[i])),

bubbleSort(arr)

print ("\nSorted array is: ")
for i in range(len(arr)):
  print ("{}".format(arr[i])),
