<?php
    include_once("news_query.php");
    function search_by_title($con,$title_keyword){
        return mysqli_query($con,"select * from news_header where title like '%$title_keyword%'");
    }

    function search_by_author($con,$author_keyword){
        //First get the list of author ids.
        $author_id_list = get_author_id_from_author_name($con,$author_keyword);

        //Turn list into string array.
        $id_list = array();
        for ($i=0;$i<mysqli_num_rows($author_id_list);$i++){
            array_push($id_list,mysqli_fetch_row($author_id_list)[0]);
        }

        return mysqli_query($con,"select * from news_header where author_id in (".implode(",",$id_list).")");
    }

    function search_by_body($con,$body_keyword){
        $news_list = mysqli_query($con,"select news_id from news_content where news_body like '%$body_keyword%'");
        
        //Turn list into string array.
        $id_list = array();
        for ($i=0;$i<mysqli_num_rows($news_list);$i++){
            array_push($id_list,mysqli_fetch_row($news_list)[0]);
        }
        return mysqli_query($con,"select * from news_header where news_id in (".implode(",",$id_list).")");
    }

    function search_by_source($con,$source_keyword){
        return mysqli_query($con,"select * from news_header where news_source like '%$source_keyword%'");
    }
?>