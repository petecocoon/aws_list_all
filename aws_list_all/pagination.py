PAGINATION_CONFIGURATION = {
   'iam': { 'ListPolicies': { 'response_field': 'Policies', 'token': 'Marker', 'parameter': 'Marker' } }
}


def pagination_token_name(service, operation):
    return PAGINATION_CONFIGURATION.get(service, {}).get(operation, {}).get('token')

def pagination_parameter_name(service, operation):
    return PAGINATION_CONFIGURATION.get(service, {}).get(operation, {}).get('parameter')

def pagination_response_field_name(service, operation):
    return PAGINATION_CONFIGURATION.get(service, {}).get(operation, {}).get('response_field')

def is_supported(service, operation):
    return pagination_token_name(service, operation) != None

def has_pagination(service, operation, response):
    return bool(extract_pagination_token(service, operation, response))
    
def extract_pagination_token(service, operation, response):
    return response.get(pagination_token_name(service, operation))

def extract_pagination_parameters(service, operation, response):
    token = extract_pagination_token(service, operation, response)
    parameter = pagination_parameter_name(service, operation)
    return {parameter: token}

def merge_responses(service, operation, old_response, new_response):
    response_field = pagination_response_field_name(service, operation)
    old_response[response_field].extend(new_response[response_field])
    return old_response