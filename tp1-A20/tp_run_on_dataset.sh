echo "algo,emplacement,taille,temps" > ./data/results.csv

for algo in "brute" "recursif" "seuil"; do
  for ex in $(ls data/testset1/); do
    sample_size=$(echo $ex | cut -d_ -f2)
    if [ $algo != "brute" ] || [ $sample_size -lt 10000 ]
    then
      time=$(./tp.sh -a ${algo} -e data/testset1/$ex -t)
      echo $algo,"data/testset1",$sample_size,$time
    fi
  done
done >> ./data/results.csv
