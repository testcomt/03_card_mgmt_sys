# common methods which does not require any user's input
CARD_FIELD = ("name", "tel", "qq", "mail")


def welcome_info()->None:
    """display welcome info Attention: the item-info need to be updated with
    redefinition of choice_list
    """

    print("*" * 30)
    print("欢迎使用【名片管理系统】 v1.0\n")
    print("1. 新建名片\n2. 显示全部\n3. 查询名片\n\n0. 退出系统")
    print("*" * 30)


def print_one_card(one_card_dict)->None:
    """print card info gracefully :rtype: object

    Args:
        one_card_dict: card dict to be printed out
    """

    print("-" * 20)
    for key in one_card_dict.keys():
        print("%s : %s" % (key, one_card_dict[key]))
    print("-" * 20)


def print_one_card_values(one_card_dict)->None:
    """Only print card values in a line

    Args:
        one_card_dict: the card to be printed [dict]
    """

    for value in one_card_dict.values():
        print(value.ljust(14), end='\t')
    print("\n")


def get_card_input_imd()->tuple:
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

    # parenthesis not needed, tuple by default
    return name, tel, qq, mail


def print_table_title()->None:
    """print card title"""

    print("-" * 100)
    for field in CARD_FIELD:
        print("", end="\t")
        print(field.ljust(10), end="\t")
    print("")
    print("-" * 100)
