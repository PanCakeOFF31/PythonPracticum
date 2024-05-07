from helpers import print_section


def get_posts_info(name, posts_qty):
    info = f"{name} wrote {posts_qty} posts"
    return info


print_section("Позиционные аргументы")
print(get_posts_info('Maxim', '100'))

print_section("Keyword аргументы")
print(get_posts_info(posts_qty=100, name='Max'))
