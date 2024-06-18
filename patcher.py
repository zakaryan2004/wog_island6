# Copyright (C) 2024 Gegham Zakaryan

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import bsdiff4
import sys
import os

def apply_patch(original_file, patched_file, patch_file):
    try:
        with open(original_file, 'rb') as orig:
            original_data = orig.read()
        
        with open(patch_file, 'rb') as patch:
            patch_data = patch.read()
        
        patched_data = bsdiff4.patch(original_data, patch_data)
        
        with open(patched_file, 'wb') as patched:
            patched.write(patched_data)
        
        print(f"Patch applied successfully! Written to {patched_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python patcher.py <win32/macos/linux> <original_file>")
        print("Example: python patcher.py win32 WorldOfGoo.exe")
        print("WARNING: Make sure to backup your original file before applying the patch!")
        print("This script will overwrite the original file.")
        sys.exit(1)

    if sys.argv[1] not in ["win32", "macos"]:
        print("Error: Invalid platform. Choose from win32, macos, (linux not yet supported).")
        sys.exit(1)

    original_file = sys.argv[2]
    patched_file = sys.argv[2]
    patch_file = f"{sys.argv[1]}/patch.patch"

    if not os.path.exists(original_file):
        print(f"Error: {original_file} does not exist.")
        sys.exit(1)
    
    if not os.path.exists(patch_file):
        print(f"Error: {patch_file} does not exist.")
        sys.exit(1)

    apply_patch(original_file, patched_file, patch_file)
