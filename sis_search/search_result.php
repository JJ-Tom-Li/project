<html>
    <head>
        <?php
        include_once("news_query.php");
        include_once("news_search.php");
        $con = mysqli_connect("localhost","root","root");
        mysqli_select_db($con,"sis");
        ?>
    </head>
    <body>
        <?php
            $title_input="";
            $author_input="";
            $body_input="";
            $source_input="";
            if (isset($_GET['search_by_title_input']))
                $title_input = $_GET['search_by_title_input'];
            if (isset($_GET['search_by_author_input']))
                $author_input = $_GET['search_by_author_input'];
            if (isset($_GET['search_by_body_input']))
                $body_input = $_GET['search_by_body_input'];
            if (isset($_GET['search_by_source_input']))
                $source_input = $_GET['search_by_source_input'];

            if($title_input!=""){
                $data = search_by_title($con,$title_input);
            }
            else if($author_input!=""){
                $data = search_by_author($con,$author_input);
            }
            else if($body_input!=""){
                $data = search_by_body($con,$body_input);
            }
            else if($source_input!=""){
                $data = search_by_source($con,$source_input);
            }
            else{
                $data = FALSE;
            }
            
            if($data==FALSE){
                echo "Not Fuond!";
            }
            else
                show_result_table($con,$data);
        ?>
    </body>
</html>