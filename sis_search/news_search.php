<?php
    include_once("news_query.php");
    function search_by_title($con,$title_keyword){
        return mysqli_query($con,"select * from news_header where title like '%$title_keyword%'");
    }

    function search_by_author($con,$author_keyword){
        $author_id_list = get_author_id_from_author_name($con,$author_keyword);
        $id_list = array();
        for ($i=0;$i<mysqli_num_rows($author_id_list);$i++){
            array_push($id_list,mysqli_fetch_row($author_id_list)[0]);
        }
        /*for ($i=0;$i<mysqli_num_rows($author_id_list);$i++){
            echo $id_list[$i];
            echo '<br>';
            
        }*/
     //   $id_list = implode(',', $id_list);
        return mysqli_query($con,"select * from news_header where author_id in (".implode(",",$id_list).")");
    }

    function search_by_body($con,$body_keyword){
        return mysqli_query($con,"select * from news_header where news_content like '%$body_keyword%'");
    }

    function search_by_source($con,$source_keyword){
        return mysqli_query($con,"select * from news_header where title like '%$title_keyword%'");
    }
?>