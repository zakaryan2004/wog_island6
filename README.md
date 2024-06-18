### World of Goo Island 6 Patch Mod for World of Goo 1.5+

This mod adds support for a new island to the World of Goo game. It is a binary patch, meaning it doesn't add any new levels and islands, but it allows you to add your own levels and island to the game. This patch works only in World of Goo 1.5 and above.

### Installation

1. Python is required to run the patcher. You can download it from [here](https://www.python.org/downloads/).

2. Clone this repository or download the zip file and extract it.

3. Install the required packages by running `pip install -r requirements.txt` in the extracted directory.

4. Run the patcher by running `python patcher.py <win32/macos> <WorldOfGoo binary>` in the extracted directory. You can find the WorldOfGoo binary and drag it to the terminal to get the path. The location of the binary depends on the platform and distribution. For example, on Windows with Epic Games Store, the binary is located (by default) in `C:\Program Files\Epic Games\WorldOfGoo\WorldOfGoo.exe`. On macOS with Epic Games Store, the binary is located (by default) in `/Users/Shared/Epic Games/WorldOfGoo/World of Goo.app/Contents/MacOS/World of Goo`.

5. Warning: The patcher will modify the game binary. Make sure to back up the original binary before running the patcher if you want to revert the changes without reinstalling the game.

6. After running the patcher, you can add your own levels and island to the game. See the instructions below.

### Patches necessary in the game/ directory (in the same directory as the binary)

### 1. game/properties/text.xml

```diff
+ <string id="CHAPTER6_NAME"
+     text="Chapter 6 Name"
+     es="Chapter 6 Name"
+     fr="Chapter 6 Name"
+     de="Chapter 6 Name"
+     it="Chapter 6 Name"
+     nl="Chapter 6 Name"
+     pl="Chapter 6 Name"
+     hu="Chapter 6 Name"
+     ko="Chapter 6 Name"
+     cn="Chapter 6 Name"
+     jp="Chapter 6 Name"
+ />
+ 
+ <string id="CHAPTER6_DESCRIPTION"
+     text="&quot;Chapter 6 Description&quot;"
+     es="&quot;Chapter 6 Description&quot;"
+     fr="&quot;Chapter 6 Description&quot;"
+     de="&quot;Chapter 6 Description&quot;"
+     it="&quot;Chapter 6 Description&quot;"
+     nl="&quot;Chapter 6 Description&quot;"
+     pl="&quot;Chapter 6 Description&quot;"
+     hu="&quot;Chapter 6 Description&quot;"
+     ko="&quot;Chapter 6 Description&quot;"
+     cn="&quot;Chapter 6 Description&quot;"
+     jp="&quot;Chapter 6 Description&quot;"
+ />
+ 
+ <string id="CHAPTER_6_SEASON"
+     text="Chapter 6 Season"
+     es="Chapter 6 Season"
+     fr="Chapter 6 Season"
+     de="Chapter 6 Season"
+     it="Chapter 6 Season"
+     nl="Chapter 6 Season"
+     pl="Chapter 6 Season"
+     hu="Chapter 6 Season"
+     ko="Chapter 6 Season"
+     cn="Chapter 6 Season"
+     jp="Chapter 6 Season"
+ />
```

Don't forget to add Chapter 6 level names and descriptions here as well.

### 2. game/properties/resources.xml

You can use any image you want for the island icon. Make sure to add the image to the game/res/images directory.

```diff
+ <Image id="IMAGE_GLOBAL_ISLAND_6_ICON" path="res/images/islandicon_blimp"/>
```

Creating island6 and its levels. For ease of testing, you can duplicate island5.

### 3. Create game/res/islands/island6.xml

Make sure the map and icon attributes are set correctly, and the level dependence is set up properly. For ease of testing, copy island5.xml, rename all levels to `<LevelName>2`, change everything pointing to island 5 to island 6.

### 4. Create game/res/levels/island6 directory with proper island contents

For ease of testing, copy island5 directory and make the necessary changes. You can do whatever you want as long as it's valid. The game will crash if there aren't island6.level/.resrc/.scene files. 

### 5. Create levels for island 6 in game/res/levels/ 

For ease of testing, copy island5 levels and make the necessary changes (`<LevelName>2`). Don't forget to make sure the new directory is used for resources, and be sure to make all necessary changes to have a valid level.

### (Optional) 6. Modify MapWorldView

... to change where the island6 button is and how it looks like. Be mindful of the arrow since it's not yet possible to change its angle.

### Troubleshooting

* If the game crashes during the loading scene, most probably there is something wrong with your island6.xml or text.xml.

* If the game crashes when you hover on island6, there is something wrong with your text.xml.

* If the game crashes when you click on island6 and the season text is seen before the crash, then most probably your levels/island6 directory is not set up properly.

* If the game crashes when you hover on levels, your text.xml is not set up properly or the level name strings aren't valid in island6.xml.

* If the game crashes immediately after clicking on a level, check your island 6 icon in resources.xml, text.xml.

* If the game crashes after clicking on a level but the icon and text are visible, check if the level files are set up properly.


For any other issues, contact me (@zakaryan2004) on the [GooFans Discord server](https://discord.gg/6BEecnD) or open an issue here.
```




