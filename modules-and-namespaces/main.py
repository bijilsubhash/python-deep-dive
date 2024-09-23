import common
import common.validators as validators
import common.models as models
import common.helpers as helpers

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

print('\n\n******* posts (package) *******')
for k in common.models.posts.__dict__.keys():
    print(k)

print('\n\n******* users (package) *******')
for k in common.models.users.__dict__.keys():
    print(k)

john_post = models.Post()
john_posts = models.Posts()
john = models.User()

calc = helpers.Calc()
print(helpers.factorial(5))
helpers.say_hello()

import asyncio
import email