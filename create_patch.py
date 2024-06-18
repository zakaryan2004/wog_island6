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

def create_patch(original_file, modified_file, patch_file):
    try:
        with open(original_file, 'rb') as orig:
            original_data = orig.read()
        
        with open(modified_file, 'rb') as mod:
            modified_data = mod.read()
        
        patch_data = bsdiff4.diff(original_data, modified_data)
        
        with open(patch_file, 'wb') as patch:
            patch.write(patch_data)
        
        print(f"Patch created successfully! Saved as {patch_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_patch.py <win32/macos/linux>")
        sys.exit(1)

    if sys.argv[1] not in ["win32", "macos"]:
        print("Error: Invalid platform. Choose from win32, macos, (linux not yet supported).")
        sys.exit(1)

    original_file = f"{sys.argv[1]}/original.bin"
    modified_file = f"{sys.argv[1]}/modified.bin"
    patch_file = f"{sys.argv[1]}/patch.patch"

    if not os.path.exists(original_file):
        print(f"Error: {original_file} does not exist.")
        sys.exit(1)
    
    if not os.path.exists(modified_file):
        print(f"Error: {modified_file} does not exist.")
        sys.exit(1)

    create_patch(original_file, modified_file, patch_file)
