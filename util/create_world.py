from django.contrib.auth.models import User
from adventure.models import Player, Room

Room.objects.all().delete()

roomsArray = [
    {'title': 'California', 'description': 'Dream Big, Eureka!, The Golden State'}, 
    {'title': 'Nevada', 'description': 'A World Within. A State Apart; Battle Born; The Silver State; Home Means Nevada'}, 
    {'title': 'Oregon', 'description': 'We Like It Here. You Might Too; We Love Dreamers; Things Look Different Here, Pacific Wonderland'}, 
    {'title': 'Washington', 'description': 'Washington: The State, SayWA!, Experience Washington, The Evergreen State'},
]

createdRooms = []

for i in range(len(roomsArray)):
    createdRooms.append(Room(title=roomsArray[i]['title'], description=roomsArray[i]['description']))
    createdRooms[i].save()


# Link rooms together
createdRooms[0].connectRooms(createdRooms[1], "e")
createdRooms[0].connectRooms(createdRooms[2], "n")
createdRooms[1].connectRooms(createdRooms[0], "w")
createdRooms[1].connectRooms(createdRooms[2], "n")
createdRooms[2].connectRooms(createdRooms[3], "n")
createdRooms[2].connectRooms(createdRooms[0], "s")
createdRooms[3].connectRooms(createdRooms[2], "s")


players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()

