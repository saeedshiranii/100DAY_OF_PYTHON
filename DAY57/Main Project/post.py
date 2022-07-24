import requests


class Post:
    
    def __init__(self, single_dict, data):

        self.post_number = single_dict
        self.post = data[single_dict]["post"]
        self.title = data[single_dict]["title"]
        self.subtitle = data[single_dict]["subtitle"]
            
                                              
        

