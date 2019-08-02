from django.contrib.auth.models import User
from adventure.models import Player, Room

Room.objects.all().delete()

roomsArray = [
    
    {'title': 'Seattle', 'description': 'The Emerald City.'},
    {'title': 'Spokane', 'description': 'Creative by Nature'},
    {'title': 'Portland', 'description': 'The City That Works'},
    {'title': 'Sacramento', 'description': 'Almond Capital of the World'},
    {'title': 'San Francisco', 'description': 'The City by the Bay'},
    {'title': 'Reno', 'description': 'Biggest Little City in the World'},
    {'title': 'Las Vegas', 'description': 'What Happens in Vegas, Stays in Vegas.'},
    {'title': 'Phoenix', 'description': "It's a DRY heat.  Very efficient."},
    {'title': 'Boise', 'description': 'Energy Peril Success. Whatever that means.'},
    {'title': 'Salt Lake City', 'description': 'The Beehive Valley'},
    {'title': 'Helena', 'description': 'Queen City of the Rockies'},
    {'title': 'Billings', 'description': 'Magic City'},
    {'title': 'Yellowstone National Park', 'description': 'Wonderland'},
    {'title': 'Cheyenne', 'description': 'Magic City of the Plains'},
    {'title': 'Denver', 'description': 'Mile High City'},
    {'title': 'Albuquerque', 'description': 'The Duke City.  The towels are oh so fluffy.'},
    # Good to here 15
    {'title': 'Bismarck', 'description': 'The Skyscraper on the Prairie'},
    {'title': 'Fargo', 'description': 'Gateway to the West'},
    {'title': 'Pierre', 'description': 'There is nothing interesting about this city.'},
    {'title': 'Lincoln', 'description': 'Husker City'},
    {'title': 'Wichita', 'description': 'Air Capital of the World. Doo-Dah'},
    {'title': 'Oklahoma City', 'description': 'The Big Friendly.  Sooners abound.'},
    {'title': 'Austin', 'description': 'Keep Austin Weird'},
    {'title': 'Kansas City', 'description': 'Paris of the Plains. Big jazz/barbecue place, apparently.'},
    {'title': 'Houston', 'description': 'H-Town, Bayou City, The Big H.'}
]

connectedCitiesIndex = [[0, 1, "e"], [ 0, 2, "s"], [ 1, 0, "w"], [ 1, 10, "e"], [ 1, 8, "s"], [ 2, 0, "n"], [ 2, 3, "s"], [ 3, 2, "n"], [ 3, 5, "e"], [ 3, 4, "s"], [ 4, 3, "n"], [ 4, 6, "e"], [ 4, 7, "s"], [ 5, 3, "w"], [ 5, 9, "e"], [ 6, 4, "w"], [ 6, 9, "e"], [ 7, 4, "w"], [ 7, 15, "e"], [ 8, 2, "n"], [ 8, 12, "e"], [ 8, 9, "s"], [ 9, 5, "w"], [ 9, 8, "n"], [ 9, 6, "s"], [ 9, 14, "e"], [ 10, 1, "w"], [ 10, 12, "s"], [ 10, 11, "e"], [ 11, 10, "w"], [ 11, 16, "e"], [ 12, 8, "w"], [ 12, 10, "n"], [ 12, 13, "e"], [ 13, 12, "w"], [ 13, 14, "s"], [ 14, 13, "n"], [ 14, 9, "w"], [ 14, 15, "s"], [ 14, 20, "e"], [ 15, 7, "w"], [ 15, 14, "n"], [ 15, 22, "s"], [ 16, 11, "w"], [ 16, 18, "s"], [ 16, 17, "e"], [ 17, 16, "w"], [ 18, 16, "n"], [ 18, 19, "s"], [ 19, 18, "n"], [ 19, 20, "s"], [ 20, 14, "w"], [ 20, 19, "n"], [ 20, 23, "e"], [ 20, 21, "s"], [ 21, 20, "n"], [ 21, 22, "s"], [ 22, 21, "n"], [ 22, 24, "e"], [ 22, 15, "w"], [ 23, 20, "w"], [ 24, 22, "e"] ]

createdRooms = []

for i in range(len(roomsArray)):
  createdRooms.append(Room(title=roomsArray[i]['title'], description=roomsArray[i]['description']))
  if i % 3 == 0:
    createdRooms[i].can_make_money = True
  createdRooms[i].save()

for i in range(len(connectedCitiesIndex)):
  createdRooms[connectedCitiesIndex[i][0]].connectRooms(createdRooms[connectedCitiesIndex[i][1]], connectedCitiesIndex[i][2])

players=Player.objects.all()
for p in players:
  p.currentRoom = createdRooms[0].id
  p.save()

