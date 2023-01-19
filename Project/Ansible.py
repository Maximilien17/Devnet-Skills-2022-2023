import json


ansible_dict = {
    "ansible_facts": {
        "ansible_all_ipv4_addresses": [
            "192.0.2.1",
            "192.0.2.2",
            "192.0.2.3",
            "192.0.2.4",
            "192.0.2.5",
            "10.0.2.15",
            "172.17.0.1"
        ],
        "ansible_all_ipv6_addresses": [
            "fe80::9002:c8ff:fee8:bb09",
            "fe80::3c67:a5ff:fe17:e4cf",
            "fe80::a00:27ff:fee9:3de6",
            "fe80::42:3ff:fef6:9477"
        ],
        "ansible_apparmor": {
            "status": "enabled"
        },
        "ansible_architecture": "x86_64",
        "ansible_bios_date": "12/01/2006",
        "ansible_bios_version": "VirtualBox",
        "ansible_cmdline": {
            "BOOT_IMAGE": "/boot/vmlinuz-5.4.0-37-generic",
            "quiet": true,
            "ro": true,
            "root": "UUID=fb261367-cf98-4bce-b682-42b3de0a8ab9",
            "vga": "792",
            "zswap.enabled": "1"
        },
        "ansible_date_time": {
            "date": "2021-01-20",
            "day": "20",
            "epoch": "1611160850",
            "hour": "16",
            "iso8601": "2021-01-20T16:40:50Z",
            "iso8601_basic": "20210120T164050181658",
            "iso8601_basic_short": "20210120T164050",
            "iso8601_micro": "2021-01-20T16:40:50.181774Z",
            "minute": "40",
            "month": "01",
            "second": "50",
            "time": "16:40:50",
            "tz": "UTC",
            "tz_offset": "+0000",
            "weekday": "Wednesday",
            "weekday_number": "3",
            "weeknumber": "03",
            "year": "2021"
        },
        "ansible_default_ipv4": {
            "address": "10.0.2.15",
            "alias": "enp0s3",
            "broadcast": "10.0.2.255",
            "gateway": "10.0.2.2",
            "interface": "enp0s3",
            "macaddress": "08:00:27:e9:3d:e6",
            "mtu": 1500,
            "netmask": "255.255.255.0",
            "network": "10.0.2.0",
            "type": "ether"
        },
        "ansible_default_ipv6": {},
        "ansible_device_links": {
            "ids": {
                "sda": [
                    "ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd"
                ],
                "sda1": [
                    "ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd-part1"
                ],
                "sda2": [
                    "ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd-part2"
                ],
                "sda5": [
                    "ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd-part5"
                ]
            },
            "labels": {},
            "masters": {},
            "uuids": {
                "sda1": [
                    "AF29-5078"
                ],
                "sda5": [
                    "fb261367-cf98-4bce-b682-42b3de0a8ab9"
                ]
            }
        },
        "ansible_devices": {
            "loop0": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "0",
                "sectorsize": "512",
                "size": "0.00 Bytes",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop1": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "299016",
                "sectorsize": "512",
                "size": "146.00 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop10": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "333552",
                "sectorsize": "512",
                "size": "162.87 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop11": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "359216",
                "sectorsize": "512",
                "size": "175.40 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop12": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "132648",
                "sectorsize": "512",
                "size": "64.77 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop13": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "354400",
                "sectorsize": "512",
                "size": "173.05 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop14": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "131792",
                "sectorsize": "512",
                "size": "64.35 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop15": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "330576",
                "sectorsize": "512",
                "size": "161.41 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop16": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "242432",
                "sectorsize": "512",
                "size": "118.38 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop2": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "300120",
                "sectorsize": "512",
                "size": "146.54 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop3": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "496912",
                "sectorsize": "512",
                "size": "242.63 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop4": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "200168",
                "sectorsize": "512",
                "size": "97.74 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop5": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "113296",
                "sectorsize": "512",
                "size": "55.32 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop6": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "200416",
                "sectorsize": "512",
                "size": "97.86 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop7": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "187848",
                "sectorsize": "512",
                "size": "91.72 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop8": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "191232",
                "sectorsize": "512",
                "size": "93.38 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop9": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "113384",
                "sectorsize": "512",
                "size": "55.36 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "sda": {
                "holders": [],
                "host": "IDE interface: Intel Corporation 82371AB/EB/MB PIIX4 IDE (rev 01)",
                "links": {
                    "ids": [
                        "ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd"
                    ],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": "VBOX HARDDISK",
                "partitions": {
                    "sda1": {
                        "holders": [],
                        "links": {
                            "ids": [
                                "ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd-part1"
                            ],
                            "labels": [],
                            "masters": [],
                            "uuids": [
                                "AF29-5078"
                            ]
                        },
                        "sectors": "1048576",
                        "sectorsize": 512,
                        "size": "512.00 MB",
                        "start": "2048",
                        "uuid": "AF29-5078"
                    },
                    "sda2": {
                        "holders": [],
                        "links": {
                            "ids": [
                                "ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd-part2"
                            ],
                            "labels": [],
                            "masters": [],
                            "uuids": []
                        },
                        "sectors": "2",
                        "sectorsize": 512,
                        "size": "1.00 KB",
                        "start": "1052670",
                        "uuid": null
                    },
                    "sda5": {
                        "holders": [],
                        "links": {
                            "ids": [
                                "ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd-part5"
                            ],
                            "labels": [],
                            "masters": [],
                            "uuids": [
                                "fb261367-cf98-4bce-b682-42b3de0a8ab9"
                            ]
                        },
                        "sectors": "64481280",
                        "sectorsize": 512,
                        "size": "30.75 GB",
                        "start": "1052672",
                        "uuid": "fb261367-cf98-4bce-b682-42b3de0a8ab9"
                    }
                },
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "65536000",
                "sectorsize": "512",
                "size": "31.25 GB",
                "support_discard": "0",
                "vendor": "ATA",
                "virtual": 1
            }
        },
        "ansible_distribution": "Ubuntu",
        "ansible_distribution_file_parsed": true,
        "ansible_distribution_file_path": "/etc/os-release",
        "ansible_distribution_file_variety": "Debian",
        "ansible_distribution_major_version": "20",
        "ansible_distribution_release": "focal",
        "ansible_distribution_version": "20.04",
        "ansible_dns": {
            "nameservers": [
                "127.0.0.53"
            ],
            "options": {
                "edns0": true
            },
            "search": [
                "telenet.be"
            ]
        },
        "ansible_docker0": {
            "active": true,
            "device": "docker0",
            "features": {
                "esp_hw_offload": "off [fixed]",
                "esp_tx_csum_hw_offload": "off [fixed]",
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "on",
                "hw_tc_offload": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "off [fixed]",
                "netns_local": "on [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off [fixed]",
                "rx_checksumming": "off [fixed]",
                "rx_fcs": "off [fixed]",
                "rx_gro_hw": "off [fixed]",
                "rx_udp_tunnel_port_offload": "off [fixed]",
                "rx_vlan_filter": "off [fixed]",
                "rx_vlan_offload": "off [fixed]",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "off [fixed]",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tls_hw_record": "off [fixed]",
                "tls_hw_rx_offload": "off [fixed]",
                "tls_hw_tx_offload": "off [fixed]",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "off [fixed]",
                "tx_checksumming": "on",
                "tx_esp_segmentation": "on",
                "tx_fcoe_segmentation": "off [requested on]",
                "tx_gre_csum_segmentation": "on",
                "tx_gre_segmentation": "on",
                "tx_gso_partial": "on",
                "tx_gso_robust": "off [requested on]",
                "tx_ipxip4_segmentation": "on",
                "tx_ipxip6_segmentation": "on",
                "tx_lockless": "on [fixed]",
                "tx_nocache_copy": "off",
                "tx_scatter_gather": "on",
                "tx_scatter_gather_fraglist": "on",
                "tx_sctp_segmentation": "on",
                "tx_tcp6_segmentation": "on",
                "tx_tcp_ecn_segmentation": "on",
                "tx_tcp_mangleid_segmentation": "on",
                "tx_tcp_segmentation": "on",
                "tx_udp_segmentation": "on",
                "tx_udp_tnl_csum_segmentation": "on",
                "tx_udp_tnl_segmentation": "on",
                "tx_vlan_offload": "on",
                "tx_vlan_stag_hw_insert": "on",
                "vlan_challenged": "off [fixed]"
            },
            "hw_timestamp_filters": [],
            "id": "8000.024203f69477",
            "interfaces": [
                "vethacd0508"
            ],
            "ipv4": {
                "address": "172.17.0.1",
                "broadcast": "172.17.255.255",
                "netmask": "255.255.0.0",
                "network": "172.17.0.0"
            },
            "ipv6": [
                {
                    "address": "fe80::42:3ff:fef6:9477",
                    "prefix": "64",
                    "scope": "link"
                }
            ],
            "macaddress": "02:42:03:f6:94:77",
            "mtu": 1500,
            "promisc": false,
            "stp": false,
            "timestamping": [
                "rx_software",
                "software"
            ],
            "type": "bridge"
        },
        "ansible_domain": "vm",
        "ansible_dummy0": {
            "active": true,
            "device": "dummy0",
            "features": {
                "esp_hw_offload": "off [fixed]",
                "esp_tx_csum_hw_offload": "off [fixed]",
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "on",
                "hw_tc_offload": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "off [fixed]",
                "netns_local": "on [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off [fixed]",
                "rx_checksumming": "off [fixed]",
                "rx_fcs": "off [fixed]",
                "rx_gro_hw": "off [fixed]",
                "rx_udp_tunnel_port_offload": "off [fixed]",
                "rx_vlan_filter": "off [fixed]",
                "rx_vlan_offload": "off [fixed]",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "off [fixed]",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tls_hw_record": "off [fixed]",
                "tls_hw_rx_offload": "off [fixed]",
                "tls_hw_tx_offload": "off [fixed]",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "off [fixed]",
                "tx_checksumming": "on",
                "tx_esp_segmentation": "on",
                "tx_fcoe_segmentation": "on",
                "tx_gre_csum_segmentation": "on",
                "tx_gre_segmentation": "on",
                "tx_gso_partial": "on",
                "tx_gso_robust": "on",
                "tx_ipxip4_segmentation": "on",
                "tx_ipxip6_segmentation": "on",
                "tx_lockless": "on [fixed]",
                "tx_nocache_copy": "off",
                "tx_scatter_gather": "on",
                "tx_scatter_gather_fraglist": "on",
                "tx_sctp_segmentation": "on",
                "tx_tcp6_segmentation": "on",
                "tx_tcp_ecn_segmentation": "on",
                "tx_tcp_mangleid_segmentation": "on",
                "tx_tcp_segmentation": "on",
                "tx_udp_segmentation": "on",
                "tx_udp_tnl_csum_segmentation": "on",
                "tx_udp_tnl_segmentation": "on",
                "tx_vlan_offload": "on",
                "tx_vlan_stag_hw_insert": "on",
                "vlan_challenged": "off [fixed]"
            },
            "hw_timestamp_filters": [],
            "id": "8000.000000000000",
            "interfaces": [],
            "ipv4": {
                "address": "192.0.2.1",
                "broadcast": "global",
                "netmask": "255.255.255.255",
                "network": "192.0.2.1"
            },
            "ipv4_secondaries": [
                {
                    "address": "192.0.2.2",
                    "broadcast": "global",
                    "netmask": "255.255.255.255",
                    "network": "192.0.2.2"
                },
                {
                    "address": "192.0.2.3",
                    "broadcast": "global",
                    "netmask": "255.255.255.255",
                    "network": "192.0.2.3"
                },
                {
                    "address": "192.0.2.4",
                    "broadcast": "global",
                    "netmask": "255.255.255.255",
                    "network": "192.0.2.4"
                },
                {
                    "address": "192.0.2.5",
                    "broadcast": "global",
                    "netmask": "255.255.255.255",
                    "network": "192.0.2.5"
                }
            ],
            "ipv6": [
                {
                    "address": "fe80::9002:c8ff:fee8:bb09",
                    "prefix": "64",
                    "scope": "link"
                }
            ],
            "macaddress": "92:02:c8:e8:bb:09",
            "mtu": 1500,
            "promisc": false,
            "stp": false,
            "timestamping": [
                "rx_software",
                "software"
            ],
            "type": "bridge"
        },
        "ansible_effective_group_id": 900,
        "ansible_effective_user_id": 900,
        "ansible_enp0s3": {
            "active": true,
            "device": "enp0s3",
            "features": {
                "esp_hw_offload": "off [fixed]",
                "esp_tx_csum_hw_offload": "off [fixed]",
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "off [fixed]",
                "hw_tc_offload": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "off [fixed]",
                "netns_local": "off [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off",
                "rx_checksumming": "off",
                "rx_fcs": "off",
                "rx_gro_hw": "off [fixed]",
                "rx_udp_tunnel_port_offload": "off [fixed]",
                "rx_vlan_filter": "on [fixed]",
                "rx_vlan_offload": "on",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "off [fixed]",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tls_hw_record": "off [fixed]",
                "tls_hw_rx_offload": "off [fixed]",
                "tls_hw_tx_offload": "off [fixed]",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "off [fixed]",
                "tx_checksumming": "on",
                "tx_esp_segmentation": "off [fixed]",
                "tx_fcoe_segmentation": "off [fixed]",
                "tx_gre_csum_segmentation": "off [fixed]",
                "tx_gre_segmentation": "off [fixed]",
                "tx_gso_partial": "off [fixed]",
                "tx_gso_robust": "off [fixed]",
                "tx_ipxip4_segmentation": "off [fixed]",
                "tx_ipxip6_segmentation": "off [fixed]",
                "tx_lockless": "off [fixed]",
                "tx_nocache_copy": "off",
                "tx_scatter_gather": "on",
                "tx_scatter_gather_fraglist": "off [fixed]",
                "tx_sctp_segmentation": "off [fixed]",
                "tx_tcp6_segmentation": "off [fixed]",
                "tx_tcp_ecn_segmentation": "off [fixed]",
                "tx_tcp_mangleid_segmentation": "off",
                "tx_tcp_segmentation": "on",
                "tx_udp_segmentation": "off [fixed]",
                "tx_udp_tnl_csum_segmentation": "off [fixed]",
                "tx_udp_tnl_segmentation": "off [fixed]",
                "tx_vlan_offload": "on [fixed]",
                "tx_vlan_stag_hw_insert": "off [fixed]",
                "vlan_challenged": "off [fixed]"
            },
            "hw_timestamp_filters": [],
            "ipv4": {
                "address": "10.0.2.15",
                "broadcast": "10.0.2.255",
                "netmask": "255.255.255.0",
                "network": "10.0.2.0"
            },
            "ipv6": [
                {
                    "address": "fe80::a00:27ff:fee9:3de6",
                    "prefix": "64",
                    "scope": "link"
                }
            ],
            "macaddress": "08:00:27:e9:3d:e6",
            "module": "e1000",
            "mtu": 1500,
            "pciid": "0000:00:03.0",
            "promisc": false,
            "speed": 1000,
            "timestamping": [
                "tx_software",
                "rx_software",
                "software"
            ],
            "type": "ether"
        },
        "ansible_env": {
            "DBUS_SESSION_BUS_ADDRESS": "unix:path=/run/user/900/bus",
            "HOME": "/home/devasc",
            "LANG": "en_US.UTF-8",
            "LANGUAGE": "en_US:",
            "LOGNAME": "devasc",
            "MOTD_SHOWN": "pam",
            "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin",
            "PWD": "/home/devasc",
            "SHELL": "/bin/bash",
            "SHLVL": "0",
            "SSH_CLIENT": "192.0.2.3 55752 22",
            "SSH_CONNECTION": "192.0.2.3 55752 192.0.2.3 22",
            "SSH_TTY": "/dev/pts/3",
            "TERM": "xterm-256color",
            "USER": "devasc",
            "XDG_RUNTIME_DIR": "/run/user/900",
            "XDG_SESSION_CLASS": "user",
            "XDG_SESSION_ID": "50",
            "XDG_SESSION_TYPE": "tty",
            "_": "/bin/sh"
        },
        "ansible_fibre_channel_wwn": [],
        "ansible_fips": false,
        "ansible_form_factor": "Other",
        "ansible_fqdn": "labvm.vm",
        "ansible_hostname": "labvm",
        "ansible_hostnqn": "",
        "ansible_interfaces": [
            "dummy0",
            "lo",
            "vethacd0508",
            "docker0",
            "enp0s3"
        ],
        "ansible_is_chroot": false,
        "ansible_iscsi_iqn": "",
        "ansible_kernel": "5.4.0-37-generic",
        "ansible_kernel_version": "#41-Ubuntu SMP Wed Jun 3 18:57:02 UTC 2020",
        "ansible_lo": {
            "active": true,
            "device": "lo",
            "features": {
                "esp_hw_offload": "off [fixed]",
                "esp_tx_csum_hw_offload": "off [fixed]",
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "on [fixed]",
                "hw_tc_offload": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "on [fixed]",
                "netns_local": "on [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off [fixed]",
                "rx_checksumming": "on [fixed]",
                "rx_fcs": "off [fixed]",
                "rx_gro_hw": "off [fixed]",
                "rx_udp_tunnel_port_offload": "off [fixed]",
                "rx_vlan_filter": "off [fixed]",
                "rx_vlan_offload": "off [fixed]",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "off [fixed]",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tls_hw_record": "off [fixed]",
                "tls_hw_rx_offload": "off [fixed]",
                "tls_hw_tx_offload": "off [fixed]",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on [fixed]",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "on [fixed]",
                "tx_checksumming": "on",
                "tx_esp_segmentation": "off [fixed]",
                "tx_fcoe_segmentation": "off [fixed]",
                "tx_gre_csum_segmentation": "off [fixed]",
                "tx_gre_segmentation": "off [fixed]",
                "tx_gso_partial": "off [fixed]",
                "tx_gso_robust": "off [fixed]",
                "tx_ipxip4_segmentation": "off [fixed]",
                "tx_ipxip6_segmentation": "off [fixed]",
                "tx_lockless": "on [fixed]",
                "tx_nocache_copy": "off [fixed]",
                "tx_scatter_gather": "on [fixed]",
                "tx_scatter_gather_fraglist": "on [fixed]",
                "tx_sctp_segmentation": "on",
                "tx_tcp6_segmentation": "on",
                "tx_tcp_ecn_segmentation": "on",
                "tx_tcp_mangleid_segmentation": "on",
                "tx_tcp_segmentation": "on",
                "tx_udp_segmentation": "off [fixed]",
                "tx_udp_tnl_csum_segmentation": "off [fixed]",
                "tx_udp_tnl_segmentation": "off [fixed]",
                "tx_vlan_offload": "off [fixed]",
                "tx_vlan_stag_hw_insert": "off [fixed]",
                "vlan_challenged": "on [fixed]"
            },
            "hw_timestamp_filters": [],
            "ipv4": {
                "address": "127.0.0.1",
                "broadcast": "host",
                "netmask": "255.0.0.0",
                "network": "127.0.0.0"
            },
            "ipv6": [
                {
                    "address": "::1",
                    "prefix": "128",
                    "scope": "host"
                }
            ],
            "mtu": 65536,
            "promisc": false,
            "timestamping": [
                "tx_software",
                "rx_software",
                "software"
            ],
            "type": "loopback"
        },
        "ansible_local": {},
        "ansible_lsb": {
            "codename": "focal",
            "description": "Ubuntu 20.04.1 LTS",
            "id": "Ubuntu",
            "major_release": "20",
            "release": "20.04"
        },
        "ansible_machine": "x86_64",
        "ansible_machine_id": "c6a52afed8564edfa075a362c20348b8",
        "ansible_memfree_mb": 258,
        "ansible_memory_mb": {
            "nocache": {
                "free": 2209,
                "used": 1727
            },
            "real": {
                "free": 258,
                "total": 3936,
                "used": 3678
            },
            "swap": {
                "cached": 2,
                "free": 1979,
                "total": 2047,
                "used": 68
            }
        },
        "ansible_memtotal_mb": 3936,
        "ansible_mounts": [
            {
                "block_available": 2011759,
                "block_size": 4096,
                "block_total": 7900888,
                "block_used": 5889129,
                "device": "/dev/sda5",
                "fstype": "ext4",
                "inode_available": 1582129,
                "inode_total": 2015232,
                "inode_used": 433103,
                "mount": "/",
                "options": "rw,relatime,errors=remount-ro",
                "size_available": 8240164864,
                "size_total": 32362037248,
                "uuid": "fb261367-cf98-4bce-b682-42b3de0a8ab9"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 1942,
                "block_used": 1942,
                "device": "/dev/loop3",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 10774,
                "inode_used": 10774,
                "mount": "/snap/chromium/1421",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 254541824,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 782,
                "block_used": 782,
                "device": "/dev/loop4",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 12826,
                "inode_used": 12826,
                "mount": "/snap/core/10185",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 102498304,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 443,
                "block_used": 443,
                "device": "/dev/loop5",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 10775,
                "inode_used": 10775,
                "mount": "/snap/core18/1885",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 58064896,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 1169,
                "block_used": 1169,
                "device": "/dev/loop1",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 4197,
                "inode_used": 4197,
                "mount": "/snap/code/50",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 153223168,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 783,
                "block_used": 783,
                "device": "/dev/loop6",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 12867,
                "inode_used": 12867,
                "mount": "/snap/core/10444",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 102629376,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 734,
                "block_used": 734,
                "device": "/dev/loop7",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 132,
                "inode_used": 132,
                "mount": "/snap/drawio/80",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 96206848,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 747,
                "block_used": 747,
                "device": "/dev/loop8",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 132,
                "inode_used": 132,
                "mount": "/snap/drawio/84",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 97910784,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 443,
                "block_used": 443,
                "device": "/dev/loop9",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 10779,
                "inode_used": 10779,
                "mount": "/snap/core18/1932",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 58064896,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 1303,
                "block_used": 1303,
                "device": "/dev/loop10",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 27807,
                "inode_used": 27807,
                "mount": "/snap/gnome-3-28-1804/145",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 170786816,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 519,
                "block_used": 519,
                "device": "/dev/loop12",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 63978,
                "inode_used": 63978,
                "mount": "/snap/gtk-common-themes/1514",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 68026368,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 1404,
                "block_used": 1404,
                "device": "/dev/loop11",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 44282,
                "inode_used": 44282,
                "mount": "/snap/postman/129",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 184025088,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 1385,
                "block_used": 1385,
                "device": "/dev/loop13",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 45118,
                "inode_used": 45118,
                "mount": "/snap/postman/128",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 181534720,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 515,
                "block_used": 515,
                "device": "/dev/loop14",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 63811,
                "inode_used": 63811,
                "mount": "/snap/gtk-common-themes/1513",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 67502080,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 1292,
                "block_used": 1292,
                "device": "/dev/loop15",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 27798,
                "inode_used": 27798,
                "mount": "/snap/gnome-3-28-1804/128",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 169345024,
                "uuid": "N/A"
            },
            {
                "block_available": 130811,
                "block_size": 4096,
                "block_total": 130812,
                "block_used": 1,
                "device": "/dev/sda1",
                "fstype": "vfat",
                "inode_available": 0,
                "inode_total": 0,
                "inode_used": 0,
                "mount": "/boot/efi",
                "options": "rw,relatime,fmask=0077,dmask=0077,codepage=437,iocharset=iso8859-1,shortname=mixed,errors=remount-ro",
                "size_available": 535801856,
                "size_total": 535805952,
                "uuid": "AF29-5078"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 947,
                "block_used": 947,
                "device": "/dev/loop16",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 1330,
                "inode_used": 1330,
                "mount": "/snap/chromium/1424",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 124125184,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 1173,
                "block_used": 1173,
                "device": "/dev/loop2",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 4207,
                "inode_used": 4207,
                "mount": "/snap/code/51",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 153747456,
                "uuid": "N/A"
            }
        ],
        "ansible_nodename": "labvm",
        "ansible_os_family": "Debian",
        "ansible_pkg_mgr": "apt",
        "ansible_proc_cmdline": {
            "BOOT_IMAGE": "/boot/vmlinuz-5.4.0-37-generic",
            "quiet": true,
            "ro": true,
            "root": "UUID=fb261367-cf98-4bce-b682-42b3de0a8ab9",
            "vga": "792",
            "zswap.enabled": "1"
        },
        "ansible_processor": [
            "0",
            "GenuineIntel",
            "Intel(R) Core(TM) i7-7600U CPU @ 2.80GHz",
            "1",
            "GenuineIntel",
            "Intel(R) Core(TM) i7-7600U CPU @ 2.80GHz"
        ],
        "ansible_processor_cores": 2,
        "ansible_processor_count": 1,
        "ansible_processor_threads_per_core": 1,
        "ansible_processor_vcpus": 2,
        "ansible_product_name": "VirtualBox",
        "ansible_product_serial": "NA",
        "ansible_product_uuid": "NA",
        "ansible_product_version": "1.2",
        "ansible_python": {
            "executable": "/usr/bin/python3",
            "has_sslcontext": true,
            "type": "cpython",
            "version": {
                "major": 3,
                "micro": 2,
                "minor": 8,
                "releaselevel": "final",
                "serial": 0
            },
            "version_info": [
                3,
                8,
                2,
                "final",
                0
            ]
        },
        "ansible_python_version": "3.8.2",
        "ansible_real_group_id": 900,
        "ansible_real_user_id": 900,
        "ansible_selinux": {
            "status": "disabled"
        },
        "ansible_selinux_python_present": true,
        "ansible_service_mgr": "systemd",
        "ansible_ssh_host_key_ecdsa_public": "AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPFM1OVBLhbMfZVSkIVrPTq0FcKqNM9vRuBawNKkevM0UoDO5PwzaDCS6Hry9lvKuJIP+aB5KNnQ0P6uZfHdpFc=",
        "ansible_ssh_host_key_ed25519_public": "AAAAC3NzaC1lZDI1NTE5AAAAIC5pTSLWhV+w/qgqcGewKBfdDczo4VhV3VWp1lLHH7U+",
        "ansible_ssh_host_key_rsa_public": "AAAAB3NzaC1yc2EAAAADAQABAAABgQCpwiwXYyl8eNmZO2dfWYyV1V1pnoq/tZjXF9ABBSSsR7KHny7SP4muQvLErLc2wOlvzsYq5l/NQoYuIeY7eGK3dffACUwda9V1Ub6AjcNQIdwLypUt1zW3Q/9e8/VfnmVGr5IeIvt02L362V4jFfLYd8QZxqlzWO7ah8bODyvGP68VP6pE7Hd+XamJAwMHH0NquCeRW5JO6xWaTVvZUiNGVYSTl0OFDuXX/CbXVXMjaaPF1ZJuLtpmfxAcmtIKRqHUmy0wWRah3GXiLwpAR4i50jlgE84Y1swqEpMneAM/nanFwrCEMBmf54olazJ1e3redxIyWFCDwhZO+Q0sZoruS3OXfpsr9/33uksfjP4TiQHy84Xn5WhR/VRRsCyqA7adn/4FmtUtbOR0eaD3pBPGElocCSy7p/wOO18B6Bfa0BSoh8si+ShBNxNVuULw2/iCebRbReXaw9xbfNFx5bJVSfJmZfJvRVpQV9HVZYV2apKuHyFbwLROAf0NRwAJxm8=",
        "ansible_swapfree_mb": 1979,
        "ansible_swaptotal_mb": 2047,
        "ansible_system": "Linux",
        "ansible_system_capabilities": [
            ""
        ],
        "ansible_system_capabilities_enforced": "True",
        "ansible_system_vendor": "innotek GmbH",
        "ansible_uptime_seconds": 88854,
        "ansible_user_dir": "/home/devasc",
        "ansible_user_gecos": "DevNet Associate,,,",
        "ansible_user_gid": 900,
        "ansible_user_id": "devasc",
        "ansible_user_shell": "/bin/bash",
        "ansible_user_uid": 900,
        "ansible_userspace_architecture": "x86_64",
        "ansible_userspace_bits": "64",
        "ansible_vethacd0508": {
            "active": true,
            "device": "vethacd0508",
            "features": {
                "esp_hw_offload": "off [fixed]",
                "esp_tx_csum_hw_offload": "off [fixed]",
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "on",
                "hw_tc_offload": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "off [fixed]",
                "netns_local": "off [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off [fixed]",
                "rx_checksumming": "on",
                "rx_fcs": "off [fixed]",
                "rx_gro_hw": "off [fixed]",
                "rx_udp_tunnel_port_offload": "off [fixed]",
                "rx_vlan_filter": "off [fixed]",
                "rx_vlan_offload": "on",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "on",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tls_hw_record": "off [fixed]",
                "tls_hw_rx_offload": "off [fixed]",
                "tls_hw_tx_offload": "off [fixed]",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "on",
                "tx_checksumming": "on",
                "tx_esp_segmentation": "off [fixed]",
                "tx_fcoe_segmentation": "off [fixed]",
                "tx_gre_csum_segmentation": "on",
                "tx_gre_segmentation": "on",
                "tx_gso_partial": "off [fixed]",
                "tx_gso_robust": "off [fixed]",
                "tx_ipxip4_segmentation": "on",
                "tx_ipxip6_segmentation": "on",
                "tx_lockless": "on [fixed]",
                "tx_nocache_copy": "off",
                "tx_scatter_gather": "on",
                "tx_scatter_gather_fraglist": "on",
                "tx_sctp_segmentation": "on",
                "tx_tcp6_segmentation": "on",
                "tx_tcp_ecn_segmentation": "on",
                "tx_tcp_mangleid_segmentation": "on",
                "tx_tcp_segmentation": "on",
                "tx_udp_segmentation": "off [fixed]",
                "tx_udp_tnl_csum_segmentation": "on",
                "tx_udp_tnl_segmentation": "on",
                "tx_vlan_offload": "on",
                "tx_vlan_stag_hw_insert": "on",
                "vlan_challenged": "off [fixed]"
            },
            "hw_timestamp_filters": [],
            "ipv6": [
                {
                    "address": "fe80::3c67:a5ff:fe17:e4cf",
                    "prefix": "64",
                    "scope": "link"
                }
            ],
            "macaddress": "3e:67:a5:17:e4:cf",
            "mtu": 1500,
            "promisc": true,
            "speed": 10000,
            "timestamping": [
                "tx_software",
                "rx_software",
                "software"
            ],
            "type": "ether"
        },
        "ansible_virtualization_role": "guest",
        "ansible_virtualization_type": "virtualbox",
        "discovered_interpreter_python": "/usr/bin/python3",
        "gather_subset": [
            "all"
        ],
        "module_setup": true
    },
    "changed": false,
    "deprecations": [],
    "warnings": []
}

