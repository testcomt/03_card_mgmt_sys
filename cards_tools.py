# common methods which does not require any user's input


def welcome_info()->None:
    """display welcome info
    Attention: the item-info need to be updated with redefinition of choice_list
    """

    print("*" * 30)
    print("欢迎使用【名片管理系统】 v1.0\n")
    print("1. 新建名片\n2. 显示全部\n3. 查询名片\n\n0. 退出系统")
    print("*" * 30)


def print_one_card(one_card_dict)->None:
    """print card info gracefully
    :rtype: object
    """

    print("-" * 20)
    for key in one_card_dict.keys():
        print("%s : %s" % (key, one_card_dict[key]))
    print("-" * 20)


def print_one_card_values(one_card_dict)->None:
    """Only print card values in a line"""

    for value in one_card_dict.values():
        print(value.ljust(14), end='\t')
    print("\n")

