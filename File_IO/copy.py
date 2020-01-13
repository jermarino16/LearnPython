'''
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''

def copy(old_name, new_name):
    with open(old_name) as file:
        data = file.read()
        
    with open(new_name, "w") as file2:
        file2.write(data)