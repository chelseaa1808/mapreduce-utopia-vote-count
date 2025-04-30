
# Utopia Vote Count - Hadoop MapReduce (Python Version)

This project replicates a Java-based MapReduce tutorial using Python and Hadoop Streaming (https://github.com/satishpatil2k13/Horton_Works-Hadoop-Tutorials/blob/master/Community/T09_Write_And_Run_Your_Own_MapReduce_Java_Program_Poll_Result_Analysis.md). The goal is to analyze poll results from the fictional Utopia dataset by counting total votes per candidate.

## Example Input
Utopia|CandidateA Utopia|CandidateB Utopia|CandidateA

## MapReduce Job Flow
- **Mapper**: Emits (Candidate, 1) pairs from each line.
- **Reducer**: Sums votes per candidate.

## Sample Output
CandidateA 2 CandidateB 1

## Run Instructions

1. Start Hadoop environment (Cloudera VM or Docker).
2. Upload `poll_input.txt` to HDFS.
   # Upload to HDFS
<pre>hdfs dfs -mkdir -p /user/cloudera/utopia
hdfs dfs -put poll_input.txt /user/cloudera/utopia/ 
</pre>

4. Run the Hadoop streaming job with `mapper.py` and `reducer.py`.
   # Run MapReduce

<pre>hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
  -input /user/cloudera/utopia/poll_input.txt \
  -output /user/cloudera/utopia/output \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py
</pre>

5. View results from HDFS output.
   # Check Output
<pre>hdfs dfs -cat /user/cloudera/utopia/output/part-00000 
</pre>

## Author

Chelsea Anestal


