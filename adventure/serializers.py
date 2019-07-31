from rest_framework import serializers


class RoomSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=500)
    n_to = serializers.IntegerField(default=0)
    s_to = serializers.IntegerField(default=0)
    e_to = serializers.IntegerField(default=0)
    w_to = serializers.IntegerField(default=0)