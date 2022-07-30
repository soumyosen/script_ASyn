set nf [molinfo 0 get numframes]
set segments [list B1 B2 C1 C2 D1 D2 E1 E2 F1 F2 G1 G2 H1 H2 I1 I2 J1 J2 K1 K2 L1 L2 M1 M2 N1 N2 O1 O2 P1 P2 Q1 Q2 R1 R2 S1 S2] 

mol new ../../ionized.psf
mol addfile ../../ionized.pdb


foreach seg $segments {
	set fp [open "100ns_$seg.dat" w]
	set b_sel [atomselect 1 "segname $seg and ((resid 35 to 46) or (resid 62 to 96)) and backbone and noh"]


	for {set i 0} {$i < $nf} {incr i} {
		molinfo 0 set frame $i
		set a_sel [atomselect 0 "segname $seg and ((resid 35 to 46) or (resid 62 to 96)) and backbone and noh"]
		set transform_matrix [measure fit $a_sel $b_sel]
		set all [atomselect 0 all frame $i]
		$all move $transform_matrix
		set rms [measure rmsd $a_sel $b_sel]
		set tim [expr $i*0.04]
		puts $fp "$tim $rms"
		$a_sel delete
		$all delete
	}
	$b_sel delete
	close $fp
}




