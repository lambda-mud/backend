from django.contrib.auth.models import User
from adventure.models import Player, Room

Room.objects.all().delete()

roomsArray = [
    {'title': 'California', 'description': 'Dream Big, Eureka!, The Golden State'}, 
    {'title': 'Nevada', 'description': 'A World Within. A State Apart; Battle Born; The Silver State; Home Means Nevada'}, 
    {'title': 'Oregon', 'description': 'We Like It Here. You Might Too; We Love Dreamers; Things Look Different Here, Pacific Wonderland'}, 
    {'title': 'Washington', 'description': 'Washington: The State, SayWA!, Experience Washington, The Evergreen State'},
]

connectedCitiesIndex = [[0, 1, "e"], [0, 2, "n"], [1, 0, "w"], [1, 2, "n"], [2, 3, "n"], [2, 0, "s"], [3, 2, "s"]]

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

