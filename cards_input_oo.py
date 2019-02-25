import cards_tools


class Card:
    def __init__(self)->None:
        """initialization of card"""

        self.__user_card_list = []

    def __str__(self, index=None)->str:
        """print card info if index is specified, print this card otherwise,
        print the whole card list

        Args:
            index:
        """

        str_temp = ""
        for item in self.__user_card_list:
            str_temp += ("%s\n" % item)

        if index is None:
            return str_temp
        else:
            return str(self.__user_card_list[index])

    def create_a_card(self, card_info_tuple)->None:
        """create a new card

        Args:
            card_info_tuple:
        """

        self.__user_card_list.append(dict(zip(cards_tools.CARD_FIELD,
                                              card_info_tuple)))

        print("A new card is successfully created!\n")
        print(self.__str__(-1))

    def show_all_cards(self)->None:
        """show all cards info"""

        if len(self.__user_card_list) == 0:
            print('当前没有名片，您可以使用"新建名片功能"创建名片\n')
            return
        else:
            print("\n共有%d张名片:" % len(self.__user_card_list))

        cards_tools.print_table_title()

        i = 1
        for card in self.__user_card_list:
            print("%d." % i, end="\t")
            cards_tools.print_one_card_values(card)
            i += 1
        print("")

    def query_a_card(self)->int:
        """search a card based on user's input of name Assumption: card name
        should't be duplicated

            , so only the first match will be printed

        :rtype return card index
        """

        name_input = input("请输入要查询的名字：")

        for card in self.__user_card_list:
            if name_input == card["name"]:
                print("找到了！您要找的名片：\n", card)
                return self.__user_card_list.index(card)
        else:
            print("抱歉，没有找到所需名片！")
            return -1

    def mod_a_card(self, index)->None:
        """Modify a card name can also be modified space characters are not
        stripped

        Args:
            index:
        """

        print("请输入更新后的名片信息：")

        # only update the field when it is not NULL
        updated_dict = dict(zip(cards_tools.CARD_FIELD,
                                cards_tools.get_card_input()))

        for item in cards_tools.CARD_FIELD:
            if updated_dict[item] != "":
                self.__user_card_list[index][item] = updated_dict[item]

        print("名片信息已经更新\n", self.__str__(index))

    def del_a_card(self, index)->None:
        """del a card

        Args:
            index:
        """

        self.__user_card_list.pop(index)
        print("名片已经成功删除！")


# create a Card instance, global
g_my_card = Card()
NEXT_CHOICE = ("m", "d")


def new_card():

    g_my_card.create_a_card(cards_tools.get_card_input())


def show_all_cards():

    g_my_card.show_all_cards()


def query_and_other_oper():

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


