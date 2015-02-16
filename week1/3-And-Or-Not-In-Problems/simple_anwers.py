text = input("Say something: ")
text = text.lower()

if "hello" in text:
    print("Hello there")
elif "how are you?" in text:
    print("I am fine, thanks. How are you?")
elif "feelings" in text:
    print("I am a machine. I have no feelings")
elif "age" in text:
    print("I have no age. Only current timestamp")
else:
    print("I did't get that")
    
