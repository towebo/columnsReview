# Columns Review #

* Author: Alberto Buffolino.
* Download [development version][3]

Columns Review is an add-on to read and copy items in a list column by column. It supports lists with a potentially infinite number of columns, and you can navigate them using keyboard or numpad digits. The column headers can be read but not copied, or vice versa.

Additionally, it provides list search, a way to interact with column headers, and can announce "0 elements" when a list is empty.

See below for more details about supported list.

## Key Commands ##

Default keys associated with numbers are NVDA and control, but you can customize them from add-on settings. See settings also for numpad/keyboard mode and layout.

* NVDA+control+digits from 1 to 0 (keyboard mode) or from 1 to 9 (numpad mode): By default when pressed once, read the chosen column, pressed twice, copy it;
If you want to customize what happens when this command is pressed please take a look at the section about customizing in settins dialog.
* NVDA+control+numpadMinus (numpad mode): read or copy the 10th, 20th, etc column;
* NVDA+control+- (default, EN-US layout, keyboard mode): in a list with 10+ columns, let you to change interval and read columns from 11 to 20, from 21 to 30, and so on; see settings to change last char according to your layout;
* NVDA+control+numpadPlus (numpad mode): exactly as previous command;
* NVDA+control+f: open find dialog;
* NVDA+f3: find next occurrence of previously entered text;
* NVDA+shift+f3: find previous occurrence;
* NVDA+control+enter (numpadEnter in numpad mode): open column headers manager;
* Arrows (in empty list): repeat "0 elements" message.


## Cusotmize action performed on columns ##
By default when pressing gesture to interact with a given column first press read its content and second copies it to the Windows clipboard.
You can, however, customize this in the settings dialog to your liking.
The following operations are possible:

* Content of the column can be read its header is announced if the corresponding checkbox is checked.
* Column content can be copied  along with its header if the corresponding checkbox is checked
* Column content can be spelled out.
* Column content can be shown in the browseable message header of the column is presented as the message title.

## For developers and advanced users ##

List types supported by search and numeric gestures are:

* SysListView32;
* DirectUIHWND (present in 64-bit systems);
* WindowsForms10.SysListView32.* (applications that use .NET);
* Mozilla table (tipically, Thunderbird message list, thread-grouping supported).

All specific gestures are associated on and only on supported lists, when these are not empty.

Any listview potentially supports empty announcement (so, not DirectUIHWND nor Mozilla table).


[1]: https://addons.nvda-project.org/files/get.php?file=cr
[2]: https://addons.nvda-project.org/files/get.php?file=cr-dev
[3]: https://raw.githubusercontent.com/ABuffEr/columnsReview/master/packages/columnsReview-3.0-20210513-dev.nvda-addon
