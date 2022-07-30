

set prot1seg [list B1 C1 D1 E1 F1 G1 H1 I1 J1 K1 L1 M1 N1 O1 P1 Q1 R1 S1]
set prot1segall [list A1 B1 C1 D1 E1 F1 G1 H1 I1 J1 K1 L1 M1 N1 O1 P1 Q1 R1 S1 T1]

set prot2seg [list B2 C2 D2 E2 F2 G2 H2 I2 J2 K2 L2 M2 N2 O2 P2 Q2 R2 S2]
set prot2segall [list A2 B2 C2 D2 E2 F2 G2 H2 I2 J2 K2 L2 M2 N2 O2 P2 Q2 R2 S2 T2] 

set residue1 80 
set residue2 35
set atom1 NZ
set atom2 CD


proc shortestdist {seglist seg residuenum1 residuenum2 atomname1 atomname2} {
	set closestdist 9999.0
	set closestseg arb
	set cent1 [measure center [atomselect top "segname $seg and resid $residuenum1 and name $atomname1"]]
	foreach sega $seglist {
		set cent2 [measure center [atomselect top "segname $sega and resid $residuenum2 and name $atomname2"]]
		set distance [vecdist $cent2 $cent1]
		if {$distance < $closestdist} {
			set closestdist $distance
			set closestseg $sega
		} 

	}

	return [list $closestseg $closestdist]
}

set sum 0.0

foreach seg1 $prot1seg {
	set shortest_seg_dist_prot1 [shortestdist $prot1segall $seg1 $residue1 $residue2 $atom1 $atom2]
	set shortest_seg [lindex $shortest_seg_dist_prot1 0]
	set shortest_dist [lindex $shortest_seg_dist_prot1 1]
	set sum [expr $sum + $shortest_dist]
	puts "$seg1 $shortest_seg $shortest_dist"
}

foreach seg2 $prot2seg {
        set shortest_seg_dist_prot2 [shortestdist $prot2segall $seg2 $residue1 $residue2 $atom1 $atom2]
        set shortest_seg [lindex $shortest_seg_dist_prot2 0]
        set shortest_dist [lindex $shortest_seg_dist_prot2 1]
        set sum [expr $sum + $shortest_dist]
        puts "$seg2 $shortest_seg $shortest_dist"                       
}
		
set avg [expr $sum/36.0]
puts "average $avg"
