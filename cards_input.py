# Deal with user's choices
# 1. create a card
# 2. Display all cards
# 3. Query one card (3.1 modify card; 3.2 del a card)

def get_card_input()->list:
    """Obtain user's input for his card
    not checking correctness"""

    name = input("姓名：")
    tel = input("电话：")
    qq = input("QQ: ")
    mail = input("邮件：")

    return [name, tel, qq, mail]


def create_a_card()->dict:
    """create a card dict based on user's input"""

    return dict(zip(["name", "tel", "qq", "mail"], get_card_input()))
