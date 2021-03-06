# -*- coding: iso-8859-15 -*-

# Promogest
#
# Copyright (C) 2007 by Promotux Informatica - http://www.promotux.it/
# Author: Francesco Meloni  <francesco@promotux.it>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

colorDict = {
        "AliceBlue": ["#0f070000","#f0f8ff"],
        "AntiqueWhite": ["#000f2305","#faebd7"],
        "AntiqueWhite1": ["#00102400","#ffefdb"],
        "AntiqueWhite2": ["#000f2211","#eedfcc"],
        "AntiqueWhite3": ["#000d1d32","#cdc0b0"],
        "AntiqueWhite4": ["#00081374","#8b8378"],
        "Aquamarine": ["#80002b00","#7fffd4"],
        "Aquamarine1": ["#80002b00","#7fffd4"],
        "Aquamarine2": ["#78002811","#76eec6"],
        "Aquamarine3": ["#67002332","#66cdaa"],
        "Aquamarine4": ["#46001774","#458b74"],
        "Azure": ["#0f000000","#f0ffff"],
        "Azure1": ["#0f000000", "#f0ffff"],
        "Azure2": ["#0e000011", "#e0eeee"],
        "Azure3": ["#0c000032", "#c1cdcd"],
        "Azure4": ["#08000074", "#838b8b"],
        "Beige": ["#0000190a", "#f5f5dc"],
        "Bisque": ["#001b3b00", "#ffe4c4"],
        "Bisque1": ["#001b3b00", "#ffe4c4"],
        "Bisque2": ["#00193711", "#eed5b7"],
        "Bisque3": ["#00162f32", "#cdb79e"],
        "Bisque4": ["#000e2074", "#8b7d6b"],
        "Black" : ["#000000ff", "#000000"],
        "BlanchedAlmond" : ["#00143200", "#ffebcd"],
        "Blue" : ["#ffff0000", "#0000ff"],
        "Blue1" : ["#ffff0000", "#0000ff"],
        "Blue2" : ["#eeee0011", "#0000ee"],
        "Blue3" : ["#cdcd0032", "#0000cd"],
        "Blue4" : ["#8b8b0074", "#00008b"],
        "BlueViolet" : ["#58b7001d", "#8a2be2"],
        "Brown" : ["#007b7b5a", "#a52a2a"],
        "Brown1" : ["#00bfbf00", "#ff4040"],
        "Brown2" : ["#00b3b311", "#ee3b3b"],
        "Brown3" : ["#009a9a32", "#cd3333"],
        "Brown4" : ["#00686874", "#8b2323"],
        "Burlywood" : ["#00265721", "#deb887"],
        "Burlywood1" : ["#002c6400", "#ffd39b"],
        "Burlywood2" : ["#00295d11", "#eec591"],
        "Burlywood3" : ["#00235032", "#cdaa7d"],
        "Burlywood4" : ["#00183674", "#8b7355"],
        "CadetBlue" : ["#4102005f", "#5f9ea0"],
        "CadetBlue1" : ["#670a0000", "#98f5ff"],
        "CadetBlue2" : ["#60090011", "#8ee5ee"],
        "CadetBlue3" : ["#53080032", "#7ac5cd"],
        "CadetBlue4" : ["#38050074", "#53868b"],
        "Chartreuse" : ["#8000ff00", "#7fff00"],
        "Chartreuse1" : ["#8000ff00", "#7fff00"],
        "Chartreuse2" : ["#7800ee11", "#76ee00"],
        "Chartreuse3" : ["#6700cd32", "#66cd00"],
        "Chartreuse4" : ["#46008b74", "#458b00"],
        "Chocolate" : ["#0069b42d", "#d2691e"],
        "Chocolate1" : ["#0080db00", "#ff7f24"],
        "Chocolate2" : ["#0078cd11", "#ee7621"],
        "Chocolate3" : ["#0067b032", "#cd661d"],
        "Chocolate4" : ["#00467874", "#8b4513"],
        "Coral" : ["#0080af00", "#ff7f50"],
        "Coral1" : ["#008da900", "#ff7256"],
        "Coral2" : ["#00849e11", "#ee6a50"],
        "Coral3" : ["#00728832", "#cd5b45"],
        "Coral4" : ["#004d5c74", "#8b3e2f"],
        "CornflowerBlue" : ["#89580012", "#6495ed"],
        "Cornsilk" : ["#00072300", "#fff8dc"],
        "Cornsilk1" : ["#00072300", "#fff8dc"],
        "Cornsilk2" : ["#00062111", "#eee8cd"],
        "Cornsilk3" : ["#00051c32", "#cdc8b1"],
        "Cornsilk4" : ["#00031374", "#8b8878"],
        "Cyan" : ["#ff000000", "#00ffff"],
        "Cyan1" : ["#ff000000", "#00ffff"],
        "Cyan2" : ["#ee000011", "#00eeee"],
        "Cyan3" : ["#cd000032", "#00cdcd"],
        "Cyan4" : ["#8b000074", "#008b8b"],
        "DarkBlue" : ["#8b8b0074", "#00008b"],
        "DarkCyan" : ["#8b000074", "#008b8b"],
        "DarkGoldenrod" : ["#0032ad47", "#b8860b"],
        "DarkGoldenrod1" : ["#0046f000", "#ffb90f"],
        "DarkGoldenrod2" : ["#0041e011", "#eead0e"],
        "DarkGoldenrod3" : ["#0038c132", "#cd950c"],
        "DarkGoldenrod4" : ["#00268374", "#8b6508"],
        "DarkGreen" : ["#6400649b", "#006400"],
        "DarkGrey" : ["#00000056", "#a9a9a9"],
        "DarkKhaki" : ["#00065242", "#bdb76b"],
        "DarkMagenta" : ["#008b0074", "#8b008b"],
        "DarkOliveGreen" : ["#16003c94", "#556b2f"],
        "DarkOliveGreen1" : ["#35008f00", "#caff70"],
        "DarkOliveGreen2" : ["#32008611", "#bcee68"],
        "DarkOliveGreen3" : ["#2b007332", "#a2cd5a"],
        "DarkOliveGreen4" : ["#1d004e74", "#6e8b3d"],
        "DarkOrange" : ["#0073ff00", "#ff8c00"],
        "DarkOrange1" : ["#0080ff00", "#ff7f00"],
        "DarkOrange2" : ["#0078ee11", "#ee7600"],
        "DarkOrange3" : ["#0067cd32", "#cd6600"],
        "DarkOrange4" : ["#00468b74", "#8b4500"],
        "DarkOrchid" : ["#339a0033", "#9932cc"],
        "DarkOrchid1" : ["#40c10000", "#bf3eff"],
        "DarkOrchid2" : ["#3cb40011", "#b23aee"],
        "DarkOrchid3" : ["#339b0032", "#9a32cd"],
        "DarkOrchid4" : ["#23690074", "#68228b"],
        "DarkRed" : ["#008b8b74", "#8b0000"],
        "DarkSalmon" : ["#00536f16", "#e9967a"],
        "DarkSeaGreen" : ["#2d002d43", "#8fbc8f"],
        "DarkSeaGreen1" : ["#3e003e00", "#c1ffc1"],
        "DarkSeaGreen2" : ["#3a003a11", "#b4eeb4"],
        "DarkSeaGreen3" : ["#32003232", "#9bcd9b"],
        "DarkSeaGreen4" : ["#22002274", "#698b69"],
        "DarkSlateBlue" : ["#434e0074", "#483d8b"],
        "DarkSlateGrey" : ["#200000b0", "#2f4f4f"],
        "DarkSlateGrey1" : ["#68000000", "#97ffff"],
        "DarkSlateGrey2" : ["#61000011", "#8deeee"],
        "DarkSlateGrey3" : ["#54000032", "#79cdcd"],
        "DarkSlateGrey4" : ["#39000074", "#528b8b"],
        "DarkTurquoise" : ["#d103002e", "#00ced1"],
        "DarkViolet" : ["#3fd3002c", "#9400d3"],
        "DeepPink" : ["#00eb6c00", "#ff1493"],
        "DeepPink1" : ["#00eb6c00", "#ff1493"],
        "DeepPink2" : ["#00dc6511", "#ee1289"],
        "DeepPink3" : ["#00bd5732", "#cd1076"],
        "DeepPink4" : ["#00813b74", "#8b0a50"],
        "DeepSkyBlue" : ["#ff400000", "#00bfff"],
        "DeepSkyBlue1" : ["#ff400000", "#00bfff"],
        "DeepSkyBlue2" : ["#ee3c0011", "#00b2ee"],
        "DeepSkyBlue3" : ["#cd330032", "#009acd"],
        "DeepSkyBlue4" : ["#8b230074", "#00688b"],
        "DimGrey" : ["#00000096", "#696969"],
        "DodgerBlue" : ["#e16f0000", "#1e90ff"],
        "DodgerBlue1" : ["#e16f0000", "#1e90ff"],
        "DodgerBlue2" : ["#d2680011", "#1c86ee"],
        "DodgerBlue3" : ["#b5590032", "#1874cd"],
        "DodgerBlue4" : ["#7b3d0074", "#104e8b"],
        "Firebrick" : ["#0090904d", "#b22222"],
        "Firebrick1" : ["#00cfcf00", "#ff3030"],
        "Firebrick2" : ["#00c2c211", "#ee2c2c"],
        "Firebrick3" : ["#00a7a732", "#cd2626"],
        "Firebrick4" : ["#00717174", "#8b1a1a"],
        "FloralWhite" : ["#00050f00", "#fffaf0"],
        "ForestGreen" : ["#69006974", "#228b22"],
        "Gainsboro" : ["#00000023", "#dcdcdc"],
        "GhostWhite" : ["#07070000", "#f8f8ff"],
        "Gold" : ["#0028ff00", "#ffd700"],
        "Gold1" : ["#0028ff00", "#ffd700"],
        "Gold2" : ["#0025ee11", "#eec900"],
        "Gold3" : ["#0020cd32", "#cdad00"],
        "Gold4" : ["#00168b74", "#8b7500"],
        "Goldenrod" : ["#0035ba25", "#daa520"],
        "Goldenrod1" : ["#003eda00", "#ffc125"],
        "Goldenrod2" : ["#003acc11", "#eeb422"],
        "Goldenrod3" : ["#0032b032", "#cd9b1d"],
        "Goldenrod4" : ["#00227774", "#8b6914"],
        "Green" : ["#ff00ff00", "#00ff00"],
        "Green1" : ["#ff00ff00", "#00ff00"],
        "Green2" : ["#ee00ee11","#00ee00"],
        "Green3" : ["#cd00cd32","#00cd00"],
        "Green4" : ["#8b008b74","#008b00"],
        "GreenYellow" : ["#5200d000","#adff2f"],
        "Grey" : ["#00000041","#bebebe"],
        "Grey0" : ["#000000ff","#000000"],
        "Grey1" : ["#000000fc","#030303"],
        "Grey10" : ["#000000e5","#1a1a1a"],
        "Grey100" : ["#00000000","#ffffff"],
        "Grey11" : ["#000000e3","#1c1c1c"],
        "Grey12" : ["#000000e0","#1f1f1f"],
        "Grey13" : ["#000000de","#212121"],
        "Grey14" : ["#000000db","#242424"],
        "Grey15" : ["#000000d9","#262626"],
        "Grey16" : ["#000000d6","#292929"],
        "Grey17" : ["#000000d4","#2b2b2b"],
        "Grey18" : ["#000000d1","#2e2e2e"],
        "Grey19" : ["#000000cf","#303030"],
        "Grey2" : ["#000000fa","#050505"],
        "Grey20" : ["#000000cc","#333333"],
        "Grey21" : ["#000000c9","#363636"],
        "Grey22" : ["#000000c7","#383838"],
        "Grey23" : ["#000000c4","#3b3b3b"],
        "Grey24" : ["#000000c2","#3d3d3d"],
        "Grey25" : ["#000000bf","#404040"],
        "Grey26" : ["#000000bd","#424242"],
        "Grey27" : ["#000000ba","#454545"],
        "Grey28" : ["#000000b8","#474747"],
        "Grey29" : ["#000000b5","#4a4a4a"],
        "Grey3" : ["#000000f7","#080808"],
        "Grey30" : ["#000000b2","#4d4d4d"],
        "Grey31" : ["#000000b0","#4f4f4f"],
        "Grey32" : ["#000000ad","#525252"],
        "Grey33" : ["#000000ab","#545454"],
        "Grey34" : ["#000000a8","#575757"],
        "Grey35" : ["#000000a6","#595959"],
        "Grey36" : ["#000000a3","#5c5c5c"],
        "Grey37" : ["#000000a1","#5e5e5e"],
        "Grey38" : ["#0000009e","#616161"],
        "Grey39" : ["#0000009c","#636363"],
        "Grey4" : ["#000000f5","#0a0a0a"],
        "Grey40" : ["#00000099","#666666"],
        "Grey41" : ["#00000096","#696969"],
        "Grey42" : ["#00000094","#6b6b6b"],
        "Grey43" : ["#00000091","#6e6e6e"],
        "Grey44" : ["#0000008f","#707070"],
        "Grey45" : ["#0000008c","#737373"],
        "Grey46" : ["#0000008a","#757575"],
        "Grey47" : ["#00000087","#787878"],
        "Grey48" : ["#00000085","#7a7a7a"],
        "Grey49" : ["#00000082","#7d7d7d"],
        "Grey5" : ["#000000f2","#0d0d0d"],
        "Grey50" : ["#00000080","#7f7f7f"],
        "Grey51" : ["#0000007d","#828282"],
        "Grey52" : ["#0000007a","#858585"],
        "Grey53" : ["#00000078","#878787"],
        "Grey54" : ["#00000075","#8a8a8a"],
        "Grey55" : ["#00000073","#8c8c8c"],
        "Grey56" : ["#00000070","#8f8f8f"],
        "Grey57" : ["#0000006e","#919191"],
        "Grey58" : ["#0000006b","#949494"],
        "Grey59" : ["#00000069","#969696"],
        "Grey6" : ["#000000f0","#0f0f0f"],
        "Grey60" : ["#00000066","#999999"],
        "Grey61" : ["#00000063","#9c9c9c"],
        "Grey62" : ["#00000061","#9e9e9e"],
        "Grey63" : ["#0000005e","#a1a1a1"],
        "Grey64" : ["#0000005c","#a3a3a3"],
        "Grey65" : ["#00000059","#a6a6a6"],
        "Grey66" : ["#00000057","#a8a8a8"],
        "Grey67" : ["#00000054","#ababab"],
        "Grey68" : ["#00000052","#adadad"],
        "Grey69" : ["#0000004f","#b0b0b0"],
        "Grey7" : ["#000000ed","#121212"],
        "Grey70" : ["#0000004c","#b3b3b3"],
        "Grey71" : ["#0000004a","#b5b5b5"],
        "Grey72" : ["#00000047","#b8b8b8"],
        "Grey73" : ["#00000045","#bababa"],
        "Grey74" : ["#00000042","#bdbdbd"],
        "Grey75" : ["#00000040","#bfbfbf"],
        "Grey76" : ["#0000003d","#c2c2c2"],
        "Grey77" : ["#0000003b","#c4c4c4"],
        "Grey78" : ["#00000038","#c7c7c7"],
        "Grey79" : ["#00000036","#c9c9c9"],
        "Grey8" : ["#000000eb","#141414"],
        "Grey80" : ["#00000033","#cccccc"],
        "Grey81" : ["#00000030","#cfcfcf"],
        "Grey82" : ["#0000002e","#d1d1d1"],
        "Grey83" : ["#0000002b","#d4d4d4"],
        "Grey84" : ["#00000029","#d6d6d6"],
        "Grey85" : ["#00000026","#d9d9d9"],
        "Grey86" : ["#00000024","#dbdbdb"],
        "Grey87" : ["#00000021","#dedede"],
        "Grey88" : ["#0000001f","#e0e0e0"],
        "Grey89" : ["#0000001c","#e3e3e3"],
        "Grey9" : ["#000000e8", "#171717"],
        "Grey90" : ["#0000001a", "#e5e5e5"],
        "Grey91" : ["#00000017", "#e8e8e8"],
        "Grey92" : ["#00000014", "#ebebeb"],
        "Grey93" : ["#00000012", "#ededed"],
        "Grey94" : ["#0000000f", "#f0f0f0"],
        "Grey95" : ["#0000000d", "#f2f2f2"],
        "Grey96" : ["#0000000a", "#f5f5f5"],
        "Grey97" : ["#00000008", "#f7f7f7"],
        "Grey98" : ["#00000005", "#fafafa"],
        "Grey99" : ["#00000003", "#fcfcfc"],
        "Honeydew" : ["#0f000f00", "#f0fff0"],
        "Honeydew1" : ["#0f000f00", "#f0fff0"],
        "Honeydew2" : ["#0e000e11", "#e0eee0"],
        "Honeydew3" : ["#0c000c32", "#c1cdc1"],
        "Honeydew4" : ["#08000874", "#838b83"],
        "HotPink" : ["#00964b00", "#ff69b4"],
        "HotPink1" : ["#00914b00", "#ff6eb4"],
        "HotPink2" : ["#00844711", "#ee6aa7"],
        "HotPink3" : ["#006d3d32","#cd6090"],
        "HotPink4" : ["#00512974","#8b3a62"],
        "IndianRed" : ["#00717132","#cd5c5c"],
        "IndianRed1" : ["#00959500","#ff6a6a"],
        "IndianRed2" : ["#008b8b11","#ee6363"],
        "IndianRed3" : ["#00787832","#cd5555"],
        "IndianRed4" : ["#00515174","#8b3a3a"],
        "Ivory" : ["#00000f00","#fffff0"],
        "Ivory1" : ["#00000f00", "#fffff0"],
        "Ivory2" : ["#00000e11","#eeeee0"],
        "Ivory3" : ["#00000c32", "#cdcdc1"],
        "Ivory4" : ["#00000874","#8b8b83"],
        "Khaki" : ["#000a640f","#f0e68c"],
        "Khaki1" : ["#00097000", "#fff68f"],
        "Khaki2" : ["#00086911","#eee685"],
        "Khaki3" : ["#00075a32", "#cdc673"],
        "Khaki4" : ["#00053d74","#8b864e"],
        "Lavender" : ["#14140005", "#e6e6fa"],
        "LavenderBlush" : ["#000f0a00","#fff0f5"],
        "LavenderBlush1" : ["#000f0a00","#fff0f5"],
        "LavenderBlush2" : ["#000e0911","#eee0e5"],
        "LavenderBlush3" : ["#000c0832","#cdc1c5"],
        "LavenderBlush4" : ["#00080574","#8b8386"],
        "LawnGreen" : ["#8000fc03","#7cfc00"],
        "LemonChiffon" : ["#00053200", "#fffacd"],
        "LemonChiffon1" : ["#00053200","#fffacd"],
        "LemonChiffon2" : ["#00052f11","#eee9bf"],
        "LemonChiffon3" : ["#00042832","#cdc9a5"],
        "LemonChiffon4" : ["#00021b74","#8b8970"],
        "LightBlue" : ["#390e0019","#add8e6"],
        "LightBlue1" : ["#40100000","#bfefff"],
        "LightBlue2" : ["#3c0f0011", "#b2dfee"],
        "LightBlue3" : ["#330d0032", "#9ac0cd"],
        "LightBlue4" : ["#23080074","#68838b"],
        "LightCoral" : ["#0070700f","#f08080"],
        "LightCyan" : ["#1f000000","#e0ffff"],
        "LightCyan1" : ["#1f000000","#e0ffff"],
        "LightCyan2" : ["#1d000011","#d1eeee"],
        "LightCyan3" : ["#19000032","#b4cdcd"],
        "LightCyan4" : ["#11000074","#7a8b8b"],
        "LightGoldenrod" : ["#00116c11","#eedd82"],
        "LightGoldenrod1" : ["#00137400","#ffec8b"],
        "LightGoldenrod2" : ["#00126c11","#eedc82"],
        "LightGoldenrod3" : ["#000f5d32","#cdbe70"],
        "LightGoldenrod4" : ["#000a3f74","#8b814c"],
        "LightGoldenrodYellow" : ["#00002805","#fafad2"],
        "LightGreen" : ["#5e005e11", "#90ee90"],
        "LightGrey" : ["#0000002c","#d3d3d3"],
        "LightPink" : ["#00493e00","#ffb6c1"],
        "LightPink1" : ["#00514600", "#ffaeb9"],
        "LightPink2" : ["#004c4111", "#eea2ad"],
        "LightPink3" : ["#00413832","#cd8c95"],
        "LightPink4" : ["#002c2674","#8b5f65"],
        "LightSalmon" : ["#005f8500", "#ffa07a"],
        "LightSalmon1" : ["#005f8500","#ffa07a"],
        "LightSalmon2" : ["#00597c11","#ee9572"],
        "LightSalmon3" : ["#004c6b32","#cd8162"],
        "LightSalmon4" : ["#00344974","#8b5742"],
        "LightSeaGreen" : ["#9200084d", "#20b2aa"],
        "LightSkyBlue" : ["#732c0005","#87cefa"],
        "LightSkyBlue1" : ["#4f1d0000","#b0e2ff"],
        "LightSkyBlue2" : ["#4a1b0011", "#a4d3ee"],
        "LightSkyBlue3" : ["#40170032", "#8db6cd"],
        "LightSkyBlue4" : ["#2b100074","#607b8b"],
        "LightSlateBlue" : ["#7b8f0000","#8470ff"],
        "LightSlateGrey" : ["#22110066","#778899"],
        "LightSteelBlue" : ["#2e1a0021","#b0c4de"],
        "LightSteelBlue1" : ["#351e0000","#cae1ff"],
        "LightSteelBlue2" : ["#321c0011","#bcd2ee"],
        "LightSteelBlue3" : ["#2b180032","#a2b5cd"],
        "LightSteelBlue4" : ["#1d100074","#6e7b8b"],
        "LightYellow" : ["#00001f00","#ffffe0"],
        "LightYellow1" : ["#00001f00", "#ffffe0"],
        "LightYellow2" : ["#00001d11", "#eeeed1"],
        "LightYellow3" : ["#00001932","#cdcdb4"],
        "LightYellow4" : ["#00001174","#8b8b7a"],
        "LimeGreen" : ["#9b009b32", "#32cd32"],
        "Linen" : ["#000a1405","#faf0e6"],
        "Magenta" : ["#00ff0000","#ff00ff"],
        "Magenta1" : ["#00ff0000","#ff00ff"],
        "Magenta2" : ["#00ee0011","#ee00ee"],
        "Magenta3" : ["#00cd0032","#cd00cd"],
        "Magenta4" : ["#008b0074","#8b008b"],
        "Maroon" : ["#0080504f","#b03060"],
        "Maroon1" : ["#00cb4c00","#ff34b3"],
        "Maroon2" : ["#00be4711","#ee30a7"],
        "Maroon3" : ["#00a43d32","#cd2990"],
        "Maroon4" : ["#006f2974","#8b1c62"],
        "MediumAquamarine" : ["#67002332","#66cdaa"],
        "MediumBlue" : ["#cdcd0032","#0000cd"],
        "MediumOrchid" : ["#197e002c", "#ba55d3"],
        "MediumOrchid1" : ["#1f990000", "#e066ff"],
        "MediumOrchid2" : ["#1d8f0011", "#d15fee"],
        "MediumOrchid3" : ["#197b0032", "#b452cd"],
        "MediumOrchid4" : ["#11540074","#7a378b"],
        "MediumPurple" : ["#486b0024","#9370db"],
        "MediumPurple1" : ["#547d0000","#ab82ff"],
        "MediumPurple2" : ["#4f750011", "#9f79ee"],
        "MediumPurple3" : ["#44650032","#8968cd"],
        "MediumPurple4" : ["#2e440074","#5d478b"],
        "MediumSeaGreen" : ["#7700424c","#3cb371"],
        "MediumSlateBlue" : ["#73860011","#7b68ee"],
        "MediumSpringGreen" : ["#fa006005","#00fa9a"],
        "MediumTurquoise" : ["#8900052e","#48d1cc"],
        "MediumVioletRed" : ["#00b24238", "#c71585"],
        "MidnightBlue" : ["#5757008f", "#191970"],
        "MintCream" : ["#0a000500","#f5fffa"],
        "MistyRose" : ["#001b1e00", "#ffe4e1"],
        "MistyRose1" : ["#001b1e00","#ffe4e1"],
        "MistyRose2" : ["#00191c11","#eed5d2"],
        "MistyRose3" : ["#00161832","#cdb7b5"],
        "MistyRose4" : ["#000e1074","#8b7d7b"],
        "Moccasin" : ["#001b4a00","#ffe4b5"],
        "NavajoWhite" : ["#00215200","#ffdead"],
        "NavajoWhite1" : ["#00215200","#ffdead"],
        "NavajoWhite2" : ["#001f4d11","#eecfa1"],
        "NavajoWhite3" : ["#001a4232","#cdb38b"],
        "NavajoWhite4" : ["#00122d74","#8b795e"],
        "NavyBlue" : ["#8080007f","#000080"],
        "OldLace" : ["#00081702","#fdf5e6"],
        "OliveDrab" : ["#23006b71","#6b8e23"],
        "OliveDrab1" : ["#3f00c100","#c0ff3e"],
        "OliveDrab2" : ["#3b00b411","#b3ee3a"],
        "OliveDrab3" : ["#33009b32","#9acd32"],
        "OliveDrab4" : ["#22006974","#698b22"],
        "Orange" : ["#005aff00","#ffa500"],
        "Orange1" : ["#005aff00","#ffa500"],
        "Orange2" : ["#0054ee11", "#ee9a00"],
        "Orange3" : ["#0048cd32","#cd8500"],
        "Orange4" : ["#00318b74","#8b5a00"],
        "OrangeRed" : ["#00baff00","#ff4500"],
        "OrangeRed1" : ["#00baff00","#ff4500"],
        "OrangeRed2" : ["#00aeee11","#ee4000"],
        "OrangeRed3" : ["#0096cd32","#cd3700"],
        "OrangeRed4" : ["#00668b74","#8b2500"],
        "Orchid" : ["#006a0425","#da70d6"],
        "Orchid1" : ["#007c0500", "#ff83fa"],
        "Orchid2" : ["#00740511","#ee7ae9"],
        "Orchid3" : ["#00640432","#cd69c9"],
        "Orchid4" : ["#00440274","#8b4789"],
        "PaleGoldenrod" : ["#00064411","#eee8aa"],
        "PaleGreen" : ["#63006304","#98fb98"],
        "PaleGreen1" : ["#65006500","#9aff9a"],
        "PaleGreen2" : ["#5e005e11","#90ee90"],
        "PaleGreen3" : ["#51005132", "#7ccd7c"],
        "PaleGreen4" : ["#37003774","#548b54"],
        "PaleTurquoise" : ["#3f000011", "#afeeee"],
        "PaleTurquoise1" : ["#44000000", "#bbffff"],
        "PaleTurquoise2" : ["#40000011","#aeeeee"],
        "PaleTurquoise3" : ["#37000032","#96cdcd"],
        "PaleTurquoise4" : ["#25000074","#668b8b"],
        "PaleVioletRed" : ["#006b4824","#db7093"],
        "PaleVioletRed1" : ["#007d5400","#ff82ab"],
        "PaleVioletRed2" : ["#00754f11","#ee799f"],
        "PaleVioletRed3" : ["#00654432","#cd6889"],
        "PaleVioletRed4" : ["#00442e74","#8b475d"],
        "PapayaWhip" : ["#00102a00","#ffefd5"],
        "PeachPuff" : ["#00254600","#ffdab9"],
        "PeachPuff1" : ["#00254600","#ffdab9"],
        "PeachPuff2" : ["#00234111","#eecbad"],
        "PeachPuff3" : ["#001e3832", "#cdaf95"],
        "PeachPuff4" : ["#00142674","#8b7765"],
        "Peru" : ["#00488e32", "#cd853f"],
        "Pink" : ["#003f3400","#ffc0cb"],
        "Pink1" : ["#004a3a00", "#ffb5c5"],
        "Pink2" : ["#00453611", "#eea9b8"],
        "Pink3" : ["#003c2f32", "#cd919e"],
        "Pink4" : ["#00281f74", "#8b636c"],
        "Plum" : ["#003d0022", "#dda0dd"],
        "Plum1" : ["#00440000", "#ffbbff"],
        "Plum2" : ["#00400011","#eeaeee"],
        "Plum3" : ["#00370032", "#cd96cd"],
        "Plum4" : ["#00250074","#8b668b"],
        "PowderBlue" : ["#36060019", "#b0e0e6"],
        "Purple" : ["#50d0000f", "#a020f0"],
        "Purple1" : ["#64cf0000", "#9b30ff"],
        "Purple2" : ["#5dc20011", "#912cee"],
        "Purple3" : ["#50a70032", "#7d26cd"],
        "Purple4" : ["#36710074", "#551a8b"],
        "Red" : ["#00ffff00", "#ff0000"],
        "Red1" : ["#00ffff00","#ff0000"],
        "Red2" : ["#00eeee11","#ee0000"],
        "Red3" : ["#00cdcd32","#cd0000"],
        "Red4" : ["#008b8b74","#8b0000"],
        "RosyBrown" : ["#002d2d43","#bc8f8f"],
        "RosyBrown1" : ["#003e3e00","#ffc1c1"],
        "RosyBrown2" : ["#003a3a11","#eeb4b4"],
        "RosyBrown3" : ["#00323232","#cd9b9b"],
        "RosyBrown4" : ["#00222274","#8b6969"],
        "RoyalBlue" : ["#a078001e", "#4169e1"],
        "RoyalBlue1" : ["#b7890000","#4876ff"],
        "RoyalBlue2" : ["#ab800011", "#436eee"],
        "RoyalBlue3" : ["#936e0032","#3a5fcd"],
        "RoyalBlue4" : ["#644b0074","#27408b"],
        "SaddleBrown" : ["#00467874","#8b4513"],
        "Salmon" : ["#007a8805", "#fa8072"],
        "Salmon1" : ["#00739600","#ff8c69"],
        "Salmon2" : ["#006c8c11","#ee8262"],
        "Salmon3" : ["#005d7932","#cd7054"],
        "Salmon4" : ["#003f5274","#8b4c39"],
        "SandyBrown" : ["#0050940b", "#f4a460"],
        "SeaGreen" : ["#5d003474","#2e8b57"],
        "SeaGreen1" : ["#ab006000","#54ff9f"],
        "SeaGreen2" : ["#a0005a11","#4eee94"],
        "SeaGreen3" : ["#8a004d32","#43cd80"],
        "SeaGreen4" : ["#5d003474","#2e8b57"],
        "Seashell" : ["#000a1100","#fff5ee"],
        "Seashell1" : ["#000a1100","#fff5ee"],
        "Seashell2" : ["#00091011","#eee5de"],
        "Seashell3" : ["#00080e32","#cdc5bf"],
        "Seashell4" : ["#00050974","#8b8682"],
        "Sienna" : ["#004e735f", "#a0522d"],
        "Sienna1" : ["#007db800","#ff8247"],
        "Sienna2" : ["#0075ac11","#ee7942"],
        "Sienna3" : ["#00659432","#cd6839"],
        "Sienna4" : ["#00446574","#8b4726"],
        "SkyBlue" : ["#641d0014","#87ceeb"],
        "SkyBlue1" : ["#78310000", "#87ceff"],
        "SkyBlue2" : ["#702e0011", "#7ec0ee"],
        "SkyBlue3" : ["#61270032","#6ca6cd"],
        "SkyBlue4" : ["#411b0074","#4a708b"],
        "SlateBlue" : ["#63730032","#6a5acd"],
        "SlateBlue1" : ["#7c900000","#836fff"],
        "SlateBlue2" : ["#74870011", "#7a67ee"],
        "SlateBlue3" : ["#64740032", "#6959cd"],
        "SlateBlue4" : ["#444f0074","#473c8b"],
        "SlateGrey" : ["#2010006f","#708090"],
        "SlateGrey1" : ["#391d0000","#c6e2ff"],
        "SlateGrey2" : ["#351b0011","#b9d3ee"],
        "SlateGrey3" : ["#2e170032","#9fb6cd"],
        "SlateGrey4" : ["#1f100074", "#6c7b8b"],
        "Snow" : ["#00050500","#fffafa"],
        "Snow1" : ["#00050500","#fffafa"],
        "Snow2" : ["#00050511","#eee9e9"],
        "Snow3" : ["#00040432","#cdc9c9"],
        "Snow4" : ["#00020274","#8b8989"],
        "SpringGreen" : ["#ff008000","#00ff7f"],
        "SpringGreen1" : ["#ff008000","#00ff7f"],
        "SpringGreen2" : ["#ee007811","#00ee76"],
        "SpringGreen3" : ["#cd006732","#00cd66"],
        "SpringGreen4" : ["#8b004674","#008b45"],
        "SteelBlue" : ["#6e32004b", "#4682b4"],
        "SteelBlue1" : ["#9c470000","#63b8ff"],
        "SteelBlue2" : ["#92420011","#5cacee"],
        "SteelBlue3" : ["#7e390032","#4f94cd"],
        "SteelBlue4" : ["#55270074","#36648b"],
        "Tan" : ["#001e462d", "#d2b48c"],
        "Tan1" : ["#005ab000","#ffa54f"],
        "Tan2" : ["#0054a511","#ee9a49"],
        "Tan3" : ["#00488e32","#cd853f"],
        "Tan4" : ["#00316074","#8b5a2b"],
        "Thistle" : ["#00190027","#d8bfd8"],
        "Thistle1" : ["#001e0000","#ffe1ff"],
        "Thistle2" : ["#001c0011","#eed2ee"],
        "Thistle3" : ["#00180032","#cdb5cd"],
        "Thistle4" : ["#00100074","#8b7b8b"],
        "Tomato" : ["#009cb800","#ff6347"],
        "Tomato1" : ["#009cb800","#ff6347"],
        "Tomato2" : ["#0092ac11","#ee5c42"],
        "Tomato3" : ["#007e9432","#cd4f39"],
        "Tomato4" : ["#00556574","#8b3626"],
        "Turquoise" : ["#a000101f","#40e0d0"],
        "Turquoise1" : ["#ff0a0000","#00f5ff"],
        "Turquoise2" : ["#ee090011","#00e5ee"],
        "Turquoise3" : ["#cd080032", "#00c5cd"],
        "Turquoise4" : ["#8b050074","#00868b"],
        "Violet" : ["#006c0011", "#ee82ee"],
        "VioletRed" : ["#00b0402f","#d02090"],
        "VioletRed1" : ["#00c16900","#ff3e96"],
        "VioletRed2" : ["#00b46211","#ee3a8c"],
        "VioletRed3" : ["#009b5532","#cd3278"],
        "VioletRed4" : ["#00693974","#8b2252"],
        "Wheat" : ["#0017420a", "#f5deb3"],
        "Wheat1" : ["#00184500","#ffe7ba"],
        "Wheat2" : ["#00164011", "#eed8ae"],
        "Wheat3" : ["#00133732","#cdba96"],
        "Wheat4" : ["#000d2574", "#8b7e66"],
        "White" : ["#00000000","#ffffff"],
        "WhiteSmoke" : ["#0000000a","#f5f5f5"],
        "Yellow" : ["#0000ff00","#ffff00"],
        "Yellow1" : ["#0000ff00","#ffff00"],
        "Yellow2" : ["#0000ee11","#eeee00"],
        "Yellow3" : ["#0000cd32","#cdcd00"],
        "Yellow4" : ["#00008b74","#8b8b00"],
        "YellowGreen" : ["#33009b32","#9acd32"],
        "None" : ["#00000000","#000000"]}
