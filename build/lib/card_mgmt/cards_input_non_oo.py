# Deal with user's choices
# 1. create a card
# 2. Display all cards
# 3. Query one card (3.1 modify card; 3.2 del a card)

from card_mgmt import cards_tools

g_user_card_list = []
NEXT_CHOICE = ("m", "d")
CARD_FIELD = ("name", "tel", "qq", "mail")


# TODO [0 - learning related]: still unsure how can I write this style of codes (3 separate small funcs
#  instead of one long func as the video does)


def create_a_card_imd()->dict:
    """create a card dict based on user's input return a card dict"""
    return dict(zip(CARD_FIELD, cards_tools.get_card_input()))


def new_card()->None:
    """user creates a new card"""

    one_card_dict = create_a_card_imd()

    print("名片创建成功：")
    cards_tools.print_one_card(one_card_dict)

    g_user_card_list.append(one_card_dict)


def show_all_cards()->None:
    """show all cards info"""

    print("\n共有%d张名片" % len(g_user_card_list))
    if len(g_user_card_list) == 0:
        print('您可以使用"新建名片功能"创建名片\n')
        return

    cards_tools.print_table_title()

    i = 1
    for card in g_user_card_list:
        print("%d." % i, end="\t")
        cards_tools.print_one_card_values(card)
        i += 1
    # don't add \n here, 'cause a return will be added by default
    print("")


def query_a_card_imd()->int:
    """return the card index, matching name queried"""

    name_input = input("请输入要查询的名字：")
    for this_user_dict in g_user_card_list:
        if name_input == this_user_dict["name"]:
            print("找到了！")
            return g_user_card_list.index(this_user_dict)
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

    current_dict = g_user_card_list[card_index]
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
    if card_index < len(g_user_card_list):
        del g_user_card_list[card_index]
        print("成功删除名片！")
    else:
        print("传入的名片索引错误！")
        assert "deleting_card_index out of range!"


def query_and_other_oper()->None:
    """query a card; modify this card del this card"""

    find_card_index = query_a_card_imd()
    if find_card_index != -1:
        cards_tools.print_one_card(g_user_card_list[find_card_index])

        user_next_choice = input("您要修改或删除该名片吗？"
                                 "m：修改；d：删除；其他：返回____")
        if user_next_choice == NEXT_CHOICE[0]:  # m:修改
            mod_a_card_imd(find_card_index)
        elif user_next_choice == NEXT_CHOICE[1]:  # d：删除
            del_a_card_imd(find_card_index)
        else:
            print("返回上一级菜单！")
