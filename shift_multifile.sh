#!/bin/bash

c=0
while [ $c -lt 100 ]; do
	nmrshift frm$c.pdb
	let "c++"
done

