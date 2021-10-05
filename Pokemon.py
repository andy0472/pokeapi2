
class Pokemon:

    def __init__(self ,foto=None ,id=None ,name=None ,ability=None ,type=None ,moves=None):
        self.foto =foto
        self.id =id
        self.name =name
        self.ability =ability
        self.type =type
        self.moves =moves

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_foto(self):
        return self.foto

    def get_ability(self):
        return self.ability

    def get_type(self):
        return self.type

    def get_moves(self):
        return self.moves

    def get_pokemones(self):
        return(f"""
                Foto: {self.foto}
                ID:    {self.id}
                Name:    {self.name}        
                Ability:    {self.ability}
                Type:    {self.type}
                Moves:    {self.moves}

        """)
