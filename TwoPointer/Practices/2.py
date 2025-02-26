# Weight lifting
# Ended
# Language:
# Python3
# Theme: Terminal
# Description
# Harry and John want to do a competition of weightlifting in which they can lift as many weights as they want. 
# There are N weights numbered f rom 1 to N where ith weight has a value weight[i].
#  We have to find the t otal weight lifted by both of them separately after the competition ends.
# Competition ends when all the weights have been lifted by them. The r ules of the game are as follows-

# 1. Harry will lift the weight from left to right and John will lift the weig ht from right to left.
# 2. Harry will start the game and in the first move he can only lift one weight i.e. weight[0].
# 3. After the first move, the players will play alternatively i.e. after the first move the John will lift, then again Harry boy and so on......
# 4. The boy will lift the least possible weight just greater than the wei ght lifted by the other boy in the previous move i.e. if one boy lifts weight equal to 8 in the previous turn, then the other boy has to li ft a weight greater than 8 (using one or more weights).

# Input
# The first line of input contains a single integer T, the number of test cas es.
# The first line of each test case contains N denoting the number of weig hts.
# The second line of each test case contains N space-separated integer weight[i] denoting the value of ith weight.
# Constraints
# 1 <= T <= 10
# 1 <= N <= 10^5
# Output
# The output must contain the total weightlifted by Harry and John respe ctively.

# 1
# 11
# 3 1 4 1 5 9 2 6 5 3 5