# Write code below 💖

#in this lesson we learnt about 2 new file_io_methods, seek and truncate.
# seek is used to move the file cursor to a required location of the file.
# truncate is used to limit the file size to a specified limit

sent_message="Hey there vartika! tu badi gandi hai..."
unsent_message="Hey there vartika! Tu badi acchi hai yaar hehehehehehe..."
with open("sent_message.txt", 'w') as file:
  file.write(sent_message)

#read the file content and move the cursor the beginning by using seek(0)
with open('sent_message.txt','r+') as file:
  original_message=file.read()

  file.seek(0)
  #modify file size to the length of the unsent message
  file.truncate(len(unsent_message))
  file.write(unsent_message)

#print the original and modified message. now whenever we write to the file we will see the new message
print('Original message:', original_message)
print('Unsent message:', unsent_message)

