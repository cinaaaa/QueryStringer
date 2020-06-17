# QueryStringer
Simple middleware for django to extract string queries from urls

# Installation
```
pip install querystringer
```

# Import
import it inside middleware in django settings
```
middlewares = [
  ...,
  'querystringer.middleware.QueryStringer',
  ...,
]
```

# Usage
all requests will have an edited request dict
and you can access them by `request.GET['queries']`

# Example
our view
```
def home(request):
    return HttpResponse(request.GET['queries'])
```
then send request to `/home?test=true`
now we should except output like this
```
('test', 'true')
```

# Remove specific characters
in your `settings.py` add a list with `QUERY_REMOVE_STRINGS` name
to ignore characters you want
like this
```
QUERY_REMOVE_STRINGS = ['-', '>', '%']
```
then the data you get will be clean
like this
request to `/home?test=tru>e`
then we get `(test, true)`
