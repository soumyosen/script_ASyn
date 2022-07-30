set nf [molinfo 0 get numframes]

set fp [open "rmsd_trj_100ns.dat" w]

mol new ../../ionized.psf
mol addfile ../../ionized.pdb

set b_sel [atomselect 1 "chain B C D E F G H I J K L M N O P Q R S and ((resid 35 to 46) or (resid 62 to 96)) and backbone and noh"]


for {set i 0} {$i < $nf} {incr i} {
	molinfo 0 set frame $i
	set a_sel [atomselect 0 "chain B C D E F G H I J K L M N O P Q R S and ((resid 35 to 46) or (resid 62 to 96)) and backbone and noh"]
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
