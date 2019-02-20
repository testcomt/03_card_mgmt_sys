# 1. Display welcome info
# 2. Display and capture user's choice
import cards_input
import cards_tools

# global variables
first_choice = ["0", "1", "2", "3"]
next_choice = ["m", "d"]
user_card_list = []


def query_a_card()->int:
    """return the card index, matching name queried"""

    name_input = input("请输入要查询的名字：")
    for this_user_dict in user_card_list:
        if name_input == this_user_dict["name"]:
            print("找到了！")
            return user_card_list.index(this_user_dict)
    else:
        print("没有找到！")
        return -1


def mod_a_card(card_index)->None:
    """modify a card (dict) info"""

    print("请输入更新后的名片信息：")
    user_card_list[card_index] = cards_input.create_a_card()
    print("名片信息已经更新")


def del_a_card(card_index)->None:
    """delete a card"""
    if card_index < len(user_card_list):
        del user_card_list[card_index]
        print("成功删除名片！")
    else:
        assert "deleting_card_index out of range!"


if __name__ == '__main__':
    while True:
        cards_tools.welcome_info()

        choice = input("请输入您想要进行的操作：")

        if choice not in first_choice:
            print("您输入的选项不正确！")

        elif choice == first_choice[0]:
            print("---退出系统成功！---")
            break

        elif choice == first_choice[1]:

            one_card_dict = cards_input.create_a_card()

            print("名片创建成功：")
            cards_tools.print_one_card(one_card_dict)

            user_card_list.append(one_card_dict)

        elif choice == first_choice[2]:
            print("共有%d张名片" % len(user_card_list))
            for card in user_card_list:
                cards_tools.print_one_card(card)

        else:
            find_card_index = query_a_card()
            if find_card_index != -1:
                cards_tools.print_one_card(user_card_list[find_card_index])

                user_next_choice = input("您要修改或删除该名片吗？m：修改；d：删除；其他：返回____")
                if user_next_choice == next_choice[0]:  # m:修改
                    mod_a_card(find_card_index)
                elif user_next_choice == next_choice[1]:  # d：删除
                    del_a_card(find_card_index)
                else:
                    print("返回上一级菜单！")


    print("感谢您使用【名片管理系统】！")
