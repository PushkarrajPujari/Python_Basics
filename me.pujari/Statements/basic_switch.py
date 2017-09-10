# Simulating Switch statement in python using dict

def welcome():
    print("Hello , nice to meet you whats up")


def goodbye():
    print("Ok goodbye... , stay in touch good night")


def unknown():
    print("Sorry I didn't get you can you repeat")


switch = {
    "hi": welcome,
    "bye": goodbye,
    "": unknown
}

message = input("Enter your message")

switch[message]()


# we can also write it as follows

def f1(message):
    switch = {
        "hi": welcome,
        "bye": goodbye,
        "": unknown
    }[message]()


f1(input("Enter your message"))
