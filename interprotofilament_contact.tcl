##################### "measure contacts" command give two lists of atoms which are within a specific distance.
###################### Each list shows the list of atoms from one selection

set nf [molinfo top get numframes]

set fp [open "contact_interprotofilament.dat" w]


for {set k 0} {$k <= $nf} {incr k} {
	molinfo top set frame $k
	set sel1 [atomselect top "protein and segname B1 C1 D1 E1 F1 G1 H1 I1 J1 K1 L1 M1 N1 O1 P1 Q1 R1 S1 and resid 30 to 103 and noh"]
	set sel2 [atomselect top "protein and segname B2 C2 D2 E2 F2 G2 H2 I2 J2 K2 L2 M2 N2 O2 P2 Q2 R2 S2 and resid 30 to 103 and noh"]
	set contactlist [measure contacts 4.0 $sel1 $sel2]
        set num [llength [lindex $contactlist 0]]
	$sel1 delete
	$sel2 delete
	set tim [expr $k * 0.04]
	puts $fp "$tim $num"
}

close $fp	
