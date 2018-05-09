#
# Copyright (C) 2018 ETH Zurich and University of Bologna
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# Authors: Germain Haugou, ETH (germain.haugou@iis.ee.ethz.ch)

from bridge.default_debug_bridge import *
import bridge.chips.gap as gap
import bridge.chips.wolfe as wolfe
import bridge.chips.fulmine as fulmine


def get_bridge(config, binaries=[], verbose=False):


    chip = list(config.get('**/pulp_chip').get_items().values())[0].get('name').get()


    if chip == 'gap':
        bridge_class = gap.gap_debug_bridge
    elif chip == 'fulmine':
        bridge_class = fulmine.fulmine_debug_bridge
    elif chip == 'wolfe':
        bridge_class = wolfe.wolfe_debug_bridge
    else:
        bridge_class = debug_bridge

    return bridge_class(config=config, binaries=binaries, verbose=verbose)
