# use REST API in this project #

Key Features of REST:
1. Serialization: Allows  automatic conversion of Django models to JSON and vice versa, hence efficient data transfer between client and server.

2. URL ROuting: DRF provides URL routing same as Django's router, that enables association of URLs with their API views efficiently.

3. Authentication: Offers various authentication including the basic auth and token auth(session based scenarios). Also supports JWT through third party(stateless scenarios).

4. Permission: Allows best control over user permissions

5. Throttling/Rate Limiting: These helps in limiting number of requests a client can make within a certain period.

6. Pagination: Provides built in support for paginating larger datasets in API responses.

7. Browsable API: Has a user friendly HTML interface for testing and exploring APIs directly from the browser.