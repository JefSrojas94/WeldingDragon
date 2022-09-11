from rest_framework import serializers
from WeldingDragonApp.Models.User import User 

class UserSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = User
        fields = ['id', 'username', 'nombre', 'apellido', 'cedula', 'correo', 'tipo_de_Cliente']

    def create(self, validated_data):
        accountData = validated_data.pop('account')
        userInstance = User.objects.create(**validated_data)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'nombre': user.nombre,
            'apellido': user.apellido,
            'cedula': user.cedula,
            'correo': user.correo,
            'tipo_de_Cliente': user.tipo_de_Cliente,
            
}
