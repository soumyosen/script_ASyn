
#set fp [open "twist.dat" w]

##########################################
set fp [open "twist_trj.dat" w]

####### Calculation of twist angle with respect to positive y axis
set chainlist [list B C D E F G H I J K L M N O P Q R S]
set gap [expr [llength $chainlist] -1]

set sel1 [atomselect top "chain B C D E F G H I J K L M N O P Q R S and name CA" frame 0]
set nf [molinfo top get numframes]

proc XYplaneAngle {vector} {
	set zproj [vecscale {0 0 1} [vecdot $vector {0 0 1}]]
	set XYplane_comp [vecsub $vector $zproj]
	set XYplane_comp_norm [vecnorm $XYplane_comp]
	set ang1 [expr acos([vecdot {1 0 0} $XYplane_comp_norm])]
	set ang1deg [expr $ang1 * 57.3]
	return $ang1deg
}

set seglist1 [list B1 C1 D1 E1 F1 G1 H1 I1 J1 K1 L1 M1 N1 O1 P1 Q1 R1 S1]
set seglist2 [list B2 C2 D2 E2 F2 G2 H2 I2 J2 K2 L2 M2 N2 O2 P2 Q2 R2 S2]


for {set k 0} {$k < $nf} {incr k} {
	molinfo top set frame $k
	set sel2 [atomselect top "chain B C D E F G H I J K L M N O P Q R S and name CA"]
	set all [atomselect top all]
	set tm [measure fit $sel2 $sel1]
	$all move $tm
	set angles []
	foreach seg1 $seglist1 seg2 $seglist2 {
		set atom_gr1_cent [measure center [atomselect top "segname $seg1 and resid 75 to 91 and backbone and name CA"] weight mass]
		set atom_gr2_cent [measure center [atomselect top "segname $seg2 and resid 75 to 91 and backbone and name CA"] weight mass]
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
close $fp
