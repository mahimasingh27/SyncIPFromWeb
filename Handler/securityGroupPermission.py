class SecurityGroupPermission:
    def __init__(self, SecurityGroupId,ec2Resource):
        self.securityGroup=ec2Resource.SecurityGroup(SecurityGroupId)

    def getSecurityGroupIp(self):
        ipSet = set()
        for permission in self.securityGroup.ip_permissions:
            if permission.get('IpProtocol') == 'tcp':
                ipRanges = permission.get("IpRanges", [])
                for ipRange in ipRanges:
                    ip=ipRange["CidrIp"]
                    ipSet.add(ip)
        return ipSet

    def addIpInSG(self,IPToAdd):
        for ipAdd in IPToAdd:
            response = self.securityGroup.authorize_ingress(
                        IpPermissions=[
                        {
                        "IpProtocol": "tcp",
                            "FromPort": 443,
                            "ToPort": 443,
                            "IpRanges": [{"CidrIp": ipAdd}]
                        }
                        ]
                    )
        return response

    def removeIpInSG(self,IPToRemove):
        for ipRem in IPToRemove:
            response = self.securityGroup.revoke_ingress(
                        IpPermissions=[
                        {
                        "IpProtocol": "tcp",
                            "FromPort": 443,
                            "ToPort": 443,
                            "IpRanges": [{"CidrIp": ipRem}]
                        }
                        ]
                    )
        return response

    def compareAndUpdateIps(self,Ips,Monitor):
        securityGroupIps=self.getSecurityGroupIp()
        if Ips == securityGroupIps:
            print(Monitor + " IPs match security group IPs.")
        else:
            print(self.Monitor+" IPs do not match security group IPs.")
            self.addIpInSG(self,Ips-securityGroupIps)
            self.removeIpInSG(self,securityGroupIps-Ips)

