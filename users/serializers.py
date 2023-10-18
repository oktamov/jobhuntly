from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "first_name", "last_name", "address", "image"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={"input_type": "password"})

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = User.objects.filter(email=email).first()

            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User account is disabled.")
                if not user.check_password(password):
                    raise serializers.ValidationError("Invalid password.")
            else:
                raise serializers.ValidationError("User not found.")
        else:
            raise serializers.ValidationError('Must include "email" and "password".')

        refresh = RefreshToken.for_user(user)
        attrs["tokens"] = {"access": str(refresh.access_token), "refresh": str(refresh)}
        attrs["user"] = user
        return attrs


class UserPasswordChangeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    old_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)

    def validate(self, attrs):
        user = User.objects.get(email=self.email)
        if user.check_password(self.old_password):
            user.password = self.new_password1
            user.set_password(self.new_password1)

        else:
            return "Invalid password"
        user.save()
        return user
