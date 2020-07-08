
The OMDb API is a RESTful web service to obtain movie information, all content and images on the site are contributed and maintained by our users.


=======
Install
=======

.. code-block:: bash

    pip install omdb_client

=======
Example
=======

.. code-block:: python

    from omdb.client import OMDAPI

    API_KEY = 'api key'
    title = 'mask'
    id = 100000
    client = OMDAPI(API_KEY)
    movies = client.search_title(title)
    movie = client.search_id(id)


=======
Donation
=======

.. image:: https://img.shields.io/badge/Donate-PayPal-green.svg
  :target: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=YYZQ6ZRZ3EW5C
