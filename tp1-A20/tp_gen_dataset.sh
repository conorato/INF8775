for i in {1..10}; do
  let nsamples=100*2**i
  echo "Generating a set with $nsamples couples"

  for j in {1..10}; do
    python gen.py $nsamples ./data/testset1/ex_${nsamples}_$j.txt
  done
done
