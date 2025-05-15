#  Match case is just like switch statement in other langauge
def htthp_server(status):
    match status:
        case 303:
            return "loading error"
        case 404:
            return "Server error"
        case 500:
           return "Network error"
        case _:
           return "unknown error"
print(htthp_server(303))