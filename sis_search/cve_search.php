<?php
    include_once("cve_query.php");

    function cve_search_by_vendor($con,$cve_vendor_input,$sort_by="cve_id",$cend="desc"){
        
        //利用CVE的vendor name搜尋
        $cve_list = mysqli_query($con,"select distinct cve_id from cve_to_product where product_id in
                                            (select product_id from cve_product where vendor_id in
                                                (select vendor_id from cve_vendor where vendor_name like '$cve_vendor_input'))
                                    ");

        //Turn list into string array.
        $id_list = array();
        for ($i=0;$i<mysqli_num_rows($cve_list);$i++){
            array_push($id_list,"'".mysqli_fetch_row($cve_list)[0]."'");
        }

        //Get result cve_id list.
        $cve_list = mysqli_query($con,"select cve_id from cve_header where cve_id in 
                                        (".implode(", ",$id_list).") order by $sort_by $cend;");
        /* //Turn list into string array.
        $id_list = array();
        for ($i=0;$i<mysqli_num_rows($cve_list);$i++){
            array_push($id_list,mysqli_fetch_row($cve_list)[0]);
        }

        return mysqli_query($con,"select * from cve_header where cve_id in (".implode(",",$id_list).")");
        */
        return $cve_list;
    }
?>