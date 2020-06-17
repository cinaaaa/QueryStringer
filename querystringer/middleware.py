from django.conf import settings

def QueryStringer(get_response):
    # Wrapper that get the requests
    # and let views proccess after
    # the wrapper do the job
    def wrapper(request):
        # Code to be executed for each request before
        # the view later middleware are called.

        # Filter get requests
        if request.method == 'GET':

            # Dict that will return after
            # all stuffs
            query_strings = []

            # Extract request query strings
            # and loop them to Generate
            # clean list of the values
            for (key,value) in dict(request.GET.lists()).items():

                # Check for that we have remove
                # strings list in settings
                try:
                    # Loop each value that extracted
                    # to check & remove the needed
                    # strings from them
                    for rm in settings.QUERY_REMOVE_STRINGS:
                        value[0] = value[0].replace(rm, '')
                except:
                    pass

                # Now cleaned data push to final list
                query_strings.append((key,value[0]))

            # Get copy from request get
            # then append query strings
            # as queries key
            edited_request = request.GET.copy()
            edited_request['queries'] = query_strings

            # Change the default get method
            # to our new edited data
            request.GET = edited_request
            response = get_response(request)

        return response

    return wrapper
