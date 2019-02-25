#!/usr/local/bin/python3

# 1. Display welcome info
# 2. Display and capture user's choice

import cards_tools

__VERSION_TYPE = True  # True = OO, False = non-OO

if __VERSION_TYPE:
    import cards_input_oo as cards_input
else:
    import cards_input_non_oo as cards_input


# global variables define a tuple due to its unchangeable attribute
FIRST_CHOICE = ("0", "1", "2", "3")
NEXT_CHOICE = ("m", "d")
# create a Card instance, global
g_my_card = cards_input.Card()


def query_and_other_oper()->None:
    """query a card; modify this card del this card"""

    find_card_index = g_my_card.query_a_card()

    if find_card_index != -1:
        user_next_choice = input("您要修改或删除该名片吗？"
                                 "m：修改；d：删除；其他：返回____")
        if user_next_choice == NEXT_CHOICE[0]:  # m:修改
            g_my_card.mod_a_card(find_card_index)
        elif user_next_choice == NEXT_CHOICE[1]:  # d：删除
            g_my_card.del_a_card(find_card_index)
        else:
            print("返回上一级菜单！")


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
            g_my_card.create_a_card(cards_tools.get_card_input())

        elif choice == FIRST_CHOICE[2]:
            g_my_card.show_all_cards()

        else:
            query_and_other_oper()

    print("感谢您使用【名片管理系统】！")


