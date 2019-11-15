# A minimal OpenStack Python Pulumi program

## Prerequisites

```console
$ curl -sSL https://get.pulumi.com | sh
$ python3 -m venv .venv
$ .venv/bin/pip3 install -r requirements.txt
$ source .venv/bin/activate
$ source openrc.rc
```

## Preview deployment

```console
$ pulumi stack init dev
Created stack 'dev'
$ pulumi preview
Previewing update (dev):

     Type                                      Name           Plan       
 +   pulumi:pulumi:Stack                       hello-dev      create     
 +   ├─ openstack:networking:SecGroup          sg1            create     
 +   ├─ openstack:networking:FloatingIp        fip1           create     
 +   ├─ openstack:networking:SecGroupRule      secgroupRule1  create     
 +   ├─ openstack:compute:Instance             test           create     
 +   └─ openstack:compute:FloatingIpAssociate  fip1           create     
 
Resources:
    + 6 to create

Permalink: https://app.pulumi.com/XXX
```

## Deploy

```console
$ pulumi up -y
Previewing update (dev):

     Type                                      Name           Plan       
 +   pulumi:pulumi:Stack                       hello-dev      create     
 +   ├─ openstack:networking:SecGroup          sg1            create     
 +   ├─ openstack:networking:FloatingIp        fip1           create     
 +   ├─ openstack:networking:SecGroupRule      secgroupRule1  create     
 +   ├─ openstack:compute:Instance             test           create     
 +   └─ openstack:compute:FloatingIpAssociate  fip1           create     
 
Resources:
    + 6 to create

Updating (dev):

     Type                                      Name           Status      
 +   pulumi:pulumi:Stack                       hello-dev      created     
 +   ├─ openstack:networking:SecGroup          sg1            created     
 +   ├─ openstack:networking:FloatingIp        fip1           created     
 +   ├─ openstack:networking:SecGroupRule      secgroupRule1  created     
 +   ├─ openstack:compute:Instance             test           created     
 +   └─ openstack:compute:FloatingIpAssociate  fip1           created     
 
Outputs:
    ip: "X.X.X.X"

Resources:
    + 6 created

Duration: 28s

Permalink: https://app.pulumi.com/XXX
```

## Destroy

```console
$ pulumi destroy -y
Previewing destroy (dev):

     Type                                      Name           Plan       
 -   pulumi:pulumi:Stack                       hello-dev      delete     
 -   ├─ openstack:compute:FloatingIpAssociate  fip1           delete     
 -   ├─ openstack:networking:SecGroupRule      secgroupRule1  delete     
 -   ├─ openstack:compute:Instance             test           delete     
 -   ├─ openstack:networking:SecGroup          sg1            delete     
 -   └─ openstack:networking:FloatingIp        fip1           delete     
 
Outputs:
  - ip: "X.X.X.X"

Resources:
    - 6 to delete

Destroying (dev):

     Type                                      Name           Status      
 -   pulumi:pulumi:Stack                       hello-dev      deleted     
 -   ├─ openstack:compute:FloatingIpAssociate  fip1           deleted     
 -   ├─ openstack:networking:SecGroupRule      secgroupRule1  deleted     
 -   ├─ openstack:compute:Instance             test           deleted     
 -   ├─ openstack:networking:SecGroup          sg1            deleted     
 -   └─ openstack:networking:FloatingIp        fip1           deleted     
 
Outputs:
  - ip: "X.X.X.X"

Resources:
    - 6 deleted

Duration: 28s

Permalink: https://app.pulumi.com/XXX
The resources in the stack have been deleted, but the history and configuration associated with the stack are still maintained. 
If you want to remove the stack completely, run 'pulumi stack rm dev'.
$ pulumi stack rm dev -y
Stack 'dev' has been removed!
```
