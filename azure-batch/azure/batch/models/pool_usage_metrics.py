# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PoolUsageMetrics(Model):
    """Usage metrics for a pool across an aggregation interval.

    :param pool_id: The id of the pool whose metrics are being aggregated.
    :type pool_id: str
    :param start_time: The start time of the aggregation interval.
    :type start_time: datetime
    :param end_time: The end time of the aggregation interval.
    :type end_time: datetime
    :param vm_size: The size of virtual machines in the pool. All VMs in a
     pool are the same size.
    :type vm_size: str
    :param total_core_hours: The total core hours used in the pool during
     this aggregation interval.
    :type total_core_hours: float
    :param data_ingress_gi_b: The cross data center network ingress in GiB to
     the pool during this interval.
    :type data_ingress_gi_b: float
    :param data_egress_gi_b: The cross data center network egress in GiB from
     the pool during this interval.
    :type data_egress_gi_b: float
    """ 

    _validation = {
        'pool_id': {'required': True},
        'start_time': {'required': True},
        'end_time': {'required': True},
        'vm_size': {'required': True},
        'total_core_hours': {'required': True},
        'data_ingress_gi_b': {'required': True},
        'data_egress_gi_b': {'required': True},
    }

    _attribute_map = {
        'pool_id': {'key': 'poolId', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'vm_size': {'key': 'vmSize', 'type': 'str'},
        'total_core_hours': {'key': 'totalCoreHours', 'type': 'float'},
        'data_ingress_gi_b': {'key': 'dataIngressGiB', 'type': 'float'},
        'data_egress_gi_b': {'key': 'dataEgressGiB', 'type': 'float'},
    }

    def __init__(self, pool_id, start_time, end_time, vm_size, total_core_hours, data_ingress_gi_b, data_egress_gi_b):
        self.pool_id = pool_id
        self.start_time = start_time
        self.end_time = end_time
        self.vm_size = vm_size
        self.total_core_hours = total_core_hours
        self.data_ingress_gi_b = data_ingress_gi_b
        self.data_egress_gi_b = data_egress_gi_b