"""Glues PKG-INFO into meson dist"""

# Copyright 2023 Ross J. Duff MSc
# The copyright holder licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
import os
import glob
import pathlib
import shutil
import sys


def main():
    """create a PKG-INFO file in the meson dist staging directory"""
    root = pathlib.Path(os.environ.get("MESON_SOURCE_ROOT", '.'))
    staged = root/'dist'
    dist_info = glob.glob('*.dist-info', root_dir=staged)[0]
    print(pathlib.Path(os.environ.get("MESON_DIST_ROOT", '.'))/os.path.splitext(dist_info)[0]/'PKG-INFO', file=sys.stderr)
    shutil.copyfile(
        pathlib.Path('dist')/dist_info/'METADATA',
        pathlib.Path(os.environ.get("MESON_DIST_ROOT", '.'))/os.path.splitext(dist_info)[0]/'PKG-INFO'  # type: ignore
    )



if __name__ == '__main__':
    try:
        main()
    except TypeError:
        print('ERROR: Missing environment variable MESON_DIST_ROOT.', file=sys.stderr)
        sys.exit(1)
    finally:
        sys.exit(0)
