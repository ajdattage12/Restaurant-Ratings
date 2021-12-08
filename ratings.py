"""Restaurant rating lister."""


open_file = open('scores.txt')


def score_compiler(file):
    dict = []
    for i in file:
        values = i.split(':')
        name = values[0]
        rating = values[1].strip()
        dict.append({'name': name,
                     'rating': rating})
    return dict


score_dict = score_compiler(open_file)
open_file.close()


def sorted_loop(dict):
    loop_listed = []
    for i in dict:
        name = i.get('name')
        rating = i.get('rating')
        loop_listed.append(f"{name} is rated at {rating}.")
    return sorted(loop_listed)


def user_access(dict):
    while True:
        user_input = input("What would you like to do?\n")
        if (user_input == 'add'):
            name = input("What's the name of the resturant?\n")
            rating = int(input("How would you rate it?\n"))
            dict.append({'name': name,
                        'rating': rating})
            looper = sorted_loop(dict)
            for i in looper:
                print(i)
        elif(user_input == 'view'):
            looper = sorted_loop(dict)
            for i in looper:
                print(i)
        elif(user_input == 'exit'):
            print("Ok, bye!\n")
            break
        else:
            print("Invalid input. Please try again.\nType one of the following options: 'view', 'add', or 'exit'\n")


user_access(score_dict)
