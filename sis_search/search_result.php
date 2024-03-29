<html>
    <head>
        <?php
        include_once("news_query.php");
        include_once("news_search.php");
        include_once("cve_query.php");
        include_once("cve_search.php");
        include_once("database_account.php");
        ?>
    </head>
    <body>
        <?php
            $title_input="";
            $author_input="";
            $body_input="";
            $source_input="";
            $cve_vendor_input="";
            $result_is_news=TRUE;
            $sotr_by="";
            $cend="";
            if (isset($_GET['search_by_title_input']))
                $title_input = $_GET['search_by_title_input'];
            if (isset($_GET['search_by_author_input']))
                $author_input = $_GET['search_by_author_input'];
            if (isset($_GET['search_by_body_input']))
                $body_input = $_GET['search_by_body_input'];
            if (isset($_GET['search_by_source_input']))
                $source_input = $_GET['search_by_source_input'];
            if(isset($_GET['cve_search_by_vendor_input']))
                $cve_vendor_input = $_GET['cve_search_by_vendor_input'];
            if(isset($_GET['sort_by']))
                $sort_by = $_GET['sort_by'];
            if(isset($_GET['cend']))
                $cend = $_GET['cend'];
            //Record the search start time,TRUE means the function will return float value;
            $search_start_time = microtime(TRUE);

            if($title_input!=""){
                echo "以下是 標題搜尋 \"$title_input\" 的搜尋結果:";
                $data = search_by_title($con,$title_input);
            }
            else if($author_input!=""){
                echo "以下是 作者搜尋 \"$author_input\" 的搜尋結果:";
                $data = search_by_author($con,$author_input);
            }
            else if($body_input!=""){
                echo "以下是 內文關鍵字搜尋 \"$body_input\" 的搜尋結果:";
                
                $data = search_by_body_keyword($con,$body_input);
                //$data = search_by_body_tag($con,$body_input);
                //$data = search_by_body_full_text($con,$body_input);
            }
            else if($source_input!=""){
                echo "以下是 新聞來源搜尋 \"$source_input\" 的搜尋結果:";
                $data = search_by_source($con,$source_input);
            }
            else if($cve_vendor_input!=""){
                //表示結果須以CVE格式顯示
                $result_is_news=FALSE;
                echo "以下是 利用產品廠商查詢CVE \"$cve_vendor_input\" 的搜尋結果:";
                //cve_search_by_vendor($con,[vendor_name],[sort by(cve_id or score or date)],[desc or asc])
                //$data = cve_search_by_vendor($con,$cve_vendor_input,$sort_by,$cend);
            }
            else{
                $data = FALSE;
            }

            //Record the search end time,TRUE means the function will return float value;
            $search_end_time =microtime(TRUE);

            if($data==FALSE){
                echo "Not Found!";
            }
            else if($result_is_news){
                //Show the total search time.
                echo "Search time:".($search_end_time-$search_start_time)."(s)";
                //Show the news search result.
                show_news_result_table($con,$data);
            }
            else{
                //Show the total search time.
                echo "Search time:".($search_end_time-$search_start_time)."(s)";
                //Show the CVE search result;
                show_cve_result_table($con,$data);
            }
        ?>
    </body>
</html>