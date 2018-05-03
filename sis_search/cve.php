<html>
    <head>
        <?php
            //Include functions.
            include_once("cve_query.php");
            //Link to database.
            $con = mysqli_connect("localhost","root","root");
            mysqli_select_db($con,"sis");

            function show_news($con,$cve_id){
                $title = get_title_from_cve_id($con,$cve_id);
                $news_link = get_news_link_from_cve_id($con,$cve_id);
                $author_name = get_author_name_from_cve_id($con,$cve_id);
                $author_link = get_author_link_from_cve_id($con,$cve_id);
                $date = get_date_from_cve_id($con,$cve_id);
                $news_source = get_news_source_from_cve_id($con,$cve_id);
                $news_body = get_news_body_from_cve_id($con,$cve_id);
                $news_tag = get_news_tag_from_cve_id($con,$cve_id);

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
                $cve_id = $_GET['cve_id'];
                show_news($con,$cve_id);
            ?>
    </body>
</html>