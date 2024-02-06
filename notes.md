Serialization: Converting python objects into Json data.

Some methods in the serializer class:
is_valid(self) := Tells if data is sufficient and valid to create/update a model instance.

save(self,,):= Method which knows how to create or update an instance.

create(self, validated_data):= method that knows how to update an instance

** Remember, the CreateAPI. Uses the POST to create entities but not to list them.  **
** RetrieveDestroyAPIView

** RetrieveDestroyAPIView: RetrieveS an individual entity details, or delete the entity. Allows GET and DELETE. **

# ModelSwerializers
Concept use is ti serialize classes that map closely to DJango model definitions.

ModelSerializer is same as regular Serializer class except that;
 1. IT automatically generates fields based on the model.

 2. Automatically generates validators for the serializer. i,e unique_together validators.

 3. Is inclusive of simple default implementations of .create() and .update()