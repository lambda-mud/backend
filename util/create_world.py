from django.contrib.auth.models import User
from adventure.models import Player, Room

Room.objects.all().delete()

roomsArray = [
    
    {'title': 'Seattle', 'description': 'EmptyDescription'},
    {'title': 'Spokane', 'description': 'EmptyDescription'},
    {'title': 'Portland', 'description': 'EmptyDescription'},
    {'title': 'Sacramento', 'description': 'EmptyDescription'},
    {'title': 'San Francisco', 'description': 'EmptyDescription'},
    {'title': 'Reno', 'description': 'EmptyDescription'},
    {'title': 'Las Vegas', 'description': 'EmptyDescription'},
    {'title': 'Phoenix', 'description': 'EmptyDescription'},
    {'title': 'Boise', 'description': 'EmptyDescription'},
    {'title': 'Salt Lake City', 'description': 'EmptyDescription'},
    {'title': 'Helena', 'description': 'EmptyDescription'},
    {'title': 'Billings', 'description': 'EmptyDescription'},
    {'title': 'Yellowstone National Park', 'description': 'EmptyDescription'},
    {'title': 'Cheyenne', 'description': 'EmptyDescription'},
    {'title': 'Denver', 'description': 'EmptyDescription'},
    {'title': 'Albuquerque', 'description': 'EmptyDescription'},
    # Good to here 15
    {'title': 'Bismarck', 'description': 'EmptyDescription'},
    {'title': 'Fargo', 'description': 'EmptyDescription'},
    {'title': 'Pierre', 'description': 'EmptyDescription'},
    {'title': 'Lincoln', 'description': 'EmptyDescription'},
    {'title': 'Wichita', 'description': 'EmptyDescription'},
    {'title': 'Oklahoma City', 'description': 'EmptyDescription'},
    {'title': 'Austin', 'description': 'EmptyDescription'},
    {'title': 'Kansas City', 'description': 'EmptyDescription'},
    {'title': 'Houston', 'description': 'EmptyDescription'}
]

connectedCitiesIndex = [[0, 1, "e"], [ 0, 1, "s"], [ 1, 0, "w"], [ 1, 10, "e"], [ 1, 8, "s"], [ 2, 0, "n"], [ 2, 3, "s"], [ 3, 2, "n"], [ 3, 5, "e"], [ 3, 4, "s"], [ 4, 3, "n"], [ 4, 6, "e"], [ 4, 7, "s"], [ 5, 3, "w"], [ 5, 9, "e"], [ 6, 4, "w"], [ 6, 9, "e"], [ 7, 4, "w"], [ 7, 15, "e"], [ 8, 2, "n"], [ 8, 12, "e"], [ 8, 9, "s"], [ 9, 5, "w"], [ 9, 8, "n"], [ 9, 6, "s"], [ 9, 14, "e"], [ 10, 1, "w"], [ 10, 12, "s"], [ 10, 11, "e"], [ 11, 10, "w"], [ 11, 16, "e"], [ 12, 8, "w"], [ 12, 10, "n"], [ 12, 13, "e"], [ 13, 12, "w"], [ 13, 14, "s"], [ 14, 13, "n"], [ 14, 9, "w"], [ 14, 15, "s"], [ 14, 20, "e"], [ 15, 7, "w"], [ 15, 14, "n"], [ 16, 11, "w"], [ 16, 18, "s"], [ 16, 17, "e"], [ 17, 16, "w"], [ 18, 16, "n"], [ 18, 19, "s"], [ 19, 18, "n"], [ 19, 20, "s"], [ 20, 14, "w"], [ 20, 19, "n"], [ 20, 23, "e"], [ 20, 21, "s"], [ 21, 20, "n"], [ 21, 22, "s"], [ 22, 21, "n"], [ 22, 24, "e"], [ 23, 20, "w"], [ 24, 22, "e"] ]

createdRooms = []

for i in range(len(roomsArray)):
  createdRooms.append(Room(title=roomsArray[i]['title'], description=roomsArray[i]['description']))
  createdRooms[i].save()

for i in range(len(connectedCitiesIndex)):
  createdRooms[connectedCitiesIndex[i][0]].connectRooms(createdRooms[connectedCitiesIndex[i][1]], connectedCitiesIndex[i][2])

players=Player.objects.all()
for p in players:
  p.currentRoom = createdRooms[0].id
  p.save()

