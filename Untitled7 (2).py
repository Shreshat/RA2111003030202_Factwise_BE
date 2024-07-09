#!/usr/bin/env python
# coding: utf-8

# In[4]:


def maxScore(cardPoints, k):
    n = len(cardPoints)
    if k == n:
        return sum(cardPoints)
    
    window_sum = sum(cardPoints[:k])
    max_sum = window_sum
    
    for i in range(k-1, -1, -1):
        window_sum += cardPoints[n-(k-i)] - cardPoints[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Ex 1:
cardPoints1 = [1, 2, 3, 4, 5, 6, 1]
k1 = 3
print(f"Example 1: Maximum score = {maxScore(cardPoints1, k1)}")

# Ex 2:
cardPoints2 = [2, 2, 2]
k2 = 2
print(f"Example 2: Maximum score = {maxScore(cardPoints2, k2)}")

# Ex 3:
cardPoints3 = [9, 7, 7, 9, 7, 7, 9]
k3 = 7
print(f"Example 3: Maximum score = {maxScore(cardPoints3, k3)}")


# In[ ]:




