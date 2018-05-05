<?php
//-----------------------Description------------------------------------
    function get_des_from_cve_id($con,$cve_id){
        $result = mysqli_query($con
        ,"select cve_description from cve_content where cve_id like '%$cve_id%'");
        return mysqli_fetch_row($result)[0]; 
    }

//-----------------------cve_link------------------------------------
    function get_cve_link_from_cve_id($con,$cve_id){
        return "https://www.cvedetails.com/cve/".$cve_id; 
    }

//-----------------------vendor------------------------------------
    function get_vendor_name_from_vendor_id($con,$vendor_id){
        //First get the vendor id.
        $result = mysqli_query($con
        ,"select vendor_name from cve_vendor where vendor_id=$vendor_id");
        return mysqli_fetch_row($result)[0]; 
    }
//-----------------------product------------------------------------
    function get_product_name_from_cve_id($con,$cve_id){
        $result = mysqli_query($con
        ,"select product_name,product_ver,vendor_id from cve_product
            where product_id in
                (select product_id from cve_to_product where cve_id='$cve_id')");
        return $result; 
    }
//-----------------------date------------------------------------
    function get_published_date_from_cve_id($con,$cve_id){
        $result = mysqli_query($con
        ,"select publishedDate from cve_header where cve_id like '%$cve_id%'");
        return mysqli_fetch_row($result)[0]; 
    }

    function get_lastModified_date_from_cve_id($con,$cve_id){
        $result = mysqli_query($con
        ,"select lastModifiedDate from cve_header where cve_id like '%$cve_id%'");
        return mysqli_fetch_row($result)[0]; 
    }

//-----------------------score------------------------------------
    function get_score_from_cve_id($con,$cve_id){
        $result = mysqli_query($con
        ,"select score from cve_header where cve_id like '%$cve_id%'");
        return mysqli_fetch_row($result)[0]; 
    }

//-----------------------show result------------------------------------
    function show_cve_result_table($con,$data){
        ?>
        <table name="cve_list">
                <tr>
                    <td>CVE id</td>
                    <td>CVE Description</td>
                    <td>Published Date</td>
                    <td>Score</td>
                </tr>
                <?php
                    for($i=1;$i<=mysqli_num_rows($data);$i++){
                        $rs=mysqli_fetch_row($data);
                    ?>
                        <tr>
                            <!--CVE id-->
                            <td><a href="<?php echo "cve.php?cve_id=".$rs[0]?>"><?php echo $rs[0]?> </a></td>
                            <!--CVE Description-->
                            <td><?php echo get_des_from_cve_id($con,$rs[0]),0,200?></td>
                            <!--published Date-->
                            <td><?php echo get_published_date_from_cve_id($con,$rs[0])?></td>
                            <!--CVSS score-->
                            <td><?php echo get_score_from_cve_id($con,$rs[0])?></td>
                        </tr>
                    <?php
                    }
                ?>
            </table>
            <?php
    }
?>