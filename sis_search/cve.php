<html>
    <head>
        <?php
            //Include functions.
            include_once("cve_query.php");
            //Link to database.
            $con = mysqli_connect("localhost","root","root");
            mysqli_select_db($con,"sis");

            function show_news($con,$cve_id){
                $cve_link = get_cve_link_from_cve_id($con,$cve_id);
                $product_name = get_product_name_from_cve_id($con,$cve_id);
                $published_date = get_published_date_from_cve_id($con,$cve_id);
                $lastModified_date = get_lastModified_date_from_cve_id($con,$cve_id);
                $score = get_score_from_cve_id($con,$cve_id);
                $description = get_des_from_cve_id($con,$cve_id);

                ?>
                <table class="show_news" style="border:3px #cccccc solid;" cellpadding="10" border='1'>
                    <tr>
                        <td>CVE_ID</td>
                        <td><?php echo $cve_id?></td>
                    </tr>
                    <tr>
                        <td>CVE_detail連結</td>
                        <td><a href="<?php echo $cve_link?>">點此前往</a></td>
                    </tr>
                    <tr>
                        <td>發布日期</td>
                        <td><?php echo $published_date?></td>
                    </tr>
                    <tr>
                        <td>最後修改日期</td>
                        <td><?php echo $lastModified_date?></td>
                    </tr>
                    <tr>
                        <td>CVSS分數</td>
                        <td><?php echo $score?></td>
                    </tr>
                    <tr>
                        <td>漏洞描述</td>
                        <td><?php echo $description?></td>
                    </tr>
                    <tr>
                        <td>影響產品</td>
                        <td>
                            <table class="show_product" style="border:3px #cccccc solid;" cellpadding="10" border='1'>
                                <tr>
                                    <td>#</td>
                                    <td>product name</td>
                                    <td>vendor name</td>
                                    <td>product version</td>
                                </tr>
                                
                                <?php 
                                    //Show the products
                                    //$rs[0] is the product name
                                    for($i=1;$i<=mysqli_num_rows($product_name);$i++){
                                        ?><tr><?php
                                        $rs=mysqli_fetch_row($product_name);?>
                                        <td>
                                            <a><?php echo $i?> </a>
                                        </td>
                                        <td>
                                            <a><?php echo $rs[0]?> </a>
                                        </td>
                                        <td>
                                            <a><?php echo get_vendor_name_from_vendor_id($con,$rs[2])?> </a>
                                        </td>
                                        <td>
                                            <a><?php echo $rs[1]?> </a>
                                        </td>
                                        </tr>
                                        <?php
                                    }
                                    ?>
                            </table>
                        
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