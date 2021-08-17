# Copyright 2021 Dr. Carlos Lopez-Franco.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np

def grid(plt, im):
    ax = plt.gca()

    m= im.shape[0]
    n= im.shape[1]

    ax.set_xticks(np.arange(0, n, 1))
    ax.set_yticks(np.arange(0, m, 1))

    ax.set_xticklabels(np.arange(0, n, 1))
    ax.set_yticklabels(np.arange(0, m, 1))

    ax.set_xticks(np.arange(-.5, n, 1), minor=True)
    ax.set_yticks(np.arange(-.5, m, 1), minor=True)

    ax.grid(which='minor', color='w', linestyle='-', linewidth=2)