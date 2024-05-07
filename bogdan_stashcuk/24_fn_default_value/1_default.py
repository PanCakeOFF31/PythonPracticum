import datetime


def mult_by_factor(value, multiplier=1):
    return value * multiplier


print(mult_by_factor(10), mult_by_factor(10, 2),
      mult_by_factor(value=10), mult_by_factor(10, multiplier=2))

print(datetime.datetime.today().strftime('%A-%HH'))


def get_weekday_now():
    return datetime.date.today().strftime('%A')


def create_new_post(post: dict, weekday: str = get_weekday_now()):
    post_copy = post.copy()
    post_copy['created_week_day'] = weekday
    return post_copy


initial_post = {
    'id': 143,
    'author': 'Igor',
}

post_with_weekday = create_new_post(initial_post)

print('initial_post:', initial_post)
print('post_with_weekday:', post_with_weekday)
