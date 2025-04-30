
# Utopia Vote Count - Hadoop MapReduce (Python Version)

This project replicates a Java-based MapReduce tutorial using Python and Hadoop Streaming. The goal is to analyze poll results from the fictional Utopia dataset by counting total votes per candidate.

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
3. Run the Hadoop streaming job with `mapper.py` and `reducer.py`.
4. View results from HDFS output.

## Author

Chelsea Anestal


