import requests

headers = {'Authorization': 'Token token=7662c59d6086d0e8a5d528bb17a58c06'}  # token


# create new user
def test_create_new_user():
    body1 = {
        "user": {
            "login": "Thgjghjghj",
            "email": "teshgjt@mail.com",
            "password": "123456"
        }
    }

    response1 = requests.post('https://favqs.com/api/users', json=body1, headers=headers)
    print(response1.text)
    print(response1.status_code)


# Change the user
def test_change_the_user():
    body2 = {
        "user": {
            "login": "Newlrtyogin",
            "email": "testrtyrtyil@.com",
            "password": "123456",
            "twitter_username": "twitter_username_here1",
            "facebook_username": "facebook_username_here2",
            "pic": "twitter",
            "profanity_filter": "false"
        }
    }
    response2 = requests.put('https://favqs.com/api/users/TestLogin', json=body2, headers=headers)
    print(response2.text)
    print(response2.status_code)


test_create_new_user()
test_change_the_user()
