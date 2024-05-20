job = ['developer', 'manager']

record = {
    'name': {
        'first': 'Bob',
        'last': 'Smith'
    },
    'job': job,
    'age': 40.5,
}

print('record:', record)

# Независимое изменение вложенного списка
job.append('homeworker')
print('record:', record)
