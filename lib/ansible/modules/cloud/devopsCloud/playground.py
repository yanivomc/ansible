#!/usr/bin/python
# Make coding more python3-ish
from __future__ import (absolute_import, division)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
import requests

def fetch(url, mod):


    s = requests.Session()
    try:

        response = requests.get(url)

    except requests.exceptions.HTTPError as e:
        mod.fail_json(msg="error is: " + e)


    if response.status_code not in [200]:
        mod.fail_json(msg=(response.status_code))



    return response.content
def write(data, dest):
    try:
        with open(dest, "w") as dest:
            dest.write(data)
    except IOError:
        raise WriteError("Data could not be written")


def save_data(mod):
    data = fetch(mod.params["url"],mod)

    write(data, mod.params["dest"])


    mod.exit_json(msg="Data saved", changed=True)



class WriteError(Exception):

    pass



def main():
    mod = AnsibleModule(
        argument_spec=dict(
            url=dict(required=True),
            dest=dict(required=False, default="/tmp/firstmod")
        )
    )

    save_data(mod)


if __name__ == '__main__':
    main()