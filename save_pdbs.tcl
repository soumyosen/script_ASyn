
set seglist [list H1 H2 I1 I2 J1 J2 K1 K2 L1 L2 M1 M2]

set chainlist [list A B C D E F G H I J K L]

set nf [molinfo top get numframes]



for {set i 0} {$i < $nf} {incr i} {
	molinfo top set frame $i
	foreach seg $seglist chain $chainlist {
		[atomselect top "protein and segname $seg"] set chain $chain
	}

	[atomselect top "protein and segname $seglist and resid 31 to 102"] writepdb frm$i.pdb
}
