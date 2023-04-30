from rest_framework.serializers import ModelSerializer

from attendance.models import Member


class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
