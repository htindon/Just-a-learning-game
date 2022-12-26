def checkForDuplicates(listToTest):
    '''
    This function tests for duplicates in a given list of items.

    >>> checkForDuplicates([2, 1, 2])
    False
    >>> checkForDuplicates([1, 2, 3])
    True    
    '''
    if len(listToTest) != len(set(listToTest)):
        return False
    return True
