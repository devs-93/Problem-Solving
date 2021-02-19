'''
First line contains L.
Second line contains N, number of photos.
Following N lines each contains two space separated integers W and H.
'''

L = int(input())
N = int(input())
for i in range(0, N):
    W, H = map(int,input().split(" "))
    if W < L or H < L:
        print('UPLOAD ANOTHER')
    elif W >= L and H >= L:
        if W == L and H == L:
            print('ACCEPTED')
        else:
            print('CROP IT')

