import requests

headers = {'Authorization': 'Token token=1912a3978ce2de40e920188a7f3b2a2a'}  # token


# create new user
def test_create_new_user():
    body1 = {
        "user": {
            "login": "Wtethgf",
            "email": "tcvffgh@mahhgffy.com",
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
            "login": "NvcWecgfn",
            "email": "vfbhnx@bbf.com",
            "password": "123456",
            "twitter_username": "twitt",
            "facebook_username": "faceb",
            "pic": "twighr",
            "profanity_filter": "false"
        }
    }
    response2 = requests.put('https://favqs.com/api/users/TestLogin', json=body2, headers=headers)
    print(response2.text)
    print(response2.status_code)


test_create_new_user()
test_change_the_user()
