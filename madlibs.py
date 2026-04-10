with open ("story.txt","r") as f:
    story = f.read()

words = set()
start_of_word = -1

target_object_start = "<"
target_object_end = ">"

