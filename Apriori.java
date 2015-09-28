import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;


/**
 * Created by yangdekun on 2015/9/28.
 */
public class Apriori {

    private List<Set> transactionList = new LinkedList<Set>();
    private Map<Set, Integer> frequencyMap = new HashMap<Set, Integer>();

    private void loadDataFromFile(String fileName) {
        File file = new File(fileName);
        BufferedReader reader = null;
        try {
            reader = new BufferedReader(new FileReader(file));
            String currentString;
            while ((currentString = reader.readLine()) != null) {
                String[] items = currentString.split(",");
                Set<String> transaction = new HashSet(items);
                transactionList.add(transaction);
            }
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException e1) {

                }
            }
        }
    }

    // generate one itemset
    private Set<Set> generateOneItemset() {
        Set<Set> oneItemset = new HashSet<Set>();
        for (Set<String> transaction : transactionList) {
            for (String item : transaction) {
                // only have one item
                Set<String> curSet = new HashSet<String>();
                curSet.add(item);
                
                oneItemset.add(curSet);
                
                // counting frequency
                if (frequencyMap.containsKey(curSet)) {
                    Integer count = frequencyMap.get(curSet);
                    frequencyMap.put(curSet, count + 1);
                } else {
                    frequencyMap.put(curSet, 1);
                }
            }
        }
        
        return oneItemset; 
    }

    public void run(String fileName) {
        // read dataset form file
        loadDataFromFile(fileName);

        Set<Set> oneItemset = generateOneItemset();

    }
}
