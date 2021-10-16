s = input()
if "," in s:
    print("сложное", end = " ")
if "!" in s and "?" in s:
    print("вопросительно-восклицательное")
elif "!" in s:
    print("восклицательное")
elif "?" in s:
    print("вопросительное")
else:
    print("повествовательное")
