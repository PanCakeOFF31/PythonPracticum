import datetime


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
post_manual_weekday = create_new_post(initial_post, 'Tuesday')

print('initial_post:', initial_post)
print('post_with_weekday:', post_with_weekday)
print('post_manual_weekday:', post_manual_weekday)
