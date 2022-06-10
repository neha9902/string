story="this is Neha and I am learning python languauge"
print(story[0:5])

#String functions

print(len(story));
print(story.endswith("languauge"))
print(story.count("I"))
print(story.count("is"))  #-->2
print(story.count("neha"))
print(story.capitalize())
print(story.find("I"))  # 17
print(story.find("Neha")) 
print(story.find("is"))  #--> first occurrence
print(story.replace("Neha","Neha Bharti")) # replaces all the occurrence
