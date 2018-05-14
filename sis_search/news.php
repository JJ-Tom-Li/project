<html>
    <head>
        <?php
            //Include functions.
            include_once("news_query.php");
            include_once("database_account.php");

            function show_news($con,$news_id){
                $title = get_title_from_news_id($con,$news_id);
                $news_link = get_news_link_from_news_id($con,$news_id);
                $author_name = get_author_name_from_news_id($con,$news_id);
                $author_link = get_author_link_from_news_id($con,$news_id);
                $date = get_date_from_news_id($con,$news_id);
                $news_source = get_news_source_from_news_id($con,$news_id);
                $news_body = get_news_body_from_news_id($con,$news_id);
                $news_tag = get_news_tag_from_news_id($con,$news_id);

                ?>
                <table class="show_news" style="border:3px #cccccc solid;" cellpadding="10" border='1'>
                    <tr>
                        <td>Title</td>
                        <td><?php echo $title?></td>
                    </tr>
                    <tr>
                        <td>新聞連結</td>
                        <td><a href="<?php echo $news_link?>">點此前往</a></td>
                    </tr>
                    <tr>
                        <td>作者</td>
                        <td><?php echo $author_name?></td>
                    </tr>
                    <tr>
                        <td>作者連結</td>
                        <td><?php echo $author_link?></td>
                    </tr>
                    <tr>
                        <td>發布日期</td>
                        <td><?php echo $date?></td>
                    </tr>
                    <tr>
                        <td>新聞來源</td>
                        <td><?php echo $news_source?></td>
                    </tr>
                    <tr>
                        <td>內文</td>
                        <td><?php echo $news_body?></td>
                    </tr>
                    <tr>
                        <td>標籤</td>
                        <td>
                        <?php 
                            //Show the tags
                            //$rs[0] is the tag name
                            //$rs[1] is the tag link
                            for($i=1;$i<=mysqli_num_rows($news_tag);$i++){
                            $rs=mysqli_fetch_row($news_tag);?>
                            <a href="<?php echo $rs[1] ?>"><?php echo $rs[0]?> </a><br>
                            <?php
                            }
                            ?>
                        </td>
                    </tr>
                </table>
                <?php
            }
        ?>
    </head>
    <body>
            <?php
                $news_id = $_GET['news_id'];
                show_news($con,$news_id);
            ?>
    </body>
</html>