gitimport random
import string

from data import CHOICE, CHOICES

score_system = 0
score_user = 0


def game():

    global score_system, score_user
    user = input("یکی از مقادیر سنگ، کاغذ، قیچی را واد کنید")

    if user not in CHOICES:
        print("مقداری که وارد کردید اشتباه است لطفا دوباره امتحان کنید")
        return game()

    system = random.choice(CHOICES)
    my_list = {user, system}
    print('انتخاب شما:', user)
    print('انتخاب رقیب:', system)

    if len(my_list) == 1:
        print('امتیاز شما: ', score_user, "امتیاز رقیب شما:", score_system)

    elif my_list in CHOICE.values():
        a = [k for k, v in CHOICE.items() if v == my_list][0]

        if user == a:
            score_user += 1
            print('امتیاز شما: ', score_user, "امتیاز رقیب شما:", score_system)

        elif system == a:
            score_system += 1
            print('امتیاز شما: ', score_user, "امتیاز رقیب شما:", score_system)


def sets():
    repeat = input('تمایل دارید چند ست بازی کنید؟')
    repeat_list = set(repeat[::])

    if repeat == '0':
        quit()

    elif repeat_list.issubset(string.digits):

        for i in range(int(repeat)):
            game()
        winner()

    else:
        print('لطفا مقدار معتبری را وارد کنید')
        sets()


def winner():
    if score_user > score_system:
        print("********** شما برنده شدید **********")

    elif score_user < score_system:
        print("********** رقیب برنده شد **********")

    else:
        print("مساوی شدید")
    play_again()


def play_again():
    again = input('تمایل دارید مجدد بازی کنید؟ بله / خیر ')
    if again == 'خیر':
        quit()
    elif again == 'بله':
        global score_system, score_user
        score_system = 0
        score_user = 0
        sets()
    else:
        print('لطفا مقدار معتبری را وارد کنید')
        return play_again()


if __name__ == '__main__':
    sets()
