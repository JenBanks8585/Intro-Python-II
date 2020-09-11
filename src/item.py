# Implement a class to hold room information. This should have name and
# description attributes.

class Item:
    def __init__(self, name = "bracelet", description = "this should be in the bedroom.", current_room= 'foyer'):
        self.name = name 
        self.description = description
        self.current_room= current_room

    def __str__(self):
        return f"These are the {self.name}. I am not sure why they are here in the {self.current_room},  so can you please {self.description}."





item1= Item('clothes', 'take these to the basement.', 'bedroom')
item2= Item('paintings', 'hang these in the bedroom.', 'basement')
item3= Item('towels', 'fold these and take these to the bathroom.', 'kitchen')
item4= Item('plates', 'be careful, they easily break and take them to the kitchen.', 'basement')
item5= Item('soap', 'take these to the kitchen.', 'bathroom')
item6= Item('rugs', 'take these to the bathroom.', 'bedroom')

#print(item6)