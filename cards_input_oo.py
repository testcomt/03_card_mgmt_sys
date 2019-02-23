class Card:
    def __init__(self):
        """initialization of card"""

        self.name = None
        self.tel = None
        self.qq = None
        self.mail = None

    def __str__(self):
        """print card info"""

        return ("name = %s\ntel = %s\nqq = %s\nmail = %s\n"
                % (self.name, self.tel, self.qq, self.mail))

    def new_card(self):
        """create a new card"""

        print("new card")



