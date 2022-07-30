##################### "measure contacts" command give two lists of atoms which are within a specific distance.
###################### Each list shows the list of atoms from one selection

#set nf [molinfo top get numframes]

set chainlist [list B2 C2 D2 E2 F2 G2 H2 I2 J2 K2 L2 M2 N2 O2 P2 Q2 R2 S2]

set firstresidue 30
set lastresidue 103

proc createlist {residuenum} {
	global firstresidue
	global lastresidue
	set first [expr $residuenum + 2]
	set residuelist {}
	for {set s $first} {$s <= $lastresidue} {incr s} {
		 lappend residuelist $s
	}
	return $residuelist
}

 
for {set k 1000} {$k < 1500} {incr k} {
	molinfo top set frame $k
	set total 0
	foreach i $chainlist {
		for {set j $firstresidue} {$j < [expr $lastresidue - 1]} {incr j} {
			set reslist [createlist $j]
			set sel1 [atomselect top "protein and segname $i and resid $j and noh"]
			set sel2 [atomselect top "protein and segname $i and resid $reslist and noh"]
			set contactlist [measure contacts 4.0 $sel1 $sel2]
        		set num [llength [lindex $contactlist 0]]
        		set total [expr $total+$num]
			$sel1 delete
			$sel2 delete
		}
	}
	
	set tim [expr $k * 0.04]
	puts "$tim $total"
}

