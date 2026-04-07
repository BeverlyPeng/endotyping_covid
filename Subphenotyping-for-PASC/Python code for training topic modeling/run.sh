
for i in {1..10}
do
    python3 ./Main_train_topic_model_test.py >> ../../data_likelihood_sinai/output_${i}.txt
done
