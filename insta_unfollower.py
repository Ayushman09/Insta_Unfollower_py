#Instagram: "Unfollow-the Unfollowers" ~ Automation Script
#By: Ayushman Chakravarty (IndianPycoder)
#Dated: 05th Nov, 2019
#Purpose - Dealing with Unfollowers (RUDE)
#Note: This script will remove all ids, which doesn't follow you back!!


from InstagramAPI import InstagramAPI #pip install InstagramAPI

#login
USERNAME = input("Enter your Username: ")
PASS = input("Enter your password: ")

#fetch your followers
def getTotalFollowers(api, user_id): #Returns the list of followers of the user. It should be equivalent of calling api.getTotalFollowers from InstagramAPI
    followers = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers

#fetch users u follow following
def getTotalFollowings(api, user_id): #Returns the list of followers of the user. It should be equivalent of calling api.getTotalFollowers from InstagramAPI
    followers = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowings(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers


def nonFollowers(followers, followings):
    nonFollowers = {}
    dictFollowers = {}
    for follower in followers:
        dictFollowers[follower['username']] = follower['pk']

    for followedUser in followings:
        if followedUser['username'] not in dictFollowers:
            nonFollowers[followedUser['username']] = followedUser['pk']

    return nonFollowers

def unFollow(number: int):
    api = InstagramAPI(USERNAME, PASS)
    api.login()
    user_id = api.username_id
    followers = getTotalFollowers(api, user_id)
    following = getTotalFollowings(api, user_id)
    nonFollow = nonFollowers(followers, following)
    totalNonFollowers = len(nonFollow)
    print('Number of followers:', len(followers))
    print('Number of followings:', len(following))
    print('Number of nonFollowers:', len(nonFollow))

    for i in range(number):
        if i >= totalNonFollowers:
            break
        user = list(nonFollow.keys())[len(nonFollow) - 1]
        api.unfollow(nonFollow[user])
        nonFollow.pop(user)

if __name__ == "__main__":
    unFollow(27)
