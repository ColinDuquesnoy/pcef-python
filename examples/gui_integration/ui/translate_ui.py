#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# PCEF - Python/Qt Code Editing Framework
# Copyright 2013, Colin Duquesnoy <colin.duquesnoy@gmail.com>
#
# This software is released under the LGPLv3 license.
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
This script calls the PyQt ui compiler on all ui files found in the cwd.
(It also compiles the qrc files to *_rc.py)
"""
import glob
import os

# compile ui files
for name in glob.glob("*.ui"):
    base = name.split(".")[0]
    # python 3
    cmd = "pyuic4 -w {0} > {1}_ui3.py ".format(name, base)
    print(cmd)
    os.system(cmd)
    # python 2
    cmd = "pyuic4 {0} > {1}_ui.py ".format(name, base)
    print(cmd)
    os.system(cmd)

for name in glob.glob("*.qrc"):
    base = name.split(".")[0]
    # python 3
    cmd = "pyrcc4 -py3 {0} > {1}_rc3.py".format(name, base)
    print(cmd)
    os.system(cmd)
    # python 2
    cmd = "pyrcc4 {0} > {1}_rc.py".format(name, base)
    print(cmd)
    os.system(cmd)


