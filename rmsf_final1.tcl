###################### Measure rmsf $sel1 ---> gives rmsf of all individual atoms
###################### present in the selection
set nf [molinfo 0 get numframes]

mol new ../../ionized.psf
mol addfile ../../ionized.pdb

set firstresidue 30
set lastresidue 103
set total_num_residue [expr $lastresidue - $firstresidue + 1]

set ref [atomselect 1 "chain B C D E F G H I J K L M N O P Q R S and name CA"]

#################### Calculating the average RMSF 
proc avglist {l} {
	set len [llength $l]
	set tot 0.0
	for {set k 0} {$k < $len} {incr k} {
		set rmsfind [lindex $l $k]
		set tot [expr $tot + $rmsfind]
	}
	set avg [expr $tot/$len]
	return $avg
}


#################### Alingning the frames
for {set i 0} {$i < $nf} {incr i} {
	molinfo 0 set frame $i
	set atoms [atomselect 0 "chain B C D E F G H I J K L M N O P Q R S and name CA"]
	set allatoms [atomselect 0 all]
	set tm [measure fit $atoms $ref]
	$allatoms move $tm
	$atoms delete
	$allatoms delete
}
$ref delete

############## Calculation of RMSF 
set all_residue_rmsf {}
for {set j $firstresidue} {$j <= $lastresidue} {incr j} {
	set sel1 [atomselect 0 "chain B C D E F G H I J K L M N O P Q R S and resid $j and noh"]
	set rmsf [measure rmsf $sel1]
	set rmsfavg [avglist $rmsf]
	lappend all_residue_rmsf $rmsfavg
	$sel1 delete
	}

#####################################################################################

############# Writing output in a file with first column showing residue id and the
############# next column is RMSF
set fp [open "rmsf_final1a_100ns.dat" w]

for {set r 0} {$r < $total_num_residue} {incr r} {
	set rmsfn [lindex $all_residue_rmsf $r]
	set resid [expr $r + $firstresidue]
	puts $fp "$resid $rmsfn"
}

close $fp
####################################################################################

	
		
