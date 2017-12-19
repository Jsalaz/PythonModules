'''
Created on Oct 8, 2017

@author: j_sal
'''
#from idlelib.pyshell import root
import sys

def sqrt(x):
    '''
    Compute square roots using the method of Heron of Alexandria.
    
    Args: 
        x: The number for which we find the square root
        
    Returns:
        The square root of x.
    '''
    
    if x < 0:
        raise ValueError("Can't compute square" 
                        "root of negative number {}".format(x))
    
    guess = x
    i = 0
    while guess * guess != x and i <20:
        guess = (guess + x / guess) / 2.0
        print(guess)
        i += 1
    return guess


def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
        print('This will not be printed.')
    except ValueError as e:
        print(e, file=sys.stderr)
        
    print('Program continues after try block.')


if __name__ == '__main__':
    main()