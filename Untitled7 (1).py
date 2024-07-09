#!/usr/bin/env python
# coding: utf-8

# In[3]:


def maxScore(cardPoints, k):
    n = len(cardPoints)
    # If k is equal to n, we take all cards, so return the sum of all cardPoints
    if k == n:
        return sum(cardPoints)
    
    # Calculate the sum of the first k cards
    window_sum = sum(cardPoints[:k])
    max_sum = window_sum
    
    # Sliding window approach to find the maximum sum of k cards
    for i in range(k-1, -1, -1):
        window_sum += cardPoints[n-(k-i)] - cardPoints[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum


# In[ ]:




