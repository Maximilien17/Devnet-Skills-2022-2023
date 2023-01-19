
import json
from pickle import FALSE
docker_json_file = [
    {
        "Id": "sha256:9140108b62dc87d9b278bb0d4fd6a3e44c2959646eb966b86531306faa81b09b",
        "RepoTags": [
            "ubuntu:latest"
        ],
        "RepoDigests": [
            "ubuntu@sha256:bc2f7250f69267c9c6b66d7b6a81a54d3878bb85f1ebb5f951c896d13e6ba537"
        ],
        "Created": "2020-09-25T22:34:30.295807036Z",
        "Container": "1046a5d685aef5c37d1829040ca8083b94e4c069ca4963f4b16a6ade2e077b06",
        "ContainerConfig": {
            "Hostname": "1046a5d685ae",
            "Domainname": "",
            "User": "",
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"/bin/bash\"]"
            ],
            "Image": "sha256:4ff2090064e7e38688bce713d50f3202d227b3c89fecea1434271c912ccd47e0",
            "Entrypoint": None,
        },
        "DockerVersion": "18.09.7",
        "Config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/bash"
            ],
            "Image": "sha256:4ff2090064e7e38688bce713d50f3202d227b3c89fecea1434271c912ccd47e0",
            "Entrypoint": None,
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 72875723,
        "VirtualSize": 72875723,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/5d66f43.../diff",
                "MergedDir": "/var/lib/docker/overlay2/c3bab84.../merged",
                "UpperDir": "/var/lib/docker/overlay2/c3bab84.../diff",
                "WorkDir": "/var/lib/docker/overlay2/c3bab84.../work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
              "sha256:d42a4fdf4b2ae8662ff2ca1b695eae571c652a62973c1beb81a296a4f4263d92",
                "sha256:90ac32a0d9ab11e7745283f3051e990054616d631812ac63e324c1a36d2677f5",
                "sha256:782f5f011ddaf2a0bfd38cc2ccabd634095d6e35c8034302d788423f486bb177"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]

print("+++++++++1++++++++")
print("---------1--------")
print("Converting json string to dict, and showing keys at level 1")
docker_dict = json.dumps(docker_json_file)
print(docker_dict[0].keys())
print("---------2--------")
print("Converting dict to raw json")
docker_json = json.dumps(docker_dict)
print("---------3--------")
print("Filtering from dict")
print(docker_dict[0]["Created"])
print(docker_dict[0]["Architecture"])
print(docker_dict[0]["Os"])

print("+++++++++2++++++++")
docker_json_file2 = [
    {
        "Name": "bridge",
        "Id": "566a72fc961157e2e71cc257fc2132beebc491a712967ef42bddcab70cbdbb23",
        "Created": "2020-12-09T17:51:15.816558163Z",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": FALSE,
        "IPAM": {
            "Driver": "default",
            "Options": None,
            "Config": [
                {
                    "Subnet": "172.17.0.0/16",
                    "Gateway": "172.17.0.1"
                }
            ]
        },
        "Internal": FALSE,
        "Attachable": FALSE,
        "Ingress": FALSE,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": FALSE,
        "Containers": {
            "4e99a64e10dfcf6608a1d47f4349676c745bf234cebd52826d786db9a3be2811": {
                "Name": "samplerunning",
                "EndpointID": "22bbd3fa7e76635c3172446813fe5104537c8f69c6c23474272b379dede44fe7",
                "MacAddress": "02:42:ac:11:00:03",
                "IPv4Address": "172.17.0.3/16",
                "IPv6Address": ""
            }
        },
        "Options": {
            "com.docker.network.bridge.default_bridge": "true",
            "com.docker.network.bridge.enable_icc": "true",
            "com.docker.network.bridge.enable_ip_masquerade": "true",
            "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
            "com.docker.network.bridge.name": "docker0",
            "com.docker.network.driver.mtu": "1500"
        },
        "Labels": {}
    }
]

print("---------1--------")
print("Converting json string to dict, and showing keys at level 1")
docker_dict2 = json.loads(docker_json_file2)
print(docker_dict2[0].keys())
print("---------2--------")
print("Converting dict to raw json")
docker_json2 = json.loads(docker_dict2)
print("Filtering from dict")
print(docker_dict2[0]["Name"])
print(docker_dict2[0]["Created"])
print(docker_dict2[0]["Containers"]["4e99a64e...bd52826d786db9a3be2811"]["IPv4Address"])