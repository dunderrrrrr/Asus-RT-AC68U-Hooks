Asus RT-AC68U Hooks
======

Fetch data with different hooks from your Asus router through this Python script.  

This will probably work with other firmare/versions of the Asus RT-series. Following hooks has been found on *Asus RT-AC68U* running *Merlin 384.17_0*.  

Replace settings in `run.py` and install python requirements `pip install -r requirements.txt`. Execute with `$python run.py`.  

Make sure `user-agent` is set in your payload to `asusrouter-Android-DUTUtil-1.0.0.201`. If not, the router wont return your token needed to get all data.  

I have not been able to find any of these hooks in any of the router-files. Hooks are discovered through the Asus Router App (https://www.asus.com/asus-router-app/) while Wiresharking.  

## Hooks

#### System
`cpu_usage(appobj)`  
`memory_usage(appobj)`  

#### WAN
`wanlink()`  
`wanlink_status()`  
`wanlink_statusstr()`  
`wanlink_type()`  
`wanlink_ipaddr()`  
`wanlink_netmask()`  
`wanlink_gateway()`  
`wanlink_dns()`  
`wanlink_lease()`  
`wanlink_expires()`  
`wanlink_xtype()`  
`wanlink_xipaddr()`  
`wanlink_xnetmask()`  
`wanlink_xgateway()`  
`wanlink_xdns()`  
`wanlink_xlease()`  
`wanlink_xexpires()` 
`is_private_subnet()`  

#### Clients
`get_clientlist()`  
`get_clientlist_from_json_database()`  
`get_allclientlist()`  
`get_wclientlist()`  
`get_wiredclientlist()`  
`get_cfg_clientlist()`  

#### DHCP
`dhcpLeaseMacList()`  

#### nvram
`nvram_get(time_zone)`  
`nvram_get(time_zone_dst)`  
`nvram_get(time_zone_x)`  
`nvram_get(time_zone_dstoff)`  
`nvram_get(time_zone)`  
`nvram_get(ntp_server0)`  
`nvram_get(acs_dfs)`  
`nvram_get(productid)`  
`nvram_get(apps_sq)`  
`nvram_get(lan_hwaddr)`  
`nvram_get(lan_ipaddr)`  
`nvram_get(lan_proto)`  
`nvram_get(x_Setting)`  
`nvram_get(label_mac)`  
`nvram_get(lan_netmask)`  
`nvram_get(lan_gateway)` 
`nvram_get(http_enable)`  
`nvram_get(https_lanport)`  
`nvram_get(wl0_country_code)`  
`nvram_get(wl1_country_code)`  

#### Other
`netdev(appobj)`  

Pull requests are welcome :) 