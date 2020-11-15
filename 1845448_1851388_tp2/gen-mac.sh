for n in {100,500,1000,5000,10000,50000,100000}; do
  echo "generating for $n samples"
  for i in {1..10}; do
    # Génération d'une permutation de 1 à 3n
    gshuf -i 1-$((3*$n)) |
    awk 'BEGIN {i=0} {printf $1; if (++i%3==0) printf "\n"; else printf " "}' |
    awk '{
      printf $1; if ($2 < $3) print " "$2" "$3; else print " "$3" "$2;
      printf $2; if ($1 < $3) print " "$1" "$3; else print " "$3" "$1;
      printf $3; if ($1 < $2) print " "$1" "$2; else print " "$2" "$1;
    }' > dataset1/b_${n}_${i}.txt
  done
done
