"""Zoom.us REST API Python Client -- Contact Center Component"""

from __future__ import absolute_import

from zoomus import util
from zoomus.components import base

#add logging to the component

import logging
log = logging.getLogger(__name__)

class ContactCenterComponentV2(base.BaseComponent):
    
    def queues_list(self, **kwargs):
        return self.get_request("/contact_center/queues", params=kwargs)

    def queues_update(self, **kwargs):
        
        util.require_keys(kwargs, "queue_id")
        print("updating contact center queues")

        return self.patch_request("/contact_center/queues/{}".format(kwargs.get("queue_id")), data=kwargs)
    
    
    def queues_add(self, **kwargs):
        util.require_keys(kwargs, "queue_name", "queue_description")
        
        print("adding contact center")
        
        
        print(kwargs)
        
        return self.post_request("/contact_center/queues/", data=kwargs)
    
    def queues_operating_hours_update(self, **kwargs):
        util.require_keys(kwargs, "queue_id")
        print("updating contact center operating hours",kwargs)
        log.debug("updating contact center operating hours")

        return self.patch_request("/contact_center/queues/{}/operating_hours".format(kwargs.get("queue_id")), data=kwargs)
    
    #/contact_center/business_hours

    def queues_dispositions_update(self, **kwargs):
        util.require_keys(kwargs, "queue_id")
        print("updating contact center disposition",kwargs)
        log.debug("updating contact center disposition")

        return self.post_request("/contact_center/queues/{}/dispositions".format(kwargs.get("queue_id")), data=kwargs)
    
    def queues_disposition_set_update(self, **kwargs):
        util.require_keys(kwargs, "queue_id")
        print("updating contact center disposition",kwargs)
        log.debug("updating contact center disposition")

        return self.post_request("/contact_center/queues/{}/dispositions/sets".format(kwargs.get("queue_id")), data=kwargs)
    

    def business_hours(self, **kwargs):
        return self.get_request("/contact_center/business_hours")
    
    def dispositions_list(self, **kwargs):
        return self.get_request("/contact_center/dispositions")
    
    def dispositions_set_list(self, **kwargs):
        return self.get_request("/contact_center/dispositions/sets")
    
    def flows_list(self, **kwargs):
        return self.get_request("/contact_center/flows", params=kwargs)
    
    def inbox_list(self, **kwargs):
        return self.get_request("/contact_center/inboxes", params=kwargs)
    
    def waiting_room_list(self, **kwargs):
        return self.get_request("/contact_center/waiting_room", params=kwargs)
    
    


    
    
    
    
    
    
