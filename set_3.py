'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #Check if member follows the other
    if to_member in (social_graph[from_member])["following"]:
        follow=1
    else:
        follow=0
    #Check if the other member follow them
    if from_member in (social_graph[to_member])["following"]:
        followed=1
    else:
        followed=0
    if follow ==1:
        if followed==1:
            return "friends"
        if followed==0:
            return "follower"
    else:
        if followed==1:
            return "followed"
        if followed==0:
            return "no relationship"
        
def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac- toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
   
    #Checks if everything in a row is the same
    for sublist in board:
        if len(set(sublist))==1:
            if sublist[0] != "":
                return sublist[0]
    checking=[]
   
    #Check everything in a column
    for i in range(len(board)):
        for z in range(len(board[i])):
            checking.append(board[z][i])
        if len(set(checking))==1:
            if checking[0]!="":
                return checking[0]
        checking=[]
    #Check if diagonal going bottom right
    checkingdr=[]
    a=0
    for i in range(len(board)):
        checkingdr.append(board[i][a])
        a=a+1
    if len(checkingdr) > 0:
        if len(set(checkingdr))==1:
            if checkingdr[0]!="":
                return checkingdr[0]        
    #Check if diagonal going bottom left
    checkingdl=[]
    a=len(board)-1
    for i in range(len(board)):
        checkingdl.append(board[i][a])
        a=a-1
    if len(checkingdl) > 0:
        if len(set(checkingdl))==1:
            if checkingdl[0]!="":
                return checkingdl[0]
    return "NO WINNER"
       
def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    # Make the keys into a list
    keykey=list(route_map.keys())
    keypair=[]
    keylist=[]
    waytest=[first_stop,second_stop]
    way=(first_stop, second_stop)
    time=0
    #If route is direct.
    for sublist in keykey:
        keypair.append(sublist[0])
        keypair.append(sublist[1])
        keylist.append(keypair)
        keypair=[]
    
    #Check pos of starting route and ending route
    try:
        if keylist.index(waytest) >= 0:
            return route_map[way]['travel_time_mins']
    except:
        pass
    for i in range(len(keylist)):
        try:
            if keylist[i].index(first_stop) == 0:
                bim=i
        except:
            pass
        
        try:
            if keylist[i].index(second_stop)==1:
                bam=i
        except:
            pass
    #If first stop comes before second stop in the route_map
    if bim < bam:
        while bim <= bam:
            time=time+route_map[keykey[bim]]['travel_time_mins']
            bim=bim+1
        return time
    #If first stop comes after second stop
    if bam < bim:
        while bim <= (len(route_map)-1):
            time=time+route_map[keykey[bim]]['travel_time_mins']
            bim=bim+1
        abc=0
        
        while abc <= bam:
            time=time+route_map[keykey[abc]]['travel_time_mins']
            abc=abc+1
        return time 

