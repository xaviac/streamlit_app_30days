# %%
import math

def plusMinus(arr: list) -> int:
    positive = []
    negative = []
    neutral = []
    for i in arr:
        if i > 0:
            positive.append(i)
        elif i < 0:
            negative.append(i)
        else:
            neutral.append(i)

    result = f'''
    Positive: {(len(positive) / len(arr)):.6f}
    Negative: {(len(negative) / len(arr)):.6f}
    Neutral: {(len(neutral) / len(arr)):.6f}
    '''

    return result


def plusNum(arr):
    # Write your code here
    positive = []
    negative = []
    neutral = []
    for i in arr:
        if i > 0:
            positive.append(i)
        elif i < 0:
            negative.append(i)
        else:
            neutral.append(i)

            
    result = f'''
    {(len(positive)/len(arr)):.6f}
    {(len(negative)/len(arr)):.6f}
    {(len(neutral)/len(arr)):.6f}
    '''
    
    return f'''
{(len(positive)/len(arr)):.6f}
{(len(negative)/len(arr)):.6f}
{(len(neutral)/len(arr)):.6f}
'''

if __name__ == '__main__':
    arr = [1, 1, 0, -1, -1]
    print(plusNum(arr))





# %%
