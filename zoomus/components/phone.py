"""Zoom.us REST API Python Client -- Phone component"""

from __future__ import absolute_import

from zoomus import util
from zoomus.components import base


class PhoneComponentV2(base.BaseComponent):
    
    def common_area_extension_id(self,**kwargs):
        return self.get_request("/phone/common_areas", params=kwargs)
        
    def sites(self, **kwargs):

        print("calling sites", kwargs)
        
        for key, value in kwargs.items():
            print(f"{key} = {value}")

        return self.post_request("/phone/sites", data=kwargs)

    def numbers_list(self, **kwargs):
        return self.get_request("/phone/numbers", params=kwargs)

    def numbers_get(self, **kwargs):
        util.require_keys(kwargs, "id")
        return self.get_request(
            "/phone/numbers/{}".format(kwargs.get("id")), params=kwargs
        )

    def call_logs(self, **kwargs):
        """
        Retrieve call logs for an account.

        Scopes: phone:read:admin

        Prerequisite:
        * Business or Enterprise account
        * A Zoom Phone license
        * Account Owner and a  with Zoom Phone Management

        :param page_size: The number of records returned within a single API call,
        default=30, max=300
        :param page_number: The current page number of returned records, default=1
        :param from: Start date from which you would like to get the call logs. The start date should be within past six months.
        :param to: The end date upto which you would like to get the call logs for.
        The end date should be within past six months.
        :param type: The type of the call logs. The value can be either "all" or "missed".
        :return: request object with json data
        """
        return self.get_request("/phone/call_logs", params=kwargs)

    def calling_plans(self, **kwargs):
        return self.get_request("/phone/calling_plans", params=kwargs)

    def users(self, **kwargs):
        return self.get_request("/phone/users", params=kwargs)
    
    def call_queues(self, **kwargs):
        print("calling call_queues")
        return self.get_request("/phone/call_queues")
    
    def call_queues_create(self, **kwargs):
        print("module calling call_queues_create")
        util.require_keys(kwargs, ["name"])

       

        print(kwargs)
        return self.post_request("/phone/call_queues", data=kwargs)
    
    def call_queue_members(self, **kwargs):
        util.require_keys(kwargs, "id")
        
        print("adding call_queue_members")
        
        value = kwargs.pop("id")
        print(kwargs)
        
        return self.post_request("/phone/call_queues/{}/members".format(value), data=kwargs)
    
    
    
    def call_queue_manager(self, **kwargs):
        util.require_keys(kwargs, "id")
        
        print("calling call_queues_manager")
        
        value = kwargs.pop("id")
        print(kwargs)
        
        return self.put_request("/phone/call_queues/{}/manager".format(value), data=kwargs)
    
    def site_list(self, **kwargs):

        print("calling site list", kwargs)
        
        for key, value in kwargs.items():
            print(f"{key} = {value}")

        return self.get_request("/phone/sites", params=kwargs)
    
    
