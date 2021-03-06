# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy
# of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from networking_cisco.plugins.ml2.drivers.cisco.nexus import (
    config as nexus_config)
from networking_cisco.plugins.ml2.drivers.cisco.nexus import (
    type_nexus_vxlan as nexus_vxlan_config)


def list_nexus_conf_opts():

    return [
        ('ml2_cisco', nexus_config.ml2_cisco_opts),
        ('ml2_mech_cisco_nexus:<ip_address>', nexus_config.nexus_sub_opts)
    ]


def list_nexus_vxlan_type_driver_conf_opts():
    return [
        ('ml2_type_nexus_vxlan', nexus_vxlan_config.nexus_vxlan_opts),
    ]
