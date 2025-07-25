# Question 4


class UserProfile:
    def __init__(self, username, email, sign_up_date):

        self.username = username
        self.email = email
        self.sign_up_date = sign_up_date


class StandardUser(UserProfile):
    def __init__(self, username, email, sign_up_date, post_limit=2):
        super().__init__(username, email, sign_up_date)

        self.post_limit = post_limit
        self.post = []

    def create_post(self, content):

        self.post.append(Post(content))

        if len(self.post) >= self.post_limit:
            raise AttributeError(
                f"You've reached your limit. your limit is {self.post_limit}"
            )
        return


class PermiumUser(UserProfile):
    def __init__(self, username, email, sign_up_date, analytics, post_edit, post_limit):
        super().__init__(username, email, sign_up_date)

        self.analytics = analytics
        self.post_edit = post_edit
        self.post_limit = post_limit
        self.post = []

    def create_post(self, content):

        self.post.append(Post(content))


class Post:
    def __init__(self, content, number_of_likes=0, number_of_shares=0):

        self.content = content
        self.number_of_likes = number_of_likes
        self.number_of_shares = number_of_shares


stu = StandardUser("ariyan", "asb@email.com", "July 2025", 1)

pru = PermiumUser("ali", "ali@email.com", "july 2024", )

stu.create_post("Hello World")
stu.create_post("Hello World2")
# stu.create_post("Hello World3")

print(len(stu.post))


