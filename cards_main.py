#!/usr/local/bin/python3

# 1. Display welcome info
# 2. Display and capture user's choice
import cards_input
import cards_tools

# global variables define a tuple due to its unchangeable attribute
FIRST_CHOICE = ("0", "1", "2", "3")


if __name__ == '__main__':
    while True:
        cards_tools.welcome_info()

        choice = input("请输入您想要进行的操作：")

        if choice not in FIRST_CHOICE:
            print("您输入的选项不正确！")

        elif choice == FIRST_CHOICE[0]:
            print("---退出系统成功！---")
            break

        elif choice == FIRST_CHOICE[1]:
            cards_input.new_card()

        elif choice == FIRST_CHOICE[2]:
            cards_input.show_all_cards()

        else:
            cards_input.query_and_other_oper()

    print("感谢您使用【名片管理系统】！")
