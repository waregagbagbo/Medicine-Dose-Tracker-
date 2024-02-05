Serialization: Converting python objects into Json data.

Some methods in the serializer class:
is_valid(self) := Tells if data is sufficient and valid to create/update a model instance.

save(self,,):= Method which knows how to create or update an instance.

create(self, validated_data):= method that knows how to update an instance