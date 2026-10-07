def two_of_three(i, j, k):
    """Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k
    """
    return min(i*i+j*j, i*i+k*k, j*j+k*k)