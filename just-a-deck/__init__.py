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

def checkForLength(item_list):
    '''
    This function tests for the length of a given list of items.
    Only lists containing 30 items are considered valid.
    >>> checkForLength(list(range(30)))
    True
    >>> checkForLength(list(range(29)))
    False
    '''
    if len(item_list) != 30:
        return False
    return True
