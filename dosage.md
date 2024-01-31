# use REST API in this project #

Key Features of REST:
1. Serialization: Allows  automatic conversion of Django models to JSON and vice versa, hence efficient data transfer between client and server.

2. URL ROuting: DRF provides URL routing same as Django's router, that enables association of URLs with their API views efficiently.

3. Authentication: Offers various authentication including the basic auth and token auth(session based scenarios). Also supports JWT through third party(stateless scenarios).

4. Permission: Allows best control over user permissions

5. Throttling/Rate Limiting: These helps in limiting number of requests a client can make within a certain period.

6. Pagination: Provides built in support for paginating larger datasets in API responses.

7. Browsable API: Has a user friendly HTML interface for testing and exploring APIs directly from the browser.


## installation ##

pip install djangorestframework

Add the the app to installed app in the settings as below:

** 'rest_framework'

Steps for defining an API are acreating a serizlizer class(serializers.py), views and then binding the urls.


## Permissions in REST API ##
DRF has in built permissions used to secure the API. You can set the permissions at three levels:
  1. Project-level
  2. View-level
  3. Model-level

   ### Project level permissions ###
They are set in the single Django settting called REST_FRAMEWORK in settings.py file.

Despite the default allowAny policy, it has other built-in project levele permissions sucj as:
  1. IsAutheneticated: Access to only authenticated users
  2. IsAdminUser: Only admin/superuser access
  3. IsAuthenticatedOrReadOnly:Only authenticated users can perfom CRUD


  REST has two main decorators for views:
    @apiview( decorator for working with function based views)
      """_summary_
      """    APIView ( decorator class for working with CBV)