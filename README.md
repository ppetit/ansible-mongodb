Cloudweeb Mongodb
=========

[![Build Status](https://travis-ci.com/cloudweeb/cloudweeb.mongodb.svg?branch=master)](https://travis-ci.com/cloudweeb/cloudweeb.mongodb)

Ansible role to install MongoDB

Requirements
------------

None

Role Variables
--------------

```YAML
# MongoDB version that want to be installed
mongodb_version: 4.0
```

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: cloudweeb.mongodb

License
-------

MIT

Author Information
------------------

Agnesius Santo Naibaho
