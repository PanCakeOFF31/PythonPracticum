s = 'spammer'
offset = s.find('am')
print(offset, s[offset:])

mutated = s.replace('am', 'AM...')
print(s, '->', mutated)

ugly = 'aaa, bbb, ccc, zzz'
formatted = ugly.split(sep=', ', maxsplit=2)
print(ugly, '->', formatted)
formatted = ugly.rsplit(sep=', ', maxsplit=2)
print(ugly, '->', formatted)

to_upper = s.upper()
to_lower = s.lower()
print(s, '->', to_upper, '->', to_lower)

unformed = '    PanCakeOFF    '
print(unformed, '"', unformed.strip(), '"', '"', unformed.lstrip(), '"', '"', unformed.rstrip(), '"', sep='')

# string formatting
print('%s %s' % ('Maxim', 'Blinov'))
print('%s %s'.format('maxim', 'blinov'))
