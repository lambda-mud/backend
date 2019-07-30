from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()

r_ca = Room(title="California",
               description="Dream Big, Eureka!, The Golden State")

r_nv = Room(title="Nevada", description="""A World Within. A State Apart; Battle Born; The Silver State; Home Means Nevada""")

r_or = Room(title="Oregon", description="""We Like It Here. You Might Too; We Love Dreamers; Things Look Different Here, Pacific Wonderland""")

r_wa = Room(title="Washington", description="""Washington: The State, SayWA!, Experience Washington, The Evergreen State""")

r_ca.save()
r_nv.save()
r_or.save()
r_wa.save()

# Link rooms together
r_ca.connectRooms(r_nv, "e")
r_ca.connectRooms(r_or, "n")

r_nv.connectRooms(r_ca, "w")
r_nv.connectRooms(r_or, "n")

r_or.connectRooms(r_wa, "n")
r_or.connectRooms(r_ca, "s")

r_wa.connectRooms(r_or, "s")

players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()

