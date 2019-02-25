import cards_tools


class Card:
    def __init__(self):
        """initialization of card"""

        self.__user_card_list = []

    def __str__(self, index=None):
        """print card info
        if index is specified, print this card
        otherwise, print the whole card list"""

        str_temp = ""
        for item in self.__user_card_list:
            str_temp += ("%s\n" % item)

        if index is None:
            return str_temp
        else:
            return str(self.__user_card_list[index])

    def create_a_card(self, card_info_tuple):
        """create a new card"""

        self.__user_card_list.append(dict(zip(("name", "tel", "qq", "mail"),
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


# create a Card instance, global
g_my_card = Card()


def new_card():

    g_my_card.create_a_card(cards_tools.get_card_input_imd())


def show_all_cards():

    g_my_card.show_all_cards()


def query_and_other_oper():

    pass


