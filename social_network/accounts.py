class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []

    def add_post(self, post):
        self.posts.append(post)
        post.user = post.set_user(self)

    def get_timeline(self):
        timeline = []
        for followed in self.following:
            timeline += followed.posts
        #I didn't get this and had to look at the answer, which I do understand.
        return sorted(timeline, key=lambda x: x.timestamp, reverse=False)

    def follow(self, other):
        self.following.append(other)
