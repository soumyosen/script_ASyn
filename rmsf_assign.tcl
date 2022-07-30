set fp [open "rmsf_final1a_100ns.dat" r]
set file_data [read $fp]
close $fp

set data [split $file_data "\n"]

set residue {}
set beta {}

foreach line $data {
	set field [split $line " "]
	#puts "$field"
	lappend residue [lindex $field 0]
	lappend beta [lindex $field 1]
}

#puts "[llength $residue]"
#puts "[llength $beta]"

set num [llength $residue]
set idx [expr $num-1]

set residue [lreplace $residue $idx $idx]
set beta [lreplace $beta $idx $idx]

#puts "[llength $residue]"
#puts "[llength $beta]"


puts "$residue"
puts "$beta"

foreach r $residue b $beta {
	[atomselect top "protein and resid $r"] set beta $b
}

[atomselect top "protein and resid 30"] set beta 2.5
[atomselect top "protein and resid 102"] set beta 2.5
[atomselect top "protein and resid 103"] set beta 2.5

[atomselect top all] writepdb ionized_beta_rmsf_100ns_a.pdb
