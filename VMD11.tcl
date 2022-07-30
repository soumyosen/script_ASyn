mol new ../../ionized.psf
mol addfile ../../last50frames.dcd waitfor all
set nf [molinfo top get numframes]
set firstresidue 31 
set lastresidue 100
set chainlist [list B1 B2 C1 C2 D1 D2 E1 E2 F1 F2 G1 G2 H1 H2 I1 I2 J1 J2 K1 K2 L1 L2 M1 M2 N1 N2 O1 O2 P1 P2 Q1 Q2 R1 R2 S1 S2]
set normalization [expr $nf*[llength $chainlist]]
set totalnumresidue [expr $lastresidue-$firstresidue+1]

proc CTprobability {resid} {
	global nf chainlist normalization totalnumresidue
	set total {}
	for {set c 1} {$c <= $totalnumresidue} {incr c} {
                lappend total 0
        }

	for {set i 0} {$i < $nf} {incr i} {
                molinfo top set frame $i
                foreach chain $chainlist {
                        set sel1 [atomselect top "segname $chain and resid $resid and noh"]
                        set count {}
                        for {set k 31} {$k <= 100} {incr k} {
                                set sel2 [atomselect top "segname $chain and resid $k and noh"]
                                set contact [measure contacts 4.0 $sel1 $sel2]
                                if {[llength [lindex $contact 0]] != 0} {
                                        lappend count 1
                                } else {
                                        lappend count 0
                                }
                                $sel2 delete
                        }
                        set total [vecadd $total $count]
                        $sel1 delete
                }
        }
        set probability [vecscale [expr 1.0/$normalization] $total]
        return $probability
}

set first 86
set last 90
for {set j $first} {$j <= $last} {incr j} {
	set prob [CTprobability $j]
	puts "$prob"
}

sed -i 1,38d contact_prob11.log
exit
