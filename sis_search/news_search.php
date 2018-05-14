<?php
    include_once("news_query.php");

    function search_by_title($con,$title_keyword){
        //第一步先搜尋整個keyword完整出現的標題，如:... solar product...
        //第二步再搜尋標題部分是keyword的標題，如:... Solaris product...
        return mysqli_query($con,"select * from news_header where title like '% $title_keyword %' 
                                union 
                                select * from news_header where title like '%$title_keyword%'");
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
//---------------------------search body-----------------------------------------
    function search_by_body_full_text($con,$body_keyword,$sort_by="",$cend="desc"){
        //全文搜尋
        $id_list = array();
        $body_keyword = mb_split("\s",$body_keyword);
        foreach ($body_keyword as $word){
            $news_list = mysqli_query($con,"select news_id from news_content where news_body like '% $word %'
                                            union
                                            select news_id from news_content where news_body like '%$word%'");
            
            //Turn list into string array.
            //$id_list = array();
            for ($i=0;$i<mysqli_num_rows($news_list);$i++){
                $tmp = mysqli_fetch_row($news_list)[0];
                array_push($id_list,$tmp);
            }
        }

        $id_list = array_count_values($id_list);
        arsort($id_list);
        /*foreach($id_list as $id){
            echo "<br>".$id;
        }*/
        $id_list = array_keys($id_list);

        if($sort_by=="")
            return mysqli_query($con,"select distinct * from news_header where news_id in (".implode(",",$id_list).")
                                        order by field (news_id,".implode(",",$id_list).")");
        else{
            return mysqli_query($con,"select distinct * from news_header where news_id in 
                                        (".implode(",",$id_list).") order by $sort_by $cend");
        }
    }

    function search_by_body_tag($con,$body_keyword,$sort_by="",$cend="desc"){
        //利用文章的tag搜尋
        $news_list = mysqli_query($con,"select news_id from news_to_tag where tag_id in
                                            (select tag_id from news_tag where tag_name like '% $body_keyword %'
                                            union
                                            select tag_id from news_tag where tag_name like '%$body_keyword%')");
        
        //Turn list into string array.
        $id_list = array();
        for ($i=0;$i<mysqli_num_rows($news_list);$i++){
            $tmp = mysqli_fetch_row($news_list)[0];
            array_push($id_list,$tmp);
        }
        if($sort_by=="")
            return mysqli_query($con,"select * from news_header where news_id in (".implode(",",$id_list).")");
        else{
            return mysqli_query($con,"select * from news_header where news_id in 
                                        (".implode(",",$id_list).") order by $sort_by $cend");
        }
    }

    function search_by_body_keyword($con,$body_keyword,$sort_by="keyword_tfidf",$cend="desc"){

        //This list will store the result news_id list.
        $id_list = array();

        //Split the keyword by space.
        $body_keyword = mb_split("\s",$body_keyword);

        //Get the number of parts of keyword.
        $number_of_keyword = count($body_keyword);

        //Parse the parts of keyword one by one.
        foreach ($body_keyword as $word){
            //利用文章的關鍵字搜尋
            $news_list = mysqli_query($con,"select news_id from news_to_keyword where keyword_id in
                                                (select keyword_id from news_keyword where keyword_name like '$word')");
                                               // union
                                               // select keyword_id from news_keyword where keyword_name like '%$word%')
                                               // order by keyword_tfidf");
            
            //Turn list into string array.
            for ($i=0;$i<mysqli_num_rows($news_list);$i++){
                $tmp = mysqli_fetch_row($news_list)[0];
                array_push($id_list,$tmp);
            }
            
        }
        /*if($sort_by=="keyword_tfidf"){
            return mysqli_query($con,"select distinct news_id,title,Date,author_id,news_source from ( select * from news_header where news_id in 
                                            (".implode(",",$id_list).") ) as T natural join news_to_keyword; ");
        }
        else{
            return mysqli_query($con,"select distinct * from news_header where news_id in 
                                        (".implode(",",$id_list).") order by $sort_by $cend");
        }*/

        /*
            The following code aims to sort the news_id list by their times of appearing.
        */
        $news_id_list = array(); //Store the result news_id array.
        $id_list = array_count_values($id_list); //count the times of appearing.
        $keys = array_keys($id_list); //Get the news_id
        //arsort($id_list);
        $i = 0;
        foreach($id_list as $id){
            if ($id>=$number_of_keyword){
                //Push to result list.
                array_push($news_id_list,$keys[$i]);
            }
            $i++;
        }
        //$id_list = array_keys($id_list);
        
        return mysqli_query($con,"select * from news_header where news_id in 
                                        (".implode(",",$news_id_list).")
                                        order by field (news_id,".implode(",",$news_id_list).")");
    }
//-------------------------------------------------------------------------------------
    function search_by_source($con,$source_keyword){
        return mysqli_query($con,"select * from news_header where news_source like '%$source_keyword%'");
    }
?>