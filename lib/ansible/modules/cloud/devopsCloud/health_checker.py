#!/usr/bin/python

# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
# Make coding more python3-ish

from __future__ import (absolute_import, division)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}



DOCUMENTATION = '''
---
module: health_checker
short_description: Downloads stuff from the interwebs
description:
    - Simple health check for Web page 
    
version_added: "2.2"
options:
  url:
    description:
      - URL to test ex. http://ynet.co.il/admin
    required: true
    default: null
  dest:
    description:
      - Where to test body
    required: false
    default: /tmp/http_logcheck
author:
    - "Yaniv cohen (@yanivomc)"
'''

RETURN = '''
msg:
    description: Just returns a friendly message
    returned: always
    type: string
    sample: 404 or ok 
'''

EXAMPLES = '''
# Download then save to your home dir
- firstmod:
    url: https://www.relaxdiego.com
    dest: ~/relaxdiego.com.txt
'''



from ansible.module_utils.basic import AnsibleModule
import requests

# (6) the fetch function receive the url and mod variables
def fetch(url, mod):


    s = requests.Session()
    headers = {'Content-Type': 'application/json'}
    #params = {'USER': "test", 'APPID': "4836627"}

    try:

     #   response = s.request('GET', url, headers=headers, params=params)
     response = s.request('GET', url, headers=headers)

    except requests.exceptions.HTTPError as e:
        mod.fail_json(msg="error is: " + e)


    # (7) if the response status code is not 200 then fail_json
    if response.status_code not in [200]:
        errormsg = str(response.status_code) + " - " + response.reason
        mod.fail_json(msg=(errormsg))

    return response.content


# (8) Write function
def write(data, dest):
    try:
        with open(dest, "w") as dest:
            dest.write(data)
    except IOError:
        raise WriteError("Data could not be written")

# (5) save_data funtion will call the fetch function and write function
def save_data(mod):
    data = fetch(mod.params["url"],mod)
    write(data, mod.params["dest"])


    mod.exit_json(msg="Data saved", changed=True)



class WriteError(Exception):

    pass



def main():
    # (2) initiate the Ansible module, this basically define the arguments accepted by this module
    mod = AnsibleModule(
        argument_spec=dict(
            url=dict(required=True),
            dest=dict(required=False, default="/tmp/http_checklog")
        )
    )

    # (4) this actualy run the function that will do the WORK by passing the ansbile (mod) instance to it.
    save_data(mod)


# (3) Execute the main function
if __name__ == '__main__':
    main()