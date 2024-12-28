class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(f"{self.username}'s Timeline: ")
        for i, post in enumerate(self.posts, start=1):
            print(f"{i}. {post}")
    
    
def main():
    user=SocialMediaProfile("Johndoe")

    user.add_post("Hello World!")
    user.add_post("What's up?")

    user.display_timeline()

main()

