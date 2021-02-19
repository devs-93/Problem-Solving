t = int(input())
while t != 0:
    num_of_play, num_of_mon = map(int, input().split(' '))
    rating_dict = {}
    final_rating = {}
    p = 0
    initial_rating = list(map(int, input().split(' ')))
    for i in range(0, num_of_play):
        list_of_rating = list(map(int, input().split(' ')))
        rating_dict[p] = list_of_rating
        p = p + 1
    print(rating_dict)
    dev=rating_dict
    i = 0
    f = 0
    rating = []
    flag=False
    while i != num_of_mon:
        p = 0
        while p != num_of_play:
            print(rating_dict[p], i, initial_rating[p])
            print(rating_dict[p][i], initial_rating[p],rating_dict[p][i]+initial_rating[p])
            print('---------->',dev[p],dev[p][i]+initial_rating[p])
            if flag==False:
                dev[p][i]=dev[p][i]+initial_rating[p]
                flag=True
            else:
                k=i-1
                print('99999999',dev[p][k])
                dev[p][i] = dev[p][i]+dev[p][k]

            print('@@@@@@@',dev)
            print('......................................')
            p = p + 1
        print("after change",dev)
        # final_rating[f]
        # f = f + 1

        i = i + 1

    t = t - 1
