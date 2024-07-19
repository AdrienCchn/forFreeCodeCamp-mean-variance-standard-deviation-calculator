import numpy as np

def calculate(list):
    # Convert the list to an array
    listToDescribe = np.array(list)

    # Exception message
    # I think it will be more relevant if the code raises the ValueError when the number of elements is different than 9, but I respect the exercise text.
    if len(listToDescribe) < 9:
        raise ValueError("List must contain nine numbers.")


    # Convert the list to a matrix
    myMatrix = listToDescribe.reshape(3, 3)
    
    # Enlist the options of the parameter axis of the calculation fonctions (np.mean, np.var...)
    myAxisList = (0, 1, None)
    
    # Initialisation of the lists which will contain the results
    meanList = [0,0,0]
    varList = [0,0,0]
    stdList = [0,0,0]
    maxList = [0,0,0]
    minList = [0,0,0]
    sumList = [0,0,0]
    
    # Calculations
    for idList, myWorkArea in enumerate(myAxisList):
        meanList[idList] = np.mean(myMatrix, axis=myWorkArea).tolist()
        varList[idList] = np.var(myMatrix, axis=myWorkArea).tolist()
        stdList[idList] = np.std(myMatrix, axis=myWorkArea).tolist()
        maxList[idList] = np.max(myMatrix, axis=myWorkArea).tolist()
        minList[idList] = np.min(myMatrix, axis=myWorkArea).tolist()
        sumList[idList] = np.sum(myMatrix, axis=myWorkArea).tolist()
    
    # Filling the dictionary
    calculations = {'mean': meanList, 'variance': varList, 'standard deviation': stdList, 'max': maxList, 'min': minList, 'sum': sumList}
    
    return calculations
