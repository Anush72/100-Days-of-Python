# Creating class
# Pascal Case for naming class

class User:
    # constructor
    # attributes - class have
    def __init__(self,user_id,user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0
    # method - class does
    def follow(self,user):
        user.followers += 1
        self.following += 1

user1 = User("001",'Anush')
user2 = User("002","Giri")
user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)

