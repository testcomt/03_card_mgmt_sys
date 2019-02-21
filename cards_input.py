# Deal with user's choices
# 1. create a card
# 2. Display all cards
# 3. Query one card (3.1 modify card; 3.2 del a card)

import cards_tools

# record all cards info, each list item is a dict
user_card_list = []
next_choice = ["m", "d"]
CARD_FIELD = ["name", "tel", "qq", "mail"]


# TODO [0 - learning related]: still unsure how can I write this style of codes (3 separate small funcs
#  instead of one long func as the video does)


def get_card_input_imd()->list:
    """Obtain user's input for his card return a card info list not checking
    correctness _imd - intermediate function, won't be called by main func
    """

    # TODO [2 - prod optimization]: name is main index, shouldn't be duplicated
    # tel and qq should be digital numbers and within a certain range
    # mail should abide by mail rules

    name = input("姓名：")
    tel = input("电话：")
    qq = input("QQ: ")
    mail = input("邮件：")

    return [name, tel, qq, mail]


def create_a_card_imd()->dict:
    """create a card dict based on user's input return a card dict"""

    return dict(zip(CARD_FIELD, get_card_input_imd()))


def new_card()->None:
    """user creates a new card"""

    one_card_dict = create_a_card_imd()

    print("名片创建成功：")
    cards_tools.print_one_card(one_card_dict)

    user_card_list.append(one_card_dict)


def print_table_title_imd():
    """print card title"""

    print("-" * 100)
    for field in CARD_FIELD:
        print("", end="\t")

        # TODO [1 - code optimization]: names can't be over 14 characters, now

        print(field.ljust(10), end="\t")
        # why "\t\t" doesn't work?
        # print(field, end="\t\t")
    print("")
    print("-" * 100)


def show_all_cards()->None:
    """show all cards info"""

    print("\n共有%d张名片" % len(user_card_list))
    if len(user_card_list) == 0:
        print('您可以使用"新建名片功能"创建名片\n')
        return

    print_table_title_imd()

    i = 1
    for card in user_card_list:
        print("%d." % i, end="\t")
        cards_tools.print_one_card_values(card)
        i += 1
    # don't add \n here, 'cause a return will be added by default
    print("")


def query_a_card_imd()->int:
    """return the card index, matching name queried"""

    name_input = input("请输入要查询的名字：")
    for this_user_dict in user_card_list:
        if name_input == this_user_dict["name"]:
            print("找到了！")
            return user_card_list.index(this_user_dict)
    else:
        print("没有找到！")
        return -1


def mod_a_card_imd(card_index)->None:
    """modify a card (dict) info

    Args:
        card_index: which card to be modified [list index]
    """

    # TODO [3 - req related]: should name be allowed to modify?

    print("请输入更新后的名片信息：")

    current_dict = user_card_list[card_index]
    # only update the field when it is not NULL
    updated_dict = create_a_card_imd()
    for item in CARD_FIELD:
        if updated_dict[item] != "":
            current_dict[item] = updated_dict[item]

    print("名片信息已经更新")


def del_a_card_imd(card_index)->None:
    """delete a card

    Args:
        card_index: which card to be deleted
    """
    if card_index < len(user_card_list):
        del user_card_list[card_index]
        print("成功删除名片！")
    else:
        print("传入的名片索引错误！")
        assert "deleting_card_index out of range!"


def query_and_other_oper()->None:
    """query a card; modify this card del this card"""

    find_card_index = query_a_card_imd()
    if find_card_index != -1:
        cards_tools.print_one_card(user_card_list[find_card_index])

        user_next_choice = input("您要修改或删除该名片吗？"
                                 "m：修改；d：删除；其他：返回____")
        if user_next_choice == next_choice[0]:  # m:修改
            mod_a_card_imd(find_card_index)
        elif user_next_choice == next_choice[1]:  # d：删除
            del_a_card_imd(find_card_index)
        else:
            print("返回上一级菜单！")
