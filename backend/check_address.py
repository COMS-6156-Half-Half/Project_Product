from smartystreets_python_sdk import StaticCredentials, ClientBuilder                               
from smartystreets_python_sdk.us_street import Lookup                                               
                                                                                                                                                                                            
def check_address(addr):
    if (len(addr.split(',')) != 3):
        return False

    auth_id = "c270223e-4b26-53cd-36e6-34a17cb7cb55"                                                
    auth_token = "3J8lKTskYlJk4rvKmeHz"                                                             
    credentials = StaticCredentials(auth_id, auth_token)                                            
                                                                                                    
    client = ClientBuilder(credentials).build_us_street_api_client()                                
                                                                                                    
    lookup = Lookup()                                                                               
    lookup.street = addr.split(',')[0]
    lookup.city = addr.split(',')[1]
    lookup.state = addr.split(',')[2]
    lookup.candidates = 10                                                                          
                                                                                                    
    client.send_lookup(lookup)                                                                      
                                                                                                    
    if not lookup.result:
        return False
    else:
        return True
    # _, candidate = enumerate(lookup.result)
    # print(candidate[1].delivery_line_1)                        
    # for c, candidate in enumerate(lookup.result):                                                   
    #     print("- {}: {}, {}".format(c, candidate.delivery_line_1, candidate.last_line))