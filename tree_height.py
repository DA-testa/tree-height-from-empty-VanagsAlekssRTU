# python3

import sys
import threading


def compute_height(n, parents):
    max_height = 0
    height = [1] * n
    viewed = {}

    for i, nodes in enumerate(parents):
        node = int(nodes)

        if node in viewed:
            height[i] = height[viewed[node]]
            continue
        if node != -1:
            viewed[node] = parents.index(node)
        
        while node != -1:
            height[i] += 1
            node = parents[node]

    return max(height)


def main():

    choice = input().strip().upper()
    
    if choice == "I":
        n = int(input())
        parents = input().split()
        height = compute_height(n, parents)
        print (height)
    elif choice == "F":
        # path example -> ./test/01
        path = input()
        if "a" in path:
            print("Invalid input") 
        else:
            with open(path, 'r') as f:
                n = int(f.readline().strip())
                parents = [int(x) for x in f.readline().strip().split(" ")]
            height = compute_height(n, parents)
            print (height)
    else: 
        print("Invalid input")
        main()


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
