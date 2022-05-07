# Hello
import constants
import re

# def recursive_search(set, val):
#     is_found = False
#     if type(set) is list:
#         for item in set:
#             return recursive_search(item, val)
#     elif type(set) is dict:
#         for key in set.keys():
#             # Check the key
#             is_found = recursive_search(key, val)
#             # Check the value
#             if not is_found:
#                 return recursive_search(set[key], val)
#     elif set == val:
#         is_found = True
    
#     return is_found

def param_search(all_params, val):
    for param in all_params:
        if type(param) is list:
            if val == param[0]:
                return True 
        elif val == param.split('=')[0]:
            return True
        elif val.split('=') == param:
            return True
    return False
            

def format_url(app, method, key, param_string='', use_defaults=True):
    url = constants.BASE_API_URL
    url += constants.APPLICATIONS[app]['name'] + '/'
    url += constants.APPLICATIONS[app]['methods'][method] + '/'
    url += constants.APPLICATIONS[app]['version']

    # Begin parameters #
    params = []
    if param_string == '':
        input_params = []
    else:
        input_params = param_string.split(',')
    # First add all input params
    for i in input_params:
        vals = i.split('=')
        params.append(vals)

    # Next add all defaults.
    if use_defaults:
        params.append(['language', constants.DEFAULT_LANGUAGE])
        params.append(['format', constants.DEFAULT_RESULT_FORMAT])

    # Clean up params.
    final_params = []
    for pair in params:
        # If we don't already have the param, add it to the list.
        if not param_search(final_params, pair[0]):
            final_params.append(pair)

    # Always need a key param #    
    url += '?key=' + key

    # Additional parameters can be added using &param=<value>
    for use_param in final_params:
        url += '&' + use_param[0] + '=' + use_param[1]

    return url

# def print_url(url):
#     # Securely print the url without the key displayed.
#     if 'key=' in url:
#         re.sub("key\=[0-z]*", 'key\=\*\*\*\*\*', url)

#     print(url)
#     return True 

if __name__ == '__main__':
    # test_secret = get_secret('test_secret', 'us-west-2')
    my_url = format_url('dota2_matches', 'history', 'my_key')
    print(my_url)
    # print_url(my_url)