{
    "ansible_facts": {
        "ansible_all_ipv4_addresses": [
            "192.0.2.1",
            "192.0.2.2",
            "192.0.2.3",
            "192.0.2.4",
            "192.0.2.5",
            "10.0.2.15",
            "172.17.0.1"
        ],
        "ansible_all_ipv6_addresses": [
            "fe80::9002:c8ff:fee8:bb09",
            "fe80::3c67:a5ff:fe17:e4cf",
            "fe80::a00:27ff:fee9:3de6",
            "fe80::42:3ff:fef6:9477"
        ],
        "ansible_apparmor": {
            "status": "enabled"
        },
        "ansible_architecture": "x86_64",
        "ansible_bios_date": "12/01/2006",
        "ansible_bios_version": "VirtualBox",
        "ansible_cmdline": {
            "BOOT_IMAGE": "/boot/vmlinuz-5.4.0-37-generic",
            "quiet": true,
            "ro": true,
            "root": "UUID=fb261367-cf98-4bce-b682-42b3de0a8ab9",
            "vga": "792",
            "zswap.enabled": "1"
        },
        "ansible_date_time": {
            "date": "2021-01-20",
            "day": "20",
            "epoch": "1611160850",
            "hour": "16",
            "iso8601": "2021-01-20T16:40:50Z",
            "iso8601_basic": "20210120T164050181658",
            "iso8601_basic_short": "20210120T164050",
            "iso8601_micro": "2021-01-20T16:40:50.181774Z",
            "minute": "40",
            "month": "01",
            "second": "50",
            "time": "16:40:50",
            "tz": "UTC",
            "tz_offset": "+0000",
            "weekday": "Wednesday",
            "weekday_number": "3",
            "weeknumber": "03",
            "year": "2021"
        },
        "ansible_default_ipv4": {
            "address": "10.0.2.15",
            "alias": "enp0s3",
            "broadcast": "10.0.2.255",
            "gateway": "10.0.2.2",
            "interface": "enp0s3",
            "macaddress": "08:00:27:e9:3d:e6",
            "mtu": 1500,
            "netmask": "255.255.255.0",
            "network": "10.0.2.0",
            "type": "ether"
        },
        "ansible_default_ipv6": {},
        "ansible_device_links": {
            "ids": {
                "sda": [
                    "ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd"
                ],
                "sda1": [
                    "ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd-part1"
                ],
                "sda2": [
                    "ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd-part2"
                ],
                "sda5": [
                    "ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd-part5"
                ]
            },
            "labels": {},
            "masters": {},
            "uuids": {
                "sda1": [
                    "AF29-5078"
                ],
                "sda5": [
                    "fb261367-cf98-4bce-b682-42b3de0a8ab9"
                ]
            }
        },
        "ansible_devices": {
            "loop0": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "0",
                "sectorsize": "512",
                "size": "0.00 Bytes",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop1": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "299016",
                "sectorsize": "512",
                "size": "146.00 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop10": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "333552",
                "sectorsize": "512",
                "size": "162.87 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop11": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "359216",
                "sectorsize": "512",
                "size": "175.40 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop12": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "132648",
                "sectorsize": "512",
                "size": "64.77 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop13": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "354400",
                "sectorsize": "512",
                "size": "173.05 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop14": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "131792",
                "sectorsize": "512",
                "size": "64.35 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop15": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "330576",
                "sectorsize": "512",
                "size": "161.41 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop16": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "242432",
                "sectorsize": "512",
                "size": "118.38 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop2": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "300120",
                "sectorsize": "512",
                "size": "146.54 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop3": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "496912",
                "sectorsize": "512",
                "size": "242.63 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop4": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "200168",
                "sectorsize": "512",
                "size": "97.74 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop5": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "113296",
                "sectorsize": "512",
                "size": "55.32 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop6": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "200416",
                "sectorsize": "512",
                "size": "97.86 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop7": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "187848",
                "sectorsize": "512",
                "size": "91.72 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop8": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "191232",
                "sectorsize": "512",
                "size": "93.38 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "loop9": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "113384",
                "sectorsize": "512",
                "size": "55.36 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "sda": {
                "holders": [],
                "host": "IDE interface: Intel Corporation 82371AB/EB/MB PIIX4 IDE (rev 01)",
                "links": {
                    "ids": [
                        "ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd"
                    ],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": "VBOX HARDDISK",
                "partitions": {
                    "sda1": {
                        "holders": [],
                        "links": {
                            "ids": [
                                "ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd-part1"
                            ],
                            "labels": [],
                            "masters": [],
                            "uuids": [
                                "AF29-5078"
                            ]
                        },
                        "sectors": "1048576",
                        "sectorsize": 512,
                        "size": "512.00 MB",
                        "start": "2048",
                        "uuid": "AF29-5078"
                    },
                    "sda2": {
                        "holders": [],
                        "links": {
                            "ids": [
                                "ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd-part2"
                            ],
                            "labels": [],
                            "masters": [],
                            "uuids": []
                        },
                        "sectors": "2",
                        "sectorsize": 512,
                        "size": "1.00 KB",
                        "start": "1052670",
                        "uuid": null
                    },
                    "sda5": {
                        "holders": [],
                        "links": {
                            "ids": [
                                "ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd-part5"
                            ],
                            "labels": [],
                            "masters": [],
                            "uuids": [
                                "fb261367-cf98-4bce-b682-42b3de0a8ab9"
                            ]
                        },
                        "sectors": "64481280",
                        "sectorsize": 512,
                        "size": "30.75 GB",
                        "start": "1052672",
                        "uuid": "fb261367-cf98-4bce-b682-42b3de0a8ab9"
                    }
                },
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "mq-deadline",
                "sectors": "65536000",
                "sectorsize": "512",
                "size": "31.25 GB",
                "support_discard": "0",
                "vendor": "ATA",
                "virtual": 1
            }
        },
        "ansible_distribution": "Ubuntu",
        "ansible_distribution_file_parsed": true,
        "ansible_distribution_file_path": "/etc/os-release",
        "ansible_distribution_file_variety": "Debian",
        "ansible_distribution_major_version": "20",
        "ansible_distribution_release": "focal",
        "ansible_distribution_version": "20.04",
        "ansible_dns": {
            "nameservers": [
                "127.0.0.53"
            ],
            "options": {
                "edns0": true
            },
            "search": [
                "telenet.be"
            ]
        },
        "ansible_docker0": {
            "active": true,
            "device": "docker0",
            "features": {
                "esp_hw_offload": "off [fixed]",
                "esp_tx_csum_hw_offload": "off [fixed]",
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "on",
                "hw_tc_offload": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "off [fixed]",
                "netns_local": "on [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off [fixed]",
                "rx_checksumming": "off [fixed]",
                "rx_fcs": "off [fixed]",
                "rx_gro_hw": "off [fixed]",
                "rx_udp_tunnel_port_offload": "off [fixed]",
                "rx_vlan_filter": "off [fixed]",
                "rx_vlan_offload": "off [fixed]",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "off [fixed]",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tls_hw_record": "off [fixed]",
                "tls_hw_rx_offload": "off [fixed]",
                "tls_hw_tx_offload": "off [fixed]",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "off [fixed]",
                "tx_checksumming": "on",
                "tx_esp_segmentation": "on",
                "tx_fcoe_segmentation": "off [requested on]",
                "tx_gre_csum_segmentation": "on",
                "tx_gre_segmentation": "on",
                "tx_gso_partial": "on",
                "tx_gso_robust": "off [requested on]",
                "tx_ipxip4_segmentation": "on",
                "tx_ipxip6_segmentation": "on",
                "tx_lockless": "on [fixed]",
                "tx_nocache_copy": "off",
                "tx_scatter_gather": "on",
                "tx_scatter_gather_fraglist": "on",
                "tx_sctp_segmentation": "on",
                "tx_tcp6_segmentation": "on",
                "tx_tcp_ecn_segmentation": "on",
                "tx_tcp_mangleid_segmentation": "on",
                "tx_tcp_segmentation": "on",
                "tx_udp_segmentation": "on",
                "tx_udp_tnl_csum_segmentation": "on",
                "tx_udp_tnl_segmentation": "on",
                "tx_vlan_offload": "on",
                "tx_vlan_stag_hw_insert": "on",
                "vlan_challenged": "off [fixed]"
            },
            "hw_timestamp_filters": [],
            "id": "8000.024203f69477",
            "interfaces": [
                "vethacd0508"
            ],
            "ipv4": {
                "address": "172.17.0.1",
                "broadcast": "172.17.255.255",
                "netmask": "255.255.0.0",
                "network": "172.17.0.0"
            },
            "ipv6": [
                {
                    "address": "fe80::42:3ff:fef6:9477",
                    "prefix": "64",
                    "scope": "link"
                }
            ],
            "macaddress": "02:42:03:f6:94:77",
            "mtu": 1500,
            "promisc": false,
            "stp": false,
            "timestamping": [
                "rx_software",
                "software"
            ],
            "type": "bridge"
        },
        "ansible_domain": "vm",
        "ansible_dummy0": {
            "active": true,
            "device": "dummy0",
            "features": {
                "esp_hw_offload": "off [fixed]",
                "esp_tx_csum_hw_offload": "off [fixed]",
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "on",
                "hw_tc_offload": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "off [fixed]",
                "netns_local": "on [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off [fixed]",
                "rx_checksumming": "off [fixed]",
                "rx_fcs": "off [fixed]",
                "rx_gro_hw": "off [fixed]",
                "rx_udp_tunnel_port_offload": "off [fixed]",
                "rx_vlan_filter": "off [fixed]",
                "rx_vlan_offload": "off [fixed]",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "off [fixed]",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tls_hw_record": "off [fixed]",
                "tls_hw_rx_offload": "off [fixed]",
                "tls_hw_tx_offload": "off [fixed]",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "off [fixed]",
                "tx_checksumming": "on",
                "tx_esp_segmentation": "on",
                "tx_fcoe_segmentation": "on",
                "tx_gre_csum_segmentation": "on",
                "tx_gre_segmentation": "on",
                "tx_gso_partial": "on",
                "tx_gso_robust": "on",
                "tx_ipxip4_segmentation": "on",
                "tx_ipxip6_segmentation": "on",
                "tx_lockless": "on [fixed]",
                "tx_nocache_copy": "off",
                "tx_scatter_gather": "on",
                "tx_scatter_gather_fraglist": "on",
                "tx_sctp_segmentation": "on",
                "tx_tcp6_segmentation": "on",
                "tx_tcp_ecn_segmentation": "on",
                "tx_tcp_mangleid_segmentation": "on",
                "tx_tcp_segmentation": "on",
                "tx_udp_segmentation": "on",
                "tx_udp_tnl_csum_segmentation": "on",
                "tx_udp_tnl_segmentation": "on",
                "tx_vlan_offload": "on",
                "tx_vlan_stag_hw_insert": "on",
                "vlan_challenged": "off [fixed]"
            },
            "hw_timestamp_filters": [],
            "id": "8000.000000000000",
            "interfaces": [],
            "ipv4": {
                "address": "192.0.2.1",
                "broadcast": "global",
                "netmask": "255.255.255.255",
                "network": "192.0.2.1"
            },
            "ipv4_secondaries": [
                {
                    "address": "192.0.2.2",
                    "broadcast": "global",
                    "netmask": "255.255.255.255",
                    "network": "192.0.2.2"
                },
                {
                    "address": "192.0.2.3",
                    "broadcast": "global",
                    "netmask": "255.255.255.255",
                    "network": "192.0.2.3"
                },
                {
                    "address": "192.0.2.4",
                    "broadcast": "global",
                    "netmask": "255.255.255.255",
                    "network": "192.0.2.4"
                },
                {
                    "address": "192.0.2.5",
                    "broadcast": "global",
                    "netmask": "255.255.255.255",
                    "network": "192.0.2.5"
                }
            ],
            "ipv6": [
                {
                    "address": "fe80::9002:c8ff:fee8:bb09",
                    "prefix": "64",
                    "scope": "link"
                }
            ],
            "macaddress": "92:02:c8:e8:bb:09",
            "mtu": 1500,
            "promisc": false,
            "stp": false,
            "timestamping": [
                "rx_software",
                "software"
            ],
            "type": "bridge"
        },
        "ansible_effective_group_id": 900,
        "ansible_effective_user_id": 900,
        "ansible_enp0s3": {
            "active": true,
            "device": "enp0s3",
            "features": {
                "esp_hw_offload": "off [fixed]",
                "esp_tx_csum_hw_offload": "off [fixed]",
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "off [fixed]",
                "hw_tc_offload": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "off [fixed]",
                "netns_local": "off [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off",
                "rx_checksumming": "off",
                "rx_fcs": "off",
                "rx_gro_hw": "off [fixed]",
                "rx_udp_tunnel_port_offload": "off [fixed]",
                "rx_vlan_filter": "on [fixed]",
                "rx_vlan_offload": "on",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "off [fixed]",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tls_hw_record": "off [fixed]",
                "tls_hw_rx_offload": "off [fixed]",
                "tls_hw_tx_offload": "off [fixed]",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "off [fixed]",
                "tx_checksumming": "on",
                "tx_esp_segmentation": "off [fixed]",
                "tx_fcoe_segmentation": "off [fixed]",
                "tx_gre_csum_segmentation": "off [fixed]",
                "tx_gre_segmentation": "off [fixed]",
                "tx_gso_partial": "off [fixed]",
                "tx_gso_robust": "off [fixed]",
                "tx_ipxip4_segmentation": "off [fixed]",
                "tx_ipxip6_segmentation": "off [fixed]",
                "tx_lockless": "off [fixed]",
                "tx_nocache_copy": "off",
                "tx_scatter_gather": "on",
                "tx_scatter_gather_fraglist": "off [fixed]",
                "tx_sctp_segmentation": "off [fixed]",
                "tx_tcp6_segmentation": "off [fixed]",
                "tx_tcp_ecn_segmentation": "off [fixed]",
                "tx_tcp_mangleid_segmentation": "off",
                "tx_tcp_segmentation": "on",
                "tx_udp_segmentation": "off [fixed]",
                "tx_udp_tnl_csum_segmentation": "off [fixed]",
                "tx_udp_tnl_segmentation": "off [fixed]",
                "tx_vlan_offload": "on [fixed]",
                "tx_vlan_stag_hw_insert": "off [fixed]",
                "vlan_challenged": "off [fixed]"
            },
            "hw_timestamp_filters": [],
            "ipv4": {
                "address": "10.0.2.15",
                "broadcast": "10.0.2.255",
                "netmask": "255.255.255.0",
                "network": "10.0.2.0"
            },
            "ipv6": [
                {
                    "address": "fe80::a00:27ff:fee9:3de6",
                    "prefix": "64",
                    "scope": "link"
                }
            ],
            "macaddress": "08:00:27:e9:3d:e6",
            "module": "e1000",
            "mtu": 1500,
            "pciid": "0000:00:03.0",
            "promisc": false,
            "speed": 1000,
            "timestamping": [
                "tx_software",
                "rx_software",
                "software"
            ],
            "type": "ether"
        },
        "ansible_env": {
            "DBUS_SESSION_BUS_ADDRESS": "unix:path=/run/user/900/bus",
            "HOME": "/home/devasc",
            "LANG": "en_US.UTF-8",
            "LANGUAGE": "en_US:",
            "LOGNAME": "devasc",
            "MOTD_SHOWN": "pam",
            "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin",
            "PWD": "/home/devasc",
            "SHELL": "/bin/bash",
            "SHLVL": "0",
            "SSH_CLIENT": "192.0.2.3 55752 22",
            "SSH_CONNECTION": "192.0.2.3 55752 192.0.2.3 22",
            "SSH_TTY": "/dev/pts/3",
            "TERM": "xterm-256color",
            "USER": "devasc",
            "XDG_RUNTIME_DIR": "/run/user/900",
            "XDG_SESSION_CLASS": "user",
            "XDG_SESSION_ID": "50",
            "XDG_SESSION_TYPE": "tty",
            "_": "/bin/sh"
        },
        "ansible_fibre_channel_wwn": [],
        "ansible_fips": false,
        "ansible_form_factor": "Other",
        "ansible_fqdn": "labvm.vm",
        "ansible_hostname": "labvm",
        "ansible_hostnqn": "",
        "ansible_interfaces": [
            "dummy0",
            "lo",
            "vethacd0508",
            "docker0",
            "enp0s3"
        ],
        "ansible_is_chroot": false,
        "ansible_iscsi_iqn": "",
        "ansible_kernel": "5.4.0-37-generic",
        "ansible_kernel_version": "#41-Ubuntu SMP Wed Jun 3 18:57:02 UTC 2020",
        "ansible_lo": {
            "active": true,
            "device": "lo",
            "features": {
                "esp_hw_offload": "off [fixed]",
                "esp_tx_csum_hw_offload": "off [fixed]",
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "on [fixed]",
                "hw_tc_offload": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "on [fixed]",
                "netns_local": "on [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off [fixed]",
                "rx_checksumming": "on [fixed]",
                "rx_fcs": "off [fixed]",
                "rx_gro_hw": "off [fixed]",
                "rx_udp_tunnel_port_offload": "off [fixed]",
                "rx_vlan_filter": "off [fixed]",
                "rx_vlan_offload": "off [fixed]",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "off [fixed]",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tls_hw_record": "off [fixed]",
                "tls_hw_rx_offload": "off [fixed]",
                "tls_hw_tx_offload": "off [fixed]",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on [fixed]",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "on [fixed]",
                "tx_checksumming": "on",
                "tx_esp_segmentation": "off [fixed]",
                "tx_fcoe_segmentation": "off [fixed]",
                "tx_gre_csum_segmentation": "off [fixed]",
                "tx_gre_segmentation": "off [fixed]",
                "tx_gso_partial": "off [fixed]",
                "tx_gso_robust": "off [fixed]",
                "tx_ipxip4_segmentation": "off [fixed]",
                "tx_ipxip6_segmentation": "off [fixed]",
                "tx_lockless": "on [fixed]",
                "tx_nocache_copy": "off [fixed]",
                "tx_scatter_gather": "on [fixed]",
                "tx_scatter_gather_fraglist": "on [fixed]",
                "tx_sctp_segmentation": "on",
                "tx_tcp6_segmentation": "on",
                "tx_tcp_ecn_segmentation": "on",
                "tx_tcp_mangleid_segmentation": "on",
                "tx_tcp_segmentation": "on",
                "tx_udp_segmentation": "off [fixed]",
                "tx_udp_tnl_csum_segmentation": "off [fixed]",
                "tx_udp_tnl_segmentation": "off [fixed]",
                "tx_vlan_offload": "off [fixed]",
                "tx_vlan_stag_hw_insert": "off [fixed]",
                "vlan_challenged": "on [fixed]"
            },
            "hw_timestamp_filters": [],
            "ipv4": {
                "address": "127.0.0.1",
                "broadcast": "host",
                "netmask": "255.0.0.0",
                "network": "127.0.0.0"
            },
            "ipv6": [
                {
                    "address": "::1",
                    "prefix": "128",
                    "scope": "host"
                }
            ],
            "mtu": 65536,
            "promisc": false,
            "timestamping": [
                "tx_software",
                "rx_software",
                "software"
            ],
            "type": "loopback"
        },
        "ansible_local": {},
        "ansible_lsb": {
            "codename": "focal",
            "description": "Ubuntu 20.04.1 LTS",
            "id": "Ubuntu",
            "major_release": "20",
            "release": "20.04"
        },
        "ansible_machine": "x86_64",
        "ansible_machine_id": "c6a52afed8564edfa075a362c20348b8",
        "ansible_memfree_mb": 258,
        "ansible_memory_mb": {
            "nocache": {
                "free": 2209,
                "used": 1727
            },
            "real": {
                "free": 258,
                "total": 3936,
                "used": 3678
            },
            "swap": {
                "cached": 2,
                "free": 1979,
                "total": 2047,
                "used": 68
            }
        },
        "ansible_memtotal_mb": 3936,
        "ansible_mounts": [
            {
                "block_available": 2011759,
                "block_size": 4096,
                "block_total": 7900888,
                "block_used": 5889129,
                "device": "/dev/sda5",
                "fstype": "ext4",
                "inode_available": 1582129,
                "inode_total": 2015232,
                "inode_used": 433103,
                "mount": "/",
                "options": "rw,relatime,errors=remount-ro",
                "size_available": 8240164864,
                "size_total": 32362037248,
                "uuid": "fb261367-cf98-4bce-b682-42b3de0a8ab9"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 1942,
                "block_used": 1942,
                "device": "/dev/loop3",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 10774,
                "inode_used": 10774,
                "mount": "/snap/chromium/1421",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 254541824,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 782,
                "block_used": 782,
                "device": "/dev/loop4",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 12826,
                "inode_used": 12826,
                "mount": "/snap/core/10185",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 102498304,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 443,
                "block_used": 443,
                "device": "/dev/loop5",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 10775,
                "inode_used": 10775,
                "mount": "/snap/core18/1885",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 58064896,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 1169,
                "block_used": 1169,
                "device": "/dev/loop1",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 4197,
                "inode_used": 4197,
                "mount": "/snap/code/50",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 153223168,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 783,
                "block_used": 783,
                "device": "/dev/loop6",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 12867,
                "inode_used": 12867,
                "mount": "/snap/core/10444",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 102629376,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 734,
                "block_used": 734,
                "device": "/dev/loop7",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 132,
                "inode_used": 132,
                "mount": "/snap/drawio/80",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 96206848,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 747,
                "block_used": 747,
                "device": "/dev/loop8",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 132,
                "inode_used": 132,
                "mount": "/snap/drawio/84",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 97910784,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 443,
                "block_used": 443,
                "device": "/dev/loop9",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 10779,
                "inode_used": 10779,
                "mount": "/snap/core18/1932",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 58064896,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 1303,
                "block_used": 1303,
                "device": "/dev/loop10",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 27807,
                "inode_used": 27807,
                "mount": "/snap/gnome-3-28-1804/145",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 170786816,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 519,
                "block_used": 519,
                "device": "/dev/loop12",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 63978,
                "inode_used": 63978,
                "mount": "/snap/gtk-common-themes/1514",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 68026368,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 1404,
                "block_used": 1404,
                "device": "/dev/loop11",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 44282,
                "inode_used": 44282,
                "mount": "/snap/postman/129",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 184025088,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 1385,
                "block_used": 1385,
                "device": "/dev/loop13",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 45118,
                "inode_used": 45118,
                "mount": "/snap/postman/128",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 181534720,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 515,
                "block_used": 515,
                "device": "/dev/loop14",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 63811,
                "inode_used": 63811,
                "mount": "/snap/gtk-common-themes/1513",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 67502080,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 1292,
                "block_used": 1292,
                "device": "/dev/loop15",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 27798,
                "inode_used": 27798,
                "mount": "/snap/gnome-3-28-1804/128",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 169345024,
                "uuid": "N/A"
            },
            {
                "block_available": 130811,
                "block_size": 4096,
                "block_total": 130812,
                "block_used": 1,
                "device": "/dev/sda1",
                "fstype": "vfat",
                "inode_available": 0,
                "inode_total": 0,
                "inode_used": 0,
                "mount": "/boot/efi",
                "options": "rw,relatime,fmask=0077,dmask=0077,codepage=437,iocharset=iso8859-1,shortname=mixed,errors=remount-ro",
                "size_available": 535801856,
                "size_total": 535805952,
                "uuid": "AF29-5078"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 947,
                "block_used": 947,
                "device": "/dev/loop16",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 1330,
                "inode_used": 1330,
                "mount": "/snap/chromium/1424",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 124125184,
                "uuid": "N/A"
            },
            {
                "block_available": 0,
                "block_size": 131072,
                "block_total": 1173,
                "block_used": 1173,
                "device": "/dev/loop2",
                "fstype": "squashfs",
                "inode_available": 0,
                "inode_total": 4207,
                "inode_used": 4207,
                "mount": "/snap/code/51",
                "options": "ro,nodev,relatime",
                "size_available": 0,
                "size_total": 153747456,
                "uuid": "N/A"
            }
        ],
        "ansible_nodename": "labvm",
        "ansible_os_family": "Debian",
        "ansible_pkg_mgr": "apt",
        "ansible_proc_cmdline": {
            "BOOT_IMAGE": "/boot/vmlinuz-5.4.0-37-generic",
            "quiet": true,
            "ro": true,
            "root": "UUID=fb261367-cf98-4bce-b682-42b3de0a8ab9",
            "vga": "792",
            "zswap.enabled": "1"
        },
        "ansible_processor": [
            "0",
            "GenuineIntel",
            "Intel(R) Core(TM) i7-7600U CPU @ 2.80GHz",
            "1",
            "GenuineIntel",
            "Intel(R) Core(TM) i7-7600U CPU @ 2.80GHz"
        ],
        "ansible_processor_cores": 2,
        "ansible_processor_count": 1,
        "ansible_processor_threads_per_core": 1,
        "ansible_processor_vcpus": 2,
        "ansible_product_name": "VirtualBox",
        "ansible_product_serial": "NA",
        "ansible_product_uuid": "NA",
        "ansible_product_version": "1.2",
        "ansible_python": {
            "executable": "/usr/bin/python3",
            "has_sslcontext": true,
            "type": "cpython",
            "version": {
                "major": 3,
                "micro": 2,
                "minor": 8,
                "releaselevel": "final",
                "serial": 0
            },
            "version_info": [
                3,
                8,
                2,
                "final",
                0
            ]
        },
        "ansible_python_version": "3.8.2",
        "ansible_real_group_id": 900,
        "ansible_real_user_id": 900,
        "ansible_selinux": {
            "status": "disabled"
        },
        "ansible_selinux_python_present": true,
        "ansible_service_mgr": "systemd",
        "ansible_ssh_host_key_ecdsa_public": "AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPFM1OVBLhbMfZVSkIVrPTq0FcKqNM9vRuBawNKkevM0UoDO5PwzaDCS6Hry9lvKuJIP+aB5KNnQ0P6uZfHdpFc=",
        "ansible_ssh_host_key_ed25519_public": "AAAAC3NzaC1lZDI1NTE5AAAAIC5pTSLWhV+w/qgqcGewKBfdDczo4VhV3VWp1lLHH7U+",
        "ansible_ssh_host_key_rsa_public": "AAAAB3NzaC1yc2EAAAADAQABAAABgQCpwiwXYyl8eNmZO2dfWYyV1V1pnoq/tZjXF9ABBSSsR7KHny7SP4muQvLErLc2wOlvzsYq5l/NQoYuIeY7eGK3dffACUwda9V1Ub6AjcNQIdwLypUt1zW3Q/9e8/VfnmVGr5IeIvt02L362V4jFfLYd8QZxqlzWO7ah8bODyvGP68VP6pE7Hd+XamJAwMHH0NquCeRW5JO6xWaTVvZUiNGVYSTl0OFDuXX/CbXVXMjaaPF1ZJuLtpmfxAcmtIKRqHUmy0wWRah3GXiLwpAR4i50jlgE84Y1swqEpMneAM/nanFwrCEMBmf54olazJ1e3redxIyWFCDwhZO+Q0sZoruS3OXfpsr9/33uksfjP4TiQHy84Xn5WhR/VRRsCyqA7adn/4FmtUtbOR0eaD3pBPGElocCSy7p/wOO18B6Bfa0BSoh8si+ShBNxNVuULw2/iCebRbReXaw9xbfNFx5bJVSfJmZfJvRVpQV9HVZYV2apKuHyFbwLROAf0NRwAJxm8=",
        "ansible_swapfree_mb": 1979,
        "ansible_swaptotal_mb": 2047,
        "ansible_system": "Linux",
        "ansible_system_capabilities": [
            ""
        ],
        "ansible_system_capabilities_enforced": "True",
        "ansible_system_vendor": "innotek GmbH",
        "ansible_uptime_seconds": 88854,
        "ansible_user_dir": "/home/devasc",
        "ansible_user_gecos": "DevNet Associate,,,",
        "ansible_user_gid": 900,
        "ansible_user_id": "devasc",
        "ansible_user_shell": "/bin/bash",
        "ansible_user_uid": 900,
        "ansible_userspace_architecture": "x86_64",
        "ansible_userspace_bits": "64",
        "ansible_vethacd0508": {
            "active": true,
            "device": "vethacd0508",
            "features": {
                "esp_hw_offload": "off [fixed]",
                "esp_tx_csum_hw_offload": "off [fixed]",
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "on",
                "hw_tc_offload": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "off [fixed]",
                "netns_local": "off [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off [fixed]",
                "rx_checksumming": "on",
                "rx_fcs": "off [fixed]",
                "rx_gro_hw": "off [fixed]",
                "rx_udp_tunnel_port_offload": "off [fixed]",
                "rx_vlan_filter": "off [fixed]",
                "rx_vlan_offload": "on",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "on",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tls_hw_record": "off [fixed]",
                "tls_hw_rx_offload": "off [fixed]",
                "tls_hw_tx_offload": "off [fixed]",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "on",
                "tx_checksumming": "on",
                "tx_esp_segmentation": "off [fixed]",
                "tx_fcoe_segmentation": "off [fixed]",
                "tx_gre_csum_segmentation": "on",
                "tx_gre_segmentation": "on",
                "tx_gso_partial": "off [fixed]",
                "tx_gso_robust": "off [fixed]",
                "tx_ipxip4_segmentation": "on",
                "tx_ipxip6_segmentation": "on",
                "tx_lockless": "on [fixed]",
                "tx_nocache_copy": "off",
                "tx_scatter_gather": "on",
                "tx_scatter_gather_fraglist": "on",
                "tx_sctp_segmentation": "on",
                "tx_tcp6_segmentation": "on",
                "tx_tcp_ecn_segmentation": "on",
                "tx_tcp_mangleid_segmentation": "on",
                "tx_tcp_segmentation": "on",
                "tx_udp_segmentation": "off [fixed]",
                "tx_udp_tnl_csum_segmentation": "on",
                "tx_udp_tnl_segmentation": "on",
                "tx_vlan_offload": "on",
                "tx_vlan_stag_hw_insert": "on",
                "vlan_challenged": "off [fixed]"
            },
            "hw_timestamp_filters": [],
            "ipv6": [
                {
                    "address": "fe80::3c67:a5ff:fe17:e4cf",
                    "prefix": "64",
                    "scope": "link"
                }
            ],
            "macaddress": "3e:67:a5:17:e4:cf",
            "mtu": 1500,
            "promisc": true,
            "speed": 10000,
            "timestamping": [
                "tx_software",
                "rx_software",
                "software"
            ],
            "type": "ether"
        },
        "ansible_virtualization_role": "guest",
        "ansible_virtualization_type": "virtualbox",
        "discovered_interpreter_python": "/usr/bin/python3",
        "gather_subset": [
            "all"
        ],
        "module_setup": true
    },
    "changed": false,
    "deprecations": [],
    "warnings": []
}


