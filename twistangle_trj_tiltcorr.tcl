
#set fp [open "twist.dat" w]

##########################################
set fp [open "twist_trj.dat" w]

####### Calculation of twist angle with respect to positive y axis
set chainlist [list B C D E F G H I J K L M N O P Q R S]
set gap [expr [llength $chainlist] -1]

set sel1 [atomselect top "not chain A T and name CA" frame 0]
set nf [molinfo top get numframes]

proc XYplaneAngle {vector} {
	set zproj [vecscale {0 0 1} [vecdot $vector {0 0 1}]]
	set XYplane_comp [vecsub $vector $zproj]
	set XYplane_comp_norm [vecnorm $XYplane_comp]
	set ang1 [expr acos([vecdot {1 0 0} $XYplane_comp_norm])]
	set ang1deg [expr $ang1 * 57.3]
	return $ang1deg
}

for {set k 0} {$k < $nf} {incr k} {
	molinfo top set frame $k
	set sel2 [atomselect top "not chain A T and name CA"]
	set all [atomselect top all]
	set tm [measure fit $sel2 $sel1]
	$all move $tm
	set angles []
	foreach chain $chainlist {
		set atom_gr1_cent [measure center [atomselect top "segname ${chain}2 and resid 53 and backbone and noh"]]
		set atom_gr2_cent [measure center [atomselect top "segname ${chain}1 and resid 53 and backbone and noh"]]
		set v [vecsub $atom_gr1_cent $atom_gr2_cent]
		#puts "$v"
		set ang [XYplaneAngle $v]
        	lappend angles $ang
	}
	#puts $angles
	$sel2 delete
	$all delete
##########################################

######## Average twist angle for a particular frame
	set totalang 0.0
	puts "$k $angles"
	for {set j 0} {$j < $gap} {incr j} {
		set relang [expr [lindex $angles [expr $j+1]] - [lindex $angles $j]]
		set absrelang [expr abs($relang)]
		set totalang [expr $totalang + $absrelang]
	}

	set avgang [expr $totalang/$gap]
	set tim [expr $k*0.04]
	puts $fp "$tim $avgang"
}
	
$sel1 delete
flush $fp
close $fp
