# Create User Class
class User:
    # class attributes
    posts = []

    # add specified instance attributes
    def __init__(self, name, email, drivers_license):
        self.Name = name
        self.Email = email
        self.Drivers_license = drivers_license
        self.User_posts = []

    # print string representation of objects
    def __repr__(self):
        return(f"All Posts: {User.posts} | User's Posts: {self.User_posts}") #I CHANGED PRINT TO RETURN#

    # instance method to create user post
    def create_a_post(self):
        title = input("Please enter post title: ")
        content = input("Please enter post content: ")
        id = int(len(User.posts) + 1) 
        new_post_dict = {id: [title, content]} 
        User.posts.append(new_post_dict)
        self.User_posts.append(new_post_dict)
        print("Posted Successfully!")

     # print all class posts
    def see_all_posts(self):
        if len (User.posts) > 0:
            print(f"{User.posts}")
        else:
            return None

    # print single instance user's posts, NOT all posts
    def see_my_posts(self):
        if len (self.User_posts) > 0:
            print(f"{self.User_posts}")
        else:
            return None


    def delete_a_post(self):
        deleted_post = None #INSTEAD OF EMPTY LIST
        # deleting by title
        # title = input("Please enter post title you want to delete: ")
        #DELETE BY ID INSTEAD#
        id_to_delete = int(input("Please enter post ID you want to delete: "))
        
        try:
            # loops through User.posts and appends the deleted post to deleted_post variable
            for i in range(len(User.posts)):
                #if title and object title matches
                if list(User.posts[i].keys())[0] == id_to_delete: #THIS IS CHANGED
                    if User.posts[i] in self.User_posts: #THIS IS CHANGED make sure user owns post
                        deleted_post=(User.posts[i])
                        break
            #DELETED TO ADD TO BELOW ELSE STATEMENT
            # if len(deleted_post) == 0:
            #     print("Post Doesn't Exist")
            # actually deletes post from class and instance variable
            # for item in deleted_post: #dont need
            #IF DELETED POST EXISTS#
            if(deleted_post):
                User.posts.remove(deleted_post)
                self.User_posts.remove(deleted_post)
                print("Post Deleted Successfully") #PRINT("") IF U WANT TO PASS TEST
            else:
                print("Post Doesn't Exist")
        except ValueError:
            #DONT NEED
            # User.posts.append(deleted_post)
            # self.User_posts.append(deleted_post)
            print("Can't Delete Someone Else's Post")
            
# input = iter(["Johns †i†le", "I Just joined OOPX"])
# user = User("John", "john@email.com", "FDUI87")
# user2 = User("Jason", "jason@email.com", "12345")
# user.create_a_post() 
# user2.create_a_post()
# user.see_my_posts() 
# user.see_all_posts() 
# user.delete_a_post()
# user.see_all_posts()

# FAILED test_User.py::test_delete_post - AssertionError: assert 1 == 0
# FAILED test_User.py::test_see_all_posts - AssertionError: assert 1 == 0
# FAILED test_User.py::test_see_my_posts - AssertionError: assert 1 == 3

#DEBUG STUFF
# user = User("John", "john@email.com", "FDUI87")
# user2 = User(**{"name":"Mike", "email":"mike@email.com", "drivers_license":"FDUI87"})
# user3 = User(**{"name":"Zack", "email":"zack@email.com", "drivers_license":"FDUI87"}) 
# user.create_a_post()
# print(len(user.posts))# 1
# print(len(user.User_posts))# == 1
# user.see_my_posts()
# user.delete_a_post()
# print(len(user.posts))# == 0
# print(len(user.User_posts))# == 0
# user.see_my_posts()
# # print("user see all posts")
# user.see_all_posts()
# user3.create_a_post()
# print(len(user3.User_posts))# == 1
# print(len(user.posts))# == 1
# user2.create_a_post()
# user.create_a_post()
# user.create_a_post()
# print(user.User_posts)
# print(len(user.User_posts))# == 2
# print(user.posts)
# print(len(user.posts))# == 4