print("---------1--------")
print("Showing dictionary keys at level 1")
ansible_dict = json.dumps(ansible_dict.json)
print(ansible_dict.keys())

print("---------2--------")
print("Showing keys of ansible facts at level 2")
print(ansible_dict['ansible_facts'].keys())

print("---------3--------")
print("Showing data below ansible facts: ip address")
print("IP Address: " + ansible_dict["ansible_facts"]["ansible_default_ipv4"]["address"])

print('---------4--------')
print("Showing data below ansible facts: ansible distribution")
print("Ansible Distribution: "  + ansible_dict["ansible_facts"]["ansible_distribution"])
print("Ansible Distribution Major: "  +ansible_dict["ansible_facts"]["ansible_distribution_major_version"])
print("Ansible Distribution Release: "  +ansible_dict["ansible_facts"]["ansible_distribution_release"])
print("Ansible Distribution Version: "  +ansible_dict["ansible_facts"]["ansible_distribution_version"])

print('---------5--------')
print("Showing data below ansible facts: kernel, nodename, os")
print("Ansible Kernel: "  +ansible_dict["ansible_facts"]["ansible_kernel"])
print("Ansible Nodename: "     + ansible_dict["ansible_facts"]["ansible_nodename"])
print("Ansible OS Family: "    + ansible_dict["ansible_facts"]["ansible_os_family"])
print("Ansible PKG Manager: "  + ansible_dict["ansible_facts"]["ansible_pkg_mgr"])
print("Ansible Python Version: "  + ansible_dict["ansible_facts"]["ansible_python_version"])

print('---------6--------')
print("Showing data below ansible facts: ansible environment")
print("Ansible Home: "  + ansible_dict["ansible_facts"]["ansible_env"]["HOME"])
print("Ansible User: "  + ansible_dict["ansible_facts"]["ansible_env"]["USER"])