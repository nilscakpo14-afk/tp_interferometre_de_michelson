import numpy as np
import math as m

def uncertainty_A(A): 
    """
    calcul of the uncertity of a quantity with multiple mesurements in array A

    A (array)

    mean_A (float): mean of the array A

    sigma_A (float): standard deviation of the arry A

    u_A (float): uncertity of the mean_A
    """
    mean_A = np.mean(A)

    sigma_A = np.std(A, ddof = 1)

    u_A = sigma_A/m.sqrt(len(A))

    return mean_A, sigma_A, u_A

def relative_difference(A_th, A_exp):
    """
    calcul of the relative difference between theorical and experimental value of A 
    
    A_th (float): theorical value of A

    A_exp (float): experimental value of A
    """
    return abs(A_exp-A_th)/A_th

