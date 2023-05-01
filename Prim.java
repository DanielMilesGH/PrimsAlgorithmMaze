import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Random;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.AccessDeniedException;


public class Prim {

    // function to get adjacents to adge
    public static ArrayList<int[]> getAdj(int[] point, int m, int n) {
        // setup the return
        ArrayList<int[]> adjLst = new ArrayList<>();

        // if (point.get(0)-1 >= 0) {
        //     adjLst.add(new int[]{point.get(0)-1, point.get(1)});
        // }
        // if (point.get(0)+1 < m) {
        //     adjLst.add(new int[]{point.get(0)+1, point.get(1)});
        // }
        // if (point.get(0)-1 >=0) {
        //     adjLst.add(new int[]{point.get(0), point.get(1)-1});
        // }
        // if (point.get(0)+1 < n) {
        //     adjLst.add(new int[]{point.get(0), point.get(1)+1});
        // }

        if (point[0]-1 >= 0) {
            adjLst.add(new int[]{point[0], point[1],
                                 point[0]-1, point[1]});
        }
        if (point[0]+1 < m) {
            adjLst.add(new int[]{point[0], point[1],
                                 point[0]+1, point[1]});
        }
        if (point[1]-1 >=0) {
            adjLst.add(new int[]{point[0], point[1],
                                 point[0], point[1]-1});
        }
        if (point[1]+1 < n) {
            adjLst.add(new int[]{point[0], point[1],
                                 point[0], point[1]+1});
        }
        return adjLst;
    }

    public static void main (String[] args) {
        // default to 0x0 grid
        int m = 0; // number of rows
        int n = 0; // number of columns
        try {
            m = Integer.parseInt(args[0]);
            n = Integer.parseInt(args[1]);
        }
        catch (NumberFormatException e) {
            System.err.println("Argument" + args[0] + " must be an integer.");
            System.exit(1);
        }
        
        // total vtx = m*n
        // creating tree, so we want eventually x*y - 1 edges
        
        /*
         * Algorithm Layout:
         * Start at any vertex (we'll choose 0,0)
         * add an edge {u,v}
         * such that u is in T and v is not
         * 
         * To do this, can look at every vertex u inside t
         * and get adjacents
        */
        ArrayList<int[]> vertices = new ArrayList<int[]>();
        HashSet<Integer> verticesHashed = new HashSet<>();
        ArrayList<int[]> edges = new ArrayList<int[]>();
        HashSet<Integer> edgesHashed = new HashSet<>();

        // start with (0,0) -> (1,0)
        vertices.add(new int[]{0, 0});
        
        // now setup while loop, while we don't have enough edges
        // to form a tree
        int randomVtx;
        int randomIdx;
        Random rand = new Random(); 
        int mod;
        boolean notAdded = true;
        int[] vtxToCheck;
        int counter = 0;
        while (edgesHashed.size()-100 < (m*n)-1) {
            // randomly select a vertex
            randomVtx = rand.nextInt(vertices.size());
            // now get adjacents of this vertex
            ArrayList<int[]> adjs = getAdj(vertices.get(randomVtx),m,n);
            // randomly select a neighbor, try 4 times before giving up
            randomIdx = rand.nextInt(4);
            mod = adjs.size();
            // System.out.println(vertices.size());
            for (int i=0; i<4;i++) {
                if (notAdded) {
                    vtxToCheck = new int[]{adjs.get((randomIdx+i)%mod)[2],
                                           adjs.get((randomIdx+i)%mod)[3]};
                    
                    // if (!(verticesHashed.contains(Arrays.hashCode(vtxToCheck)))) {
                    if (!(verticesHashed.contains(Arrays.toString(vtxToCheck).hashCode()))) {

                    // if (!(vertices.contains(new int[]{adjs.get((randomIdx+i)%mod)[2],
                    //                                   adjs.get((randomIdx+i)%mod)[3]}))) {
                        // if in here, then we can add this edge, and the new vertex
                        edges.add(adjs.get((randomIdx+i) % mod));
                        edgesHashed.add(Arrays.hashCode(adjs.get((randomIdx+i) % mod)));
                        vertices.add(vtxToCheck);
                        verticesHashed.add(Arrays.toString(vtxToCheck).hashCode());
                        notAdded=false;
                        counter=0;
                    }
                }
            }
            notAdded=true;
            counter+=1;
            if (counter > 100000) {
                System.out.println("breaking out");
                break;
            }
        }

        // ArrayList<int[]> tst = getAdj(new ArrayList<Integer>(Arrays.asList(1,1)),m,n);


        // for (int i=0;i<tst.size();i++) {
        //     System.out.println(Arrays.toString(tst.get(i)).hashCode());
        //     System.out.println(Arrays.toString(tst.get(i)).hashCode());
        //     System.out.println(Arrays.toString(tst.get(i)).hashCode());
        //     System.out.println('new:')
        // }
        
        System.out.println("Tree Edge Count: " + (m*n - 1));
        System.out.println("Hashed Edge Count: " + edgesHashed.size());
        System.out.println("Edge Count: " + edges.size());
        System.out.println("Hashed Vertex Count: " + verticesHashed.size());
        System.out.println("Vertex Count: " + vertices.size());

        try {
            FileWriter myWriter = new FileWriter("tree.txt");
            myWriter.write('[');
            for (int i=0; i<edges.size()-1; i++) {
                myWriter.write(Arrays.toString(edges.get(i))+",\n");
            }

            myWriter.write(Arrays.toString(edges.get(edges.size()-1))+']');
            myWriter.close();
            System.out.println("Successfully wrote to the file.");
          } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
          }

        // now running dijkstra
        System.out.println("Finding path:");
        // create a distance and prev lists
        int[] dist = new int[verticesHashed.size()];
        int[] prev = new int[verticesHashed.size()];
        for (int i=0; i<verticesHashed.size(); i++) {
            dist[i] = Integer.MAX_VALUE;
            prev[i] = -1;
        }

        

    }
}
