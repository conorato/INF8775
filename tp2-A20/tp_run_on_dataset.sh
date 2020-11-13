algo=vorace
# algo=progdyn
# algo=tabou

folder=dataset
results_file=./results/results_${algo}.csv

echo "algo,emplacement,taille,temps,hauteur" > ${results_file}

for ex in $(ls $folder); do
  sample_size=$(echo $ex | cut -d_ -f2)
  time_height=$(./tp.sh -a ${algo} -e $folder/$ex -t -r)
  time=$(echo ${time_height} | cut -d ' ' -f1)
  height=$(echo ${time_height} | cut -d ' ' -f2)
  echo $algo,$folder,$sample_size,$time,$height
done >> ${results_file}
