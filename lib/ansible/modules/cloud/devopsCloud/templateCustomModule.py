#!/usr/bin/python
# (1) Make coding more python3-ish
from __future__ import (absolute_import, division)

__metaclass__ = type

#### As our module code is not the only code that is being executed
#  Ansible takes our code and construct a single Python script that gets copied to the remote system and then executed.
# The "from ansible.module_utils.basic import AnsibleModule " imports * ~ 1600 lines or the module we require to the final script

from ansible.module_utils.basic import AnsibleModule

# (5) the actual function
def some_funcion(mod):

    mod_local_input_var = mod.params['input']

    mod.exit_json(changed=True, msg="Some Function ran", CustoMessage="message from function " + mod_local_input_var)
    mod.fail_json(msg="Some fatal error happened")


    raise NotImplementedError
# (3) initiate the Ansible module, this basically define the arguments accepted by this module
def main():
    mod = AnsibleModule(
        argument_spec=dict(
            input=dict(required=False, default=""),
            input2=dict(required=False, default="some string")
        )
    )
    # (4) this actualy run the function that will do the WORK by passing the ansbile (mod) instance to it.
    some_funcion(mod)

    #We can Access the module dictionary parmeters using: 'module.params['key']'

    mod_local_input_var = mod.params['input']
    # In ansible return values must be serialize as JSON to integrate with ansible
    # one way to do it is to use exit_json - "changed=..." is required , other fields are custom
    #mod.exit_json(changed=True, msg=mod_local_input_var)


# (2) Execute the main function
if __name__ == '__main__':
    main()


    # Note that this is the basic layout of a custom module.
    # This means that whenever your are building a custom module,
    # The main() function should only do the initiate of the Ansiblemodule and then pass it to another function
    # that will do the real work.



