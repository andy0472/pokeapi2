

class SiguientePagina:
    __POKEMON_NEXT=0
    def __init__(self):
        SiguientePagina.__POKEMON_NEXT+=20
        self.__pokemon_next=SiguientePagina.__POKEMON_NEXT

    def get_pokemon_next(self):
        return self.__pokemon_next

    def get_pokemon_previous(self):
        previous = self.__pokemon_next
        return previous-20
