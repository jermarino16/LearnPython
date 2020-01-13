'''
copy_and_reverse('story.txt', 'story_reversed.txt') # None
# expect the contents of story_reversed.txt to be the reverse of the contents of story.txt
'''

def copy_and_reverse(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()
        text = text[::-1]
        
    with open(new_file_name, "w") as file2:
        file2.write(text)