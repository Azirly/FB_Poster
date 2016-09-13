#Current Date Edit on top
#6/11/2016

#Issues with using Facebook API


import facebook
import time

#Structs Here
Tokens =  {
    '''
    I give you went I can automate this.
    '''
}

FB_Groups = {
    #'WICS': '2200392077',
    #'IEEE': '353086428076607',
    #'BIM': '353033718081878',
    #'SWE': '2200130987',
    #'DATspace': '141673622569388', #problem
    #'ICS': '353008418084408',
    #'CS': '352925081426075',
    #'ICSSC': '323935841652',
    #'ACM': '228954137162541',
    #'VGDC': '506447329398010',         #problem
    #'UCI Hackers': '264672160360168', #problem
    #'IN4MATX ': '353047451413838',
    #'UCI AppDev': '804525909598967', #problem
    #'Class 2019': '550306828438333', #problem
    #'Class 2018': '245262542297029', #problem
    #'Class 2017': '306196982840992', #problem
    
       
}

attachment = {
    'name': '',
    'link': '',
    'caption': '',
    'description': '',
    'picture': ''
    }

post ='''
Who's going to be in Irvine over the summer?
'''

def main():
    #Creates the graph from the Graph API from Facebook
    graph = facebook.GraphAPI(access_token=Tokens['ACCESS_TOKEN'], version='2.2')


    for group_id in FB_Groups.values():
        print(group_id)
        post_group_message(graph, group_id)

def post_user_message(da_graph, fb_page_id):
    successful_post = da_graph.put_wall_post(post,attachment, profile_id = fb_page_id)
    return successful_post

def post_group_message(graph,fb_page_id):

##    groups = [ 'groupid1', 'groupid2', 'groupid3']
##    for group_id in groups:
##	print "Posting to " + 'http://www.facebook.com/groups/' + str(group_id)
##	graph.post(path =str(group_id) + '/feed', message=message)
##	time.sleep(10)
##  
    successful_post = graph.put_wall_post(post,attachment,profile_id = fb_page_id)
    return successful_post


if __name__ == "__main__":
    main()

