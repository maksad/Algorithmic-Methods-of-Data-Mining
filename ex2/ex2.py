# '''
# ex 2
# '''

# import random
# from scipy import stats
# print('----------------', random.random())

# def get_x():
#     x = []
#     for i in range(10):
#         uniform = stats.uniform()
#         sample = round(stats.uniform().rvs(1)[0], 3)
#         x.append(sample)
#     return x

# def get_max(x):
#     max_num = -1
#     for i in X:
#         if max_num < i:
#             max_num = i
#     return max_num

# X = get_x()
# max_num = get_max(X)

# print('X', X)
# print('max_num', max_num)

'''
ex 3
'''

# An efficient Python3 program
# to randomly select k items
# from a stream of items
import random
# A function to randomly select
# k items from stream[0..n-1].
def selectKItems(stream, n, k):
        i=0;

        # reservoir[] is the output
        # array. Initialize it with
        # first k elements from stream[]
        reservoir = [0]*k;
        for i in range(k):
            reservoir[i] = stream[i];

        # Iterate from the (k+1)th
        # element to nth element
        print('\nreservoir')
        print(reservoir)
        while(i < n):
            # Pick a random index
            # from 0 to i.
            j = random.randrange(i+1);

            # If the randomly picked
            # index is smaller than k,
            # then replace the element
            # present at the index
            # with new element from stream
            if(j < k):
                reservoir[j] = stream[i];
            i+=1;
            print(reservoir);

        print("\nFollowing are k randomly selected items");
        print(stream);
        print(reservoir);

# Driver Code

stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
n = len(stream);
k = 5;
selectKItems(stream, n, k);

# This code is contributed by mits
