import pulumi
from pulumi_openstack import compute, networking

fip1 = networking.FloatingIp('fip1', pool='public')

sg1 = networking.SecGroup('sg1')

networking.SecGroupRule('secgroupRule1',
    direction='ingress',
    ethertype='IPv4',
    port_range_max=80,
    port_range_min=80,
    protocol='tcp',
    remote_ip_prefix='0.0.0.0/0',
    security_group_id=sg1.id,
)

user_data = """#cloud-config
apt_update: true
apt_upgrade: true
packages:
  - nginx
"""

instance1 = compute.Instance('test',
	flavor_name='m1.small',
	image_name='bionic-server-cloudimg-amd64',
	networks=[{'name': 'private'}],
	user_data=user_data,
	security_groups=[sg1.name]
	)

fip_association = compute.FloatingIpAssociate('fip1',
    floating_ip=fip1.address,
    instance_id=instance1.id,
)

pulumi.export('ip', fip1.address)
