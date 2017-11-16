#!/usr/bin/python
# (1) Make coding more python3-ish
from __future__ import (absolute_import, division)

__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule


def save_data(mod):
    raise NotImplementedError


# (3) initiate the Ansible module, this basically define the arguments accepted by this module
def main():
    mod = AnsibleModule(
        argument_spec=dict(
            url=dict(required=True),
            dest=dict(required=False, default="/tmp/firstmod")
        )
    )




    # (4) this actualy run the function that will do the WORK by passing the ansbile (mod) instance to it.
    save_data(mod)

    # 4





# (2) Execute the main function
if __name__ == '__main__':
    main()


    # Note that this is the basic layout of a custom module.
    # This means that whenever your are building a custom module,
    # The main() function should only do the initiate of the Ansiblemodule and then pass it to another function
    # that will do the real work.



