set psf "../../ionized.psf"            
set trj "../../last50frames.dcd"

set scripts [list "intracontact1.tcl" "intracontact_energy.tcl"]

set firstresidue 31
set lastresidue 100
set max_residue_per_run 5

set totalnumresidue [expr $lastresidue-$firstresidue+1]

if {[expr $totalnumresidue%$max_residue_per_run] == 0} {
	set numVMD [expr $totalnumresidue/$max_residue_per_run]
} else {
	set numVMD [expr [expr $totalnumresidue/$max_residue_per_run] + 1]
}

for {set i 0} {$i < $numVMD} {incr i} {
	set first [expr 31 + ($i*$max_residue_per_run)]
	set last [expr ($first + $max_residue_per_run) - 1]
	if {$last > $lastresidue} {
		set last $lastresidue
	}
	set inScript [open [lindex $scripts 0] r]	
	set outScript [open "VMD[format %02d ${i}].tcl" w]

	puts $outScript "mol new $psf"
	puts $outScript "mol addfile $trj waitfor all"
	
	set inline [gets $inScript]
        set indicator 0
	while {$indicator == 0} {
        	puts $outScript $inline
    		set inline [gets $inScript]
		if {[regexp Main $inline]>0} {
			set indicator 1
		}

    	}
	puts $outScript "set first $first"
	puts $outScript "set last $last"
	set inline [gets $inScript]
	set inline [gets $inScript]
	set inline [gets $inScript]
 	
	while { ! [eof $inScript]} {
		puts $outScript $inline
		set inline [gets $inScript]
	}
	close $inScript
	puts $outScript "sed -i 1,38d contact_prob[format %02d ${i}].log"
	puts $outScript "exit"
	close $outScript
}

#for {set i 0} {$i<$numVMD} {incr i} {
#    exec gnome-terminal -e "vmd -dispdev text -e VMD[format %02d ${i}].tcl | tee contact_prob[format %02d ${i}].log "
#    after 1000
#}
	

