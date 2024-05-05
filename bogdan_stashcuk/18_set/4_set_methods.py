from helpers import *

print_article()
print_section("Исходный множества:")

photo_sizes = {'1920x1080', '800x600'}
other_photo = {'800x600', '12024x768'}

print(photo_sizes)
print(other_photo)

print_section_ending()
print_section('union() __or__() |')

print(photo_sizes.union(other_photo))
print(photo_sizes | other_photo)

print_section_ending()
print_section('intersection() __and__() &')

print(photo_sizes.intersection(other_photo))
print(photo_sizes.__and__(other_photo))
print(photo_sizes & other_photo)

print_section_ending()
print_section('difference()')

print(photo_sizes.difference(other_photo))
print(photo_sizes - other_photo)

print_section_ending()
print_section('symmetric_difference() __xor__() ^')

print(photo_sizes.symmetric_difference(other_photo))
print(photo_sizes.__xor__(other_photo))
print(photo_sizes ^ other_photo)

print_section_ending()
print_article_ending()
