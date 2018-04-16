<?php
//-----------------------title------------------------------------
    function get_title_from_news_id($con,$news_id){
        $result = mysqli_query($con
        ,"select title from news_header where news_id=$news_id");
        return mysqli_fetch_row($result)[0]; 
    }

//-----------------------news_link------------------------------------
    function get_news_link_from_news_id($con,$news_id){
        $result = mysqli_query($con
        ,"select news_link from news_content where news_id=$news_id");
        return mysqli_fetch_row($result)[0]; 
    }

//-----------------------author------------------------------------
    function get_author_name_from_news_id($con,$news_id){
        //First get the author id.
        $result = mysqli_query($con
        ,"select author_id from news_header where news_id=$news_id");
        //Use author id to get author name.
        $result = get_author_name_from_author_id($con,mysqli_fetch_row($result)[0]);
        return $result; 
    }

    function get_author_link_from_news_id($con,$news_id){
        //First get the author id.
        $result = mysqli_query($con
        ,"select author_id from news_header where news_id=$news_id");
        //Use author id to get author name.
        $result = get_author_link_from_author_id($con,mysqli_fetch_row($result)[0]);
        return $result; 
    }

    function get_author_name_from_author_id($con,$author_id){
        $result = mysqli_query($con
        ,"select author_name from news_author where author_id=$author_id");
        return mysqli_fetch_row($result)[0];
    }

    function get_author_link_from_author_id($con,$author_id){
        $result = mysqli_query($con
        ,"select author_link from news_author where author_id=$author_id");
        return mysqli_fetch_row($result)[0];
    }

    function get_author_id_from_author_name($con,$author_name){
        $result = mysqli_query($con
        ,"select author_id from news_author where author_name like '%$author_name%'");
        return $result;
    }

//-----------------------date------------------------------------
    function get_date_from_news_id($con,$news_id){
        $result = mysqli_query($con
        ,"select date from news_header where news_id=$news_id");
        return mysqli_fetch_row($result)[0]; 
    }

//-----------------------news_source------------------------------------
    function get_news_source_from_news_id($con,$news_id){
        $result = mysqli_query($con
        ,"select news_source from news_header where news_id=$news_id");
        return mysqli_fetch_row($result)[0]; 
    }

//-----------------------news_body------------------------------------    
    function get_news_body_from_news_id($con,$news_id){
        $result = mysqli_query($con
        ,"select news_body from news_content where news_id=$news_id");
        return mysqli_fetch_row($result)[0]; 
    }

//-----------------------topic------------------------------------
    function get_topic_name_from_topic_id($con,$topic_id){
        $result = mysqli_query($con
        ,"select topic_name from news_topic where topic_id=$topic_id");
        return mysqli_fetch_row($result)[0]; 
    }

//-----------------------show result------------------------------------
    function show_result_table($con,$data){
        ?>
        <table name="news_list">
                <tr>
                    <td>News id</td>
                    <td>News title</td>
                    <td>Date</td>
                    <td>Author</td>
                    <td>Source</td>
                </tr>
                <?php
                    for($i=1;$i<=mysqli_num_rows($data);$i++){
                        $rs=mysqli_fetch_row($data);
                    ?>
                        <tr>
                            <td><?php echo $rs[0]?></td>
                            <td><a href="<?php echo "news.php?news_id=".$rs[0]?>"> <?php echo $rs[1]?> </a></td>
                            <td><?php echo $rs[2]?></td>
                            <td><a href="<?php echo get_author_link_from_author_id($con,$rs[3])?>"><?php echo get_author_name_from_author_id($con,$rs[3])?></a></td>
                            <td><?php echo $rs[4]?></td>
                        </tr>
                    <?php
                    }
                ?>
            </table>
            <?php
    }
?>