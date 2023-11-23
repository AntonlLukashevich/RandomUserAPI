from rest_framework import serializers
from .models import RandomUser


class RandomUserSerializer(serializers.ModelSerializer):
    def save_response(self, response_data):
        result = response_data["results"][0]
        name = result['name']
        location = result['location']
        login = result['login']
        dob = result['dob']

        data = {
            'gender': result.get("gender"),
            'first_name': name.get("first"),
            'last_name': name.get("last"),
            'street_number': location['street'].get("number"),
            'street_name': location['street'].get("name"),
            'city': location.get("city"),
            'country': location.get("country"),
            'postcode': location.get("postcode"),
            'login': login.get("username"),
            'password': login.get("password"),
            'email': result.get("email"),
            'born_date': dob.get("date"),
            'age': dob.get("age"),
        }

        RandomUser.objects.create(**data)

    class Meta:
        model = RandomUser
        fields = '__all__'
