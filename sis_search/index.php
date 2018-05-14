<html>
    <head>
        <?php
        include_once("news_query.php");
        include_once("database_account.php");
        $data = mysqli_query($con,"select * from news_header limit 60");

        ?>
        </script>
    </head>
    <body>
        <div class="input">
            <form method="get" action="search_result.php">
                請輸入查詢內容:<br>
                利用標題查詢:<input type="text" name="search_by_title_input">
                <input type="submit" value="查詢"/><br>
            </form>
            <form method="get" action="search_result.php">
                利用作者查詢:<input type="text" name="search_by_author_input">
                <input type="submit" value="查詢"/><br>
            </form>
            <form method="get" action="search_result.php">
                利用內文關鍵字查詢:<input type="text" name="search_by_body_input">
                <input type="submit" value="查詢"/><br>
            </form>
            <form method="get" action="search_result.php">
                利用新聞來源查詢:<input type="text" name="search_by_source_input">
                <input type="submit" value="查詢"/><br>
            </form>
            <form method="get" action="search_result.php">
                利用產品廠牌查詢CVE:<input type="text" name="cve_search_by_vendor_input">
                排序依照:
                <select name="sort_by">
                　<option value="CVE_id">CVEID</option>
                　<option value="PublishedDate">發布日期</option>
                　<option value="Score">分數</option>
                </select>
                <select name="cend">
                　<option value="desc">從高到低</option>
                　<option value="asc">從低到高</option>
                </select>
                <input type="submit" value="查詢"/><br>
            </form>
        </div>
        <div class="show_result_table">
            <?php
                show_news_result_table($con,$data);
            ?>
        </div>
    </body>
</html>