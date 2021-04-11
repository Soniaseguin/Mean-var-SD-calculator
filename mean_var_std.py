import numpy as np
list=[1,2,3,4,5,6,7,8,9]
def calculate(list):
  arr = np.reshape(list,(3,3))
  calculations ={
    'mean' : [np.mean(arr, axis=1), np.mean(arr,axis=0), np.mean(arr)], 
    'variance' : [np.var(arr,axis=1), np.var(arr,axis=0), np.var(arr)],
    'standard deviation': [np.std(arr,axis=1), np.std(arr,axis=0), np.std(arr)], 
    'max': [np.max(arr, axis=1), np.max(arr,axis=0), np.max(arr)], 
    'min': [np.min(arr, axis=1), np.min(arr, axis=0), np.min(arr)],
    'sum': [np.sum(arr,axis=1), np.sum(arr,axis=0), np.sum(arr)] 
  }
  print(calculations)

  return calculations

""""
1 convert the list into a 3 x 3 Numpy array,
2 return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.
{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]

 4 - CHECK RAISE ERROR
  If a list containing less than 9 elements is passed into the function, it should raise a ValueError exception with the message: "List must contain nine numbers." The values in the returned dictionary should be lists and not Numpy arrays.
}"""