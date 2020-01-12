import jwt


my_token = jwt.encode(
    {'the_key': 'the_value'},
    'the_secret'
)

print(my_token)

my_token = jwt.decode(my_token, 'the_secret')

print(my_token)
