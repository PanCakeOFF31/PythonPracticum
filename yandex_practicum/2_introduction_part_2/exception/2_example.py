def calc_share(apples: int, friends: str) -> float:
    try:
        friends_number = int(friends.split(' ')[0])
        return round(apples / friends_number, 2)
    except ValueError:
        return apples
    except ZeroDivisionError:
        return 0


friend_list = ['7 друзей', '2 друга', '0 друзей', 'один враг']
apples = 17
for friend in friend_list:
    calculated = calc_share(apples, friend)
    print(f'Если разделить {apples} яблок на  {friend}, по каждый получит по: {calculated}')
