import common.validators as validators
import common

validators.json.is_json('{"name": "John", "age": 30}')
validators.date.is_date('2023-01-01')
validators.numeric.is_integer(10)

print('\\nn******* self *******')
for k in dict(globals()).keys():
    print(k)

print('\n\n******* common *******')
for k in common.__dict__.keys():
    print(k)


print('\n\n******* validators *******')
for k in validators.__dict__.keys():
    print(k)

print('\n\n******* numeric *******')
for k in validators.numeric.__dict__.keys():
    print(